import threading
import signal
import sys
import os
from networktable.NetworkTable import NeworkTable
from websocket.WebSocketServer import WebSocketServer
from dotenv import load_dotenv

def signal_handler(sig, frame):
    print("prgoram is closing")
    sys.exit(0)


if __name__ == "__main__":
    load_dotenv()

    threads = []

    networktable = NeworkTable(os.getenv("client_name"),os.getenv("host_name"),os.getenv("table_name"))
    websocket = WebSocketServer()

    threads.append(threading.Thread(target= websocket.start ))
    threads.append(threading.Thread(target= networktable.start ))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    
    signal.signal(signal.SIGINT, signal_handler)
    