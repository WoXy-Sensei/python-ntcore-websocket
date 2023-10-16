import threading
import signal
import sys
import os
from dashboard.Dashboard import Dashboard
from websocket.WebSocketServer import WebSocketServer
from dotenv import load_dotenv

def signal_handler(sig, frame):
    print("prgoram is closing")
    sys.exit(0)


if __name__ == "__main__":
    load_dotenv()

    threads = []
    
    dashboard = Dashboard(os.getenv("client_name"),os.getenv("host_name"),os.getenv("table_name"))

    threads.append(threading.Thread(target=WebSocketServer().start))
    threads.append(threading.Thread(target=Dashboard().start))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    
    signal.signal(signal.SIGINT, signal_handler)
    