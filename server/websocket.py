from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer


class WebSocketHandler(WebSocket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handleMessage(self):
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        WebSocketManagement.add_client(self)

    def handleClose(self):
        WebSocketManagement.remove_client(self)
        print(self.address, 'closed')


class WebSocketManagement:
    clients = []

    @staticmethod
    def add_client(client):
        WebSocketManagement.clients.append(client)

    @staticmethod
    def remove_client(client):
        WebSocketManagement.clients.remove(client)

    @staticmethod
    def get_clients():
        return WebSocketManagement.clients


class WebSocketServer:

    def start(self):
        print("Dashboard socket başlatıldı")
        self.server = SimpleWebSocketServer(
            'localhost', 8000, WebSocketHandler)
        self.server.serveforever()

    def stop(self):
        self.server.close()

    @staticmethod
    def broadcast(message):
        for client in WebSocketManagement.get_clients():
            client.sendMessage(message)
