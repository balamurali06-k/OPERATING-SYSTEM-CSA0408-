#Simulate ls Command
import os
path = "."
files = os.listdir(path)
print("Files in Directory:")
for f in files:
    if os.path.isfile(os.path.join(path, f)):
        print(f)

