#Simulate grep Command
pattern = "hello"
filename = "file.txt"
with open(filename, "w") as f:
    f.write("hello world\nhi there\nhello python")
with open(filename, "r") as f:
    for line in f:
        if pattern in line:
            print(line.strip())
