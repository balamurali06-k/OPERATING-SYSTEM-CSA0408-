def priority_scheduling():
    n = int(input("Enter number of processes: "))
    burst_time = []
    priority = []

    for i in range(n):
        bt = int(input(f"Enter burst time for P{i+1}: "))
        burst_time.append(bt)

    for i in range(n):
        pr = int(input(f"Enter priority for P{i+1} (smaller number = higher priority): "))
        priority.append(pr)

    # Store process numbers
    processes = list(range(1, n+1))

    # Sort processes by priority (ascending)
    for i in range(n-1):
        for j in range(i+1, n):
            if priority[i] > priority[j]:
                # Swap priority
                priority[i], priority[j] = priority[j], priority[i]
                # Swap burst time
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                # Swap process number
                processes[i], processes[j] = processes[j], processes[i]

    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Display results
    print("\nProcess  Burst Time  Priority  Waiting Time  Turnaround Time")
    for i in range(n):
        print(f"P{processes[i]}       {burst_time[i]}           {priority[i]}         {waiting_time[i]}             {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")

# Run the program
priority_scheduling()
