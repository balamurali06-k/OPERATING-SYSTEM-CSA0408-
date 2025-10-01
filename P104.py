#UNIX File Management Simulation
filename = "test.txt"
with open(filename, "w") as f:
    f.write("Hello Python\n")
with open(filename, "r") as f:
    content = f.read()
print("File Content:", content)
import os
print("File Exists:", os.path.exists(filename))
os.remove(filename)
print("File Removed")
