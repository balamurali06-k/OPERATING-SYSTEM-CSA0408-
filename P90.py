from multiprocessing import Process,Queue;import time
def prod(q):[q.put(f"msg{i}") or print("P",i) or time.sleep(.1) for i in range(5)];q.put("END")
def cons(q): 
    while 1: m=q.get();print("C",m); 
    if m=="END":break
if __name__=="__main__":
    q=Queue();p=Process(target=prod,args=(q,));c=Process(target=cons,args=(q,))
    p.start();c.start();p.join();c.join()
