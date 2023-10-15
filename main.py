import threading
import signal
import sys
from dashboard.Dashboard import Dashboard
from websocket.WebSocketServer import WebSocketServer

def signal_handler(sig, frame):
    print("prgoram is closing")
    sys.exit(0)


if __name__ == "__main__":
    threads = []

    threads.append(threading.Thread(target=WebSocketServer().start))
    threads.append(threading.Thread(target=Dashboard().start))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    
    signal.signal(signal.SIGINT, signal_handler)
    