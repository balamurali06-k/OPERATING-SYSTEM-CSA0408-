#LRU Paging
frames = 3
pages = [7, 0, 1, 2, 0, 3, 0, 4]
memory = []
recent = []
faults = 0

for p in pages:
    if p not in memory:
        if len(memory) < frames:
            memory.append(p)
        else:
            lru = recent.pop(0)
            idx = memory.index(lru)
            memory[idx] = p
        faults += 1
    if p in recent: recent.remove(p)
    recent.append(p)
    print("Memory:", memory)
print("Total Page Faults:", faults)