import os
from networktable.NetworkTable import NetworkTable
from websocket.WebSocketServer import WebSocketServer
import multiprocessing
import sys

def start_networktable():
    networktable = NetworkTable(os.getenv("client_name"), os.getenv("host_name"), os.getenv("table_name"))
    networktable.start()

def start_websocket():
    websocket = WebSocketServer()
    websocket.start()

if __name__ == "__main__":

    networktable_process = multiprocessing.Process(target=start_networktable)
    websocket_process = multiprocessing.Process(target=start_websocket)

    networktable_process.start()
    websocket_process.start()

