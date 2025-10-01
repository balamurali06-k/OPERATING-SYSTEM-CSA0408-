#SCAN Disk Scheduling
requests = [98, 183, 41, 122, 14]
head = 50
requests.sort()
left = [r for r in requests if r < head][::-1]
right = [r for r in requests if r >= head]
sequence = right + left
total = 0
pos = head
for r in sequence:
    total += abs(pos - r)
    pos = r
print("Head Sequence:", sequence, "Total Movement:", total)

