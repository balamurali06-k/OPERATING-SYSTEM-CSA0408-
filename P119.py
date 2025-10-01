#C-SCAN Disk Scheduling
requests = [98, 183, 41, 122, 14]
head = 50
max_cyl = 199
requests.sort()
right = [r for r in requests if r >= head]
left = [r for r in requests if r < head]
sequence = right + [max_cyl, 0] + left
total = 0
pos = head
for r in sequence:
    total += abs(pos - r)
    pos = r
print("Head Sequence:", sequence, "Total Movement:", total)
