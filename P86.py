#Preemptive Priority Scheduling (CPU scheduling simulator — lower number = higher priority)
import heapq
def simulate(ps):
    for p in ps: p['rem']=p['burst'];p['start']=-1
    t=i=0;h=[];g=[]
    while i<len(ps) or h:
        if not h and i<len(ps):t=max(t,ps[i]['arrival'])
        while i<len(ps) and ps[i]['arrival']<=t:heapq.heappush(h,(ps[i]['priority'],ps[i]));i+=1
        pr,cur=heapq.heappop(h);g.append((t,cur['pid']))
        if cur['start']==-1:cur['start']=t
        cur['rem']-=1;t+=1
        if cur['rem']>0:heapq.heappush(h,(cur['priority'],cur))
        else:cur['finish']=t
    for p in ps:print(p['pid'],p['finish']-p['arrival'],p['finish']-p['arrival']-p['burst'])
simulate([{'pid':1,'arrival':0,'burst':7,'priority':2},{'pid':2,'arrival':2,'burst':4,'priority':1}])

