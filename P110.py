#Thread Concepts (create, join, exit)
from threading import Thread, current_thread
def task():
    print(f"Thread {current_thread().name} running")
t1 = Thread(target=task, name="T1")
t2 = Thread(target=task, name="T2")
t1.start()
t2.start()
t1.join()
t2.join()
print("All threads finished")
