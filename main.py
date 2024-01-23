import os
from networktable.NetworkTable import NetworkTable
from websocket.WebSocketServer import WebSocketServer
import threading
import sys
import signal

def start_networktable():
    networktable = NetworkTable(os.getenv("client_name"), os.getenv("host_name"), os.getenv("table_name"))
    networktable.start()

def start_websocket():
    websocket = WebSocketServer(os.getenv("ws_host"), os.getenv("ws_port"))
    websocket.start()

def signal_handler(sig, frame):
    print("Closing...")
    sys.exit(0)

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    networktable_process = threading.Thread(target=start_networktable)
    websocket_process = threading.Thread(target=start_websocket)

    networktable_process.start()
    websocket_process.start()

