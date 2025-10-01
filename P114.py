#Sequential File Allocation
records = ["Rec1","Rec2","Rec3","Rec4"]
file = []
for r in records:
    file.append(r)
print("File Records Access:")
for i, r in enumerate(file):
    print(f"Reading {i+1}: {r}")

