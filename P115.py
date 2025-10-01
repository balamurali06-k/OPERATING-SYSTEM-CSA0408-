#Indexed File Allocation
records = ["Rec1","Rec2","Rec3","Rec4"]
index_block = list(range(len(records)))
print("Index Block:", index_block)
file = {}
for i, r in enumerate(records):
    file[i] = r
for i in index_block:
    print(f"Access Record {i}: {file[i]}")
