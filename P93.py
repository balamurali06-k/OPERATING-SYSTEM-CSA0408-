def fit(blocks,ps,mode):
    bl=blocks[:];res=[]
    for p in ps:
        idx=-1
        if mode=="first": idx=next((i for i,b in enumerate(bl) if b>=p),-1)
        elif mode=="best": idx=min((i for i,b in enumerate(bl) if b>=p),key=lambda i:bl[i],default=-1)
        else: idx=max((i for i,b in enumerate(bl) if b>=p),key=lambda i:bl[i],default=-1)
        if idx!=-1:bl[idx]-=p;res.append((p,idx))
        else:res.append((p,None))
    print(mode,res)
blocks=[100,500,200,300,600];ps=[212,417,112,426]
for m in["first","best","worst"]:fit(blocks,ps,m)
