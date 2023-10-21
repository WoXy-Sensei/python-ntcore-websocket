import ntcore
import threading
from websocket.WebSocketManagement import WebSocketManagement
from utils.printServer import printServer
from networktable.NetworkTableManagement import NetworkTableManagement
from models.Entry import Entry
import eel

class NetworkTable:
    def __init__(self,client_name,host_name,table_name) -> None:

        self.client_name = client_name
        self.host_name = host_name
        self.table_name = table_name

        inst = ntcore.NetworkTableInstance.getDefault()
        inst.startClient4(self.client_name)
        inst.setServer(self.host_name)
        self.lock = threading.Lock()


        def _connect_cb(event: ntcore.Event):
            if event.is_(ntcore.EventFlags.kConnected):
                printServer(f"Connected to {event.data.remote_id}")
            elif event.is_(ntcore.EventFlags.kDisconnected):
                printServer(f"Disconnected from {event.data.remote_id}")

        self.connListenerHandle = inst.addConnectionListener(True, _connect_cb)

        datatable = inst.getTable(self.table_name)

        def _on_change_value(event: ntcore.Event):

            with self.lock:
                
                name = str(event.data.topic.getName().split('/')[-1])
                value = event.data.value.value()
                type = str(event.data.topic.getTypeString())
               
                printServer(f"{name} | Change value : {event.data.value.value()}")

                entry = Entry(name,value,type)

                WebSocketManagement.broadcast(entry)

        def _on_pub(event: ntcore.Event):

            if event.is_(ntcore.EventFlags.kPublish):
                printServer(f"Publishing : {event.data.name}")
                self.entry = datatable.getEntry(event.data.name.split('/')[-1])
                NetworkTableManagement.add_entry(self.entry)

                inst.addListener(self.entry, ntcore.EventFlags.kValueAll, _on_change_value)

        self.topicListenerHandle = inst.addListener(
            [datatable.getPath() + "/"], ntcore.EventFlags.kTopic, _on_pub
        )

    def periodic(self):
        pass

    def start(self):
        printServer("Start Dashboard")

    def close(self):
        inst = ntcore.NetworkTableInstance.getDefault()
        inst.removeListener(self.topicListenerHandle)
        inst.removeListener(self.connListenerHandle)
