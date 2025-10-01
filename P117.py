#FCFS Disk Scheduling
requests = [98, 183, 41, 122, 14]
head = 50
total = 0
for r in requests:
    total += abs(head - r)
    head = r
print("Total Head Movement:", total)
