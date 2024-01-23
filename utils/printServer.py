import time

def printServer(text:str):
    """ Print text with date and time """
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{date}] - {text}")
    