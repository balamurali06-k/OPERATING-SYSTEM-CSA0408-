def banker(alloc,maxm,avail):
    n,m=len(alloc),len(avail)
    need=[[maxm[i][j]-alloc[i][j] for j in range(m)]for i in range(n)]
    f=[0]*n;ans=[]
    while len(ans)<n:
        safe=False
        for i in range(n):
            if not f[i] and all(need[i][j]<=avail[j] for j in range(m)):
                for j in range(m):avail[j]+=alloc[i][j]
                ans.append(i);f[i]=1;safe=True
        if not safe:break
    print("Safe seq:" if len(ans)==n else "Unsafe",ans)
banker([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]],[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]],[3,3,2])
