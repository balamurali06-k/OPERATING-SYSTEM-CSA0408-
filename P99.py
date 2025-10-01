import threading,time
lock=threading.Lock()
cnt=0
def worker(id):
    global cnt
    for _ in range(3):
        with lock:cnt+=1;print("T",id,"cnt",cnt)
        time.sleep(.1)
ths=[threading.Thread(target=worker,args=(i,)) for i in range(3)]
[t.start() for t in ths];[t.join() for t in ths]
