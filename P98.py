#Producer-Consumer with Semaphores
import threading,queue,time
q=queue.Queue(3);empty=threading.Semaphore(3);full=threading.Semaphore(0)
def prod():[empty.acquire() or q.put(i) or print("P",i) or full.release() or time.sleep(.1) for i in range(5)]
def cons():[full.acquire() or print("C",q.get()) or empty.release() or time.sleep(.2) for _ in range(5)]
t1=threading.Thread(target=prod);t2=threading.Thread(target=cons);t1.start();t2.start();t1.join();t2.join()

