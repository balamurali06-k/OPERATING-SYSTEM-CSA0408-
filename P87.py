def simulate(ps):
    for p in ps:p['done']=0
    t=0;n=len(ps);c=0
    while c<n:
        r=[p for p in ps if p['arrival']<=t and not p['done']]
        if not r:t+=1;continue
        cur=min(r,key=lambda x:x['burst']);cur['start']=t;cur['finish']=t+cur['burst'];t+=cur['burst'];cur['done']=1;c+=1
    for p in ps:print(p['pid'],p['finish']-p['arrival'],p['start']-p['arrival'])
simulate([{'pid':1,'arrival':0,'burst':7},{'pid':2,'arrival':2,'burst':4}])
