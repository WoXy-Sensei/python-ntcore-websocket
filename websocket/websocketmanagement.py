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