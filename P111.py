#FIFO Paging
frames = 3
pages = [7, 0, 1, 2, 0, 3, 0, 4]
memory = []
page_faults = 0

for p in pages:
    if p not in memory:
        if len(memory) < frames:
            memory.append(p)
        else:
            memory.pop(0)
            memory.append(p)
        page_faults += 1
    print("Memory:", memory)
print("Total Page Faults:", page_faults)
