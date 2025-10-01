#Two-Level Directory
class FS:
    def __init__(s):s.u={}
    def mkuser(s,u):s.u.setdefault(u,{})
    def mkfile(s,u,f,c=""):s.u[u][f]=c
    def list(s,u):return list(s.u.get(u,{}))
    def read(s,u,f):return s.u.get(u,{}).get(f)
fs=FS();fs.mkuser("a");fs.mkuser("b");fs.mkfile("a","x","ax");fs.mkfile("b","y","by")
print(fs.list("a"));print(fs.read("a","x"))

