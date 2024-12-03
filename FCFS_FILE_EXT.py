def fcfs(filename): 
    with open(filename, "r") as file:
        lines = file.readlines()
    processes = []
    for line in lines:
        data = line.strip().split()  
        processes.append((data[0], int(data[1])))
    n = len(processes)  
    waiting_time = [0] * n  
    turn_around_time = [0] * n  
    for i in range(1, n): 
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]
    for i in range(n):  
        turn_around_time[i] = waiting_time[i] + processes[i][1]
    avg_waiting_time = sum(waiting_time) / n  
    avg_turnaround_time = sum(turn_around_time) / n  
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")  
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
input_filename = "process.txt" 
fcfs(input_filename)