#File Access Permission Simulation
users = {"owner":"rw","group":"r","others":"r"}
file = "example.txt"
for u, perm in users.items():
    print(f"User: {u}, Permission: {perm}")
print("Owner can read/write, group can read, others can read only")
