class Dir:
    def __init__(s):s.f={}
    def create(s,n,c=""):s.f.setdefault(n,c)
    def delete(s,n):s.f.pop(n,None)
    def list(s):return list(s.f)
    def read(s,n):return s.f.get(n)
d=Dir();d.create("f1","hi");d.create("f2","bye")
print(d.list());print(d.read("f1"));d.delete("f2");print(d.list())
