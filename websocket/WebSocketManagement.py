from dashboard.DashboardManagement import DashboardManagement  
import json

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
           
            entry = {
                "name" : entryName,
                "value" : entryValue,
                "type" : entryType
            }
            
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
    def broadcast(message):
        for client in WebSocketManagement.get_clients():
            json_string = json.dumps(message)
            client.sendMessage(json_string)