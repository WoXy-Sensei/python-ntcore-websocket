import ntcore
import threading
import os
from dotenv import load_dotenv
from websocket import WebSocketServer


class Dashboard:
    def __init__(self) -> None:
        load_dotenv()

        inst = ntcore.NetworkTableInstance.getDefault()
        inst.startClient4(os.getenv("client_name"))
        inst.setServer(os.getenv("host_name"))
        self.lock = threading.Lock()
        self.values = []

        def _connect_cb(event: ntcore.Event):
            if event.is_(ntcore.EventFlags.kConnected):
                print("Connected to", event.data.remote_id)
            elif event.is_(ntcore.EventFlags.kDisconnected):
                print("Disconnected from", event.data.remote_id)

        self.connListenerHandle = inst.addConnectionListener(True, _connect_cb)

        datatable = inst.getTable(os.getenv("table_name"))

        def _on_change_value(event: ntcore.Event):
            with self.lock:
                WebSocketServer.broadcast("test")
                print(event.data, event.data.value)

        def _on_pub(event: ntcore.Event):

            if event.is_(ntcore.EventFlags.kPublish):
                print(event.data.name)
                self.sub = datatable.getDoubleTopic(
                    event.data.name.split('/')[-1]).subscribe(0.0)
                self.values.append(self.sub)
                inst.addListener(
                    self.sub, ntcore.EventFlags.kValueAll, _on_change_value)

        self.topicListenerHandle = inst.addListener(
            [datatable.getPath() + "/"], ntcore.EventFlags.kTopic, _on_pub
        )

    def periodic(self):
        pass

    def start(self):
        print("Dashboard başlatıldı")

    def close(self):
        inst = ntcore.NetworkTableInstance.getDefault()
        inst.removeListener(self.topicListenerHandle)
        inst.removeListener(self.connListenerHandle)
