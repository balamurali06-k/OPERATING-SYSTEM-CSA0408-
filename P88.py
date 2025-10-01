from collections import deque
def rr(ps,q):
    for p in ps:p['rem']=p['burst'];p['start']=-1
    t=0;dq=deque(ps)
    while dq:
        cur=dq.popleft()
        if cur['start']==-1:cur['start']=max(t,cur['arrival']);t=cur['start']
        run=min(q,cur['rem']);t+=run;cur['rem']-=run
        if cur['rem']>0:dq.append(cur)
        else:cur['finish']=t
    for p in ps:print(p['pid'],p['finish']-p['arrival'],p['finish']-p['arrival']-p['burst'])
rr([{'pid':1,'arrival':0,'burst':5},{'pid':2,'arrival':1,'burst':4}],2)
