#Best Fit Memory Management
blocks = [100, 500, 200, 300]
processes = [212, 417, 112, 426]
allocation = [-1]*len(processes)

for i, p in enumerate(processes):
    bfit = -1
    for j, b in enumerate(blocks):
        if b >= p and (bfit == -1 or blocks[j] < blocks[bfit]):
            bfit = j
    if bfit != -1:
        allocation[i] = bfit
        blocks[bfit] -= p

print("Process -> Block")
for i, b in enumerate(allocation):
    print(f"P{i} -> {b}")
