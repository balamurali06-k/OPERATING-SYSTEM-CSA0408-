#First Come First Served(FCFS)
def fcfs_scheduling():
    n = int(input("Enter number of processes: "))
    burst_time = []
    for i in range(n):
        bt = int(input(f"Enter burst time for P{i+1}: "))
        burst_time.append(bt)

    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Display results
    print("\nProcess  Burst Time  Waiting Time  Turnaround Time")
    for i in range(n):
        print(f"P{i+1}       {burst_time[i]}           {waiting_time[i]}             {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")

# Run the program
fcfs_scheduling()
