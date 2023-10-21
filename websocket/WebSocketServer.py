from SimpleWebSocketServer import SimpleWebSocketServer
from websocket.WebSocketHandler import WebSocketHandler
from dotenv import load_dotenv
from utils.printServer import printServer

class WebSocketServer:
    
    def __init__(self,ws_host,ws_port) -> None:
        self.ws_host = ws_host
        self.ws_port = ws_port

        load_dotenv()

    def start(self):
        printServer("Start websocket server")
        self.server = SimpleWebSocketServer(self.ws_host,self.ws_port, WebSocketHandler)
        self.server.serveforever()

    def stop(self):
        self.server.close()

    
