#Reader-Writer Problem with Semaphores
import threading,time
wsem=threading.Semaphore(1);rsem=threading.Semaphore(1);rc=0
def reader(i):
    global rc
    rsem.acquire();rc+=1
    if rc==1:wsem.acquire()
    rsem.release();print("Reader",i,"reading");time.sleep(.1)
    rsem.acquire();rc-=1
    if rc==0:wsem.release()
    rsem.release()
def writer(i):wsem.acquire();print("Writer",i,"writing");time.sleep(.2);wsem.release()
ths=[threading.Thread(target=reader,args=(i,)) for i in range(3)]+[threading.Thread(target=writer,args=(1,))]
[t.start() for t in ths];[t.join() for t in ths]

