import eel
import os
from networktable.NetworkTable import NetworkTable
from websocket.WebSocketServer import WebSocketServer
import multiprocessing
import sys

def start_eel_app():
    eel.init('web')
    eel.start('index.html', port=5000, close_callback=close)

def start_networktable():
    networktable = NetworkTable(os.getenv("client_name"), os.getenv("host_name"), os.getenv("table_name"))
    networktable.start()

def start_websocket():
    websocket = WebSocketServer()
    websocket.start()

def close(page, sockets):
    print(page,sockets)
    print("Program kapatılıyor...")
    sys.exit(0)

if __name__ == "__main__":
    eel_process = multiprocessing.Process(target=start_eel_app)
    networktable_process = multiprocessing.Process(target=start_networktable)
    websocket_process = multiprocessing.Process(target=start_websocket)

    eel_process.start()
    networktable_process.start()
    websocket_process.start()

    eel_process.join()  
    networktable_process.terminate() 
    websocket_process.terminate()
