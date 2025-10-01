import threading,time,random
def phil(i,l,r):
    for _ in range(2):
        time.sleep(random.random()/3)
        a,b=(l,r) if id(l)<id(r) else (r,l)
        with a: 
            with b:print("P",i,"eating");time.sleep(.1)
fs=[threading.Lock() for _ in range(5)]
ths=[threading.Thread(target=phil,args=(i,fs[i],fs[(i+1)%5])) for i in range(5)]
[t.start() for t in ths];[t.join() for t in ths]
