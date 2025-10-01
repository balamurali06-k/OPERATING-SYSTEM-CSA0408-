import struct,os
fmt="i20s"
def add(f,id,name):
    with open(f,"ab") as fp:fp.write(struct.pack(fmt,id,name.encode().ljust(20)))
def read(f,pos):
    with open(f,"rb") as fp:fp.seek(pos*struct.calcsize(fmt));id,n=struct.unpack(fmt,fp.read(struct.calcsize(fmt)));print(id,n.decode().strip())
f="emp.dat";[add(f,i,f"emp{i}") for i in range(1,4)]
read(f,1)
