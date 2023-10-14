import threading
import signal
import sys
from dashboard import Dashboard
from websocket import WebSocketServer




def signal_handler(sig, frame):
    print("prgoram is closing")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    dashboard = Dashboard()
    websocket = WebSocketServer()
    t1 = threading.Thread(target=websocket.start)
    t1.start()
    t2 = threading.Thread(target=dashboard.start)
    t2.start()
  
    