#Multithreading
import threading,queue,time
def worker(q,i):
    while 1:
        try:t=q.get_nowait()
        except:break
        print(i,t);time.sleep(.1);q.task_done()
q=queue.Queue();[q.put(x) for x in range(5)]
ths=[threading.Thread(target=worker,args=(q,i)) for i in range(3)]
[t.start() for t in ths];[t.join() for t in ths]

