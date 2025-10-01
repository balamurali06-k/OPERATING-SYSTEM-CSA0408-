#First Fit Memory Management
blocks = [100, 500, 200, 300]
processes = [212, 417, 112, 426]
allocation = [-1]*len(processes)

for i, p in enumerate(processes):
    for j, b in enumerate(blocks):
        if b >= p:
            allocation[i] = j
            blocks[j] -= p
            break

print("Process -> Block")
for i, b in enumerate(allocation):
    print(f"P{i} -> {b}")
