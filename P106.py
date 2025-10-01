#File Management Operations
import os
filename = "sample.txt"
with open(filename, "w") as f:
    f.write("Python File Ops")
print("File Created:", os.path.exists(filename))
with open(filename, "r") as f:
    print("Read:", f.read())
os.rename(filename, "sample_renamed.txt")
os.remove("sample_renamed.txt")
print("File Deleted")
