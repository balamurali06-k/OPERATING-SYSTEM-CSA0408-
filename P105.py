#UNIX I/O System Calls Simulation
import os
filename = "demo.txt"
fd = os.open(filename, os.O_CREAT|os.O_RDWR)
os.write(fd, b"Hello UNIX")
os.lseek(fd, 0, os.SEEK_SET)
data = os.read(fd, 20)
print("Data:", data.decode())
os.close(fd)
print("File Size:", os.stat(filename).st_size)
os.remove(filename)
