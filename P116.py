#Linked File Allocation
records = ["Rec1","Rec2","Rec3","Rec4"]
file = {}
for i in range(len(records)-1):
    file[i] = (records[i], i+1)
file[len(records)-1] = (records[-1], None)
ptr = 0
while ptr is not None:
    data, ptr = file[ptr]
    print("Accessed:", data)
