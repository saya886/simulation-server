import threading
import multiprocessing as mp
import socket
import time
import sys
import random
from decimal import *

def client_instance():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.18.111', 9998))
    device_id = b"server = socketserver.ThreadingTCPServer(('0.0.0.0', 9994), MyServer)"
    s.send(device_id)
    while True:
        rev_data = s.recv(1024)
        print(rev_data)
        # 发送数据:
        s.send(b'Hello')
        # 接收数据:
        time.sleep(float(Decimal(random.randint(50,5000))*Decimal(0.001)))
    s.close()

if __name__ == "__main__":
    if sys.argv[1] == "t":
        for i in range(100):
            t = threading.Thread(target=client_instance)
            t.start()

    if sys.argv[1] == "p":
        # mp = mp.get_context('spawn')
        for i in range(1000):
            p = mp.Process(target=client_instance)
            p.start()