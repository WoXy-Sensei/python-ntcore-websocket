import time

def printServer(text:str):
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{date}] - {text}")
    