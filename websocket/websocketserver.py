from SimpleWebSocketServer import SimpleWebSocketServer
from websocket.websockethandler import WebSocketHandler
from websocket.websocketmanagement import WebSocketManagement
from dotenv import load_dotenv
import os
import json
from utils.printServer import printServer

class WebSocketServer:
    
    def __init__(self) -> None:
        load_dotenv()

    def start(self):
        printServer("Start websocket server")
        self.server = SimpleWebSocketServer(os.getenv("ws_host"), os.getenv("ws_port"), WebSocketHandler)
        self.server.serveforever()

    def stop(self):
        self.server.close()

    @staticmethod
    def broadcast(message):
        for client in WebSocketManagement.get_clients():
            json_string = json.dumps(message)
            client.sendMessage(json_string)
