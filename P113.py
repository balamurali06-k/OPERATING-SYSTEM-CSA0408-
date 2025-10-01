#Optimal Paging
frames = 3
pages = [7, 0, 1, 2, 0, 3, 0, 4]
memory = []
faults = 0

for i, p in enumerate(pages):
    if p not in memory:
        if len(memory) < frames:
            memory.append(p)
        else:
            future = [(memory[j], pages[i+1:].index(memory[j]) if memory[j] in pages[i+1:] else float('inf')) for j in range(len(memory))]
            idx = max(future, key=lambda x: x[1])[0]
            memory[memory.index(idx)] = p
        faults += 1
    print("Memory:", memory)
print("Total Page Faults:", faults)