from SimpleWebSocketServer import WebSocket
from utils.printServer import printServer
from websocket.websocketmanagement import WebSocketManagement


class WebSocketHandler(WebSocket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handleMessage(self):
        self.sendMessage(self.data)

    def handleConnected(self):
        printServer(f"{self.address} connected")
        WebSocketManagement.add_client(self)

    def handleClose(self):
        WebSocketManagement.remove_client(self)
        printServer(f"{self.address} closed")