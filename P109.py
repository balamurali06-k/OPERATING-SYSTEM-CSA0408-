#Classical Process Synchronization (Producer-Consumer)
from threading import Thread, Lock
buffer = []
lock = Lock()
def producer():
    for i in range(3):
        lock.acquire()
        buffer.append(i)
        print("Produced:", i)
        lock.release()
def consumer():
    for i in range(3):
        lock.acquire()
        if buffer:
            item = buffer.pop(0)
            print("Consumed:", item)
        lock.release()
Thread(target=producer).start()
Thread(target=consumer).start()
