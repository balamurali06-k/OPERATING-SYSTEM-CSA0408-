#Shared Memory IPC
from multiprocessing import Process,shared_memory;import time
def prod(n):sh=shared_memory.SharedMemory(name=n);sh.buf[0]=5;[sh.buf.__setitem__(i+1,i+1) or time.sleep(.1) for i in range(5)]
def cons(n):sh=shared_memory.SharedMemory(name=n);time.sleep(.2);print([sh.buf[i+1] for i in range(sh.buf[0])])
if __name__=="__main__":
    sh=shared_memory.SharedMemory(create=True,size=20)
    p=Process(target=prod,args=(sh.name,));c=Process(target=cons,args=(sh.name,))
    p.start();c.start();p.join();c.join();sh.close();sh.unlink()

