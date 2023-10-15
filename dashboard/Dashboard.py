import ntcore
import threading
import os
from dotenv import load_dotenv
from websocket.WebSocketManagement import WebSocketManagement
from utils.printServer import printServer
from dashboard.DashboardManagement import DashboardManagement

class Dashboard:
    def __init__(self) -> None:
        load_dotenv()

        inst = ntcore.NetworkTableInstance.getDefault()
        inst.startClient4(os.getenv("client_name"))
        inst.setServer(os.getenv("host_name"))
        self.lock = threading.Lock()
    

        def _connect_cb(event: ntcore.Event):
            if event.is_(ntcore.EventFlags.kConnected):
                printServer(f"Connected to {event.data.remote_id}")
            elif event.is_(ntcore.EventFlags.kDisconnected):
                printServer(f"Disconnected from {event.data.remote_id}")

        self.connListenerHandle = inst.addConnectionListener(True, _connect_cb)

        datatable = inst.getTable(os.getenv("table_name"))

        def _on_change_value(event: ntcore.Event):

            with self.lock:
                DashboardManagement.set_entry("test3",354)
                name = str(event.data.topic.getName().split('/')[-1])
                value = event.data.value.value()
                type = str(event.data.topic.getTypeString())
               
                # printServer(f"{name} | Change value : {event.data.value.value()}")
        
                WebSocketManagement.broadcast({
                    "name" : name,
                    "value" : value,
                    "type" : type
                })


        def _on_pub(event: ntcore.Event):

            if event.is_(ntcore.EventFlags.kPublish):
                printServer(f"Publishing : {event.data.name}")
                self.entry = datatable.getEntry(event.data.name.split('/')[-1])
                self.entry.setInteger(412341234123)
                DashboardManagement.add_entry(self.entry)

                inst.addListener(self.entry, ntcore.EventFlags.kValueAll, _on_change_value)

        self.topicListenerHandle = inst.addListener(
            [datatable.getPath() + "/"], ntcore.EventFlags.kTopic, _on_pub
        )

    def periodic(self):
        pass

    def start(self):
        printServer("Start dashboard")

    def close(self):
        inst = ntcore.NetworkTableInstance.getDefault()
        inst.removeListener(self.topicListenerHandle)
        inst.removeListener(self.connListenerHandle)
