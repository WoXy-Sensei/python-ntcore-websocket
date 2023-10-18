from networktable.NetworkTableManagement import DashboardManagement  
from models.Entry import Entry

class WebSocketManagement:
    clients = []

    @staticmethod
    def add_client(client):
        WebSocketManagement.clients.append(client)
        entries = DashboardManagement.get_entries()
        
        for key, value in entries.items():
            entryName = key
            entryValue = None
            entryType = value.getTopic().getTypeString()
           
            entry = Entry(entryName,entryValue,entryType)
            
            WebSocketManagement.broadcast(entry);
        
        return client

    @staticmethod
    def remove_client(client):
        WebSocketManagement.clients.remove(client)
        return client

    @staticmethod
    def get_clients():
        return WebSocketManagement.clients
    
    @staticmethod
    def broadcast(entry : Entry):
        for client in WebSocketManagement.get_clients():
            entry = entry.getByJson()
            client.sendMessage(entry)