def sjf(filename): 
    with open(filename, "r") as file:
        lines = file.readlines()
    processes = []
    for line in lines:
        data = line.strip().split() 
        processes.append((data[0], int(data[1]))) 
    n = len(processes)  
    processes.sort(key=lambda x: x[1])  
    waiting_time = [0] * n 
    turn_around_time = [0] * n 
    completion_time = 0  
    for i in range(n): 
        waiting_time[i] = completion_time
        completion_time += processes[i][1]
        turn_around_time[i] = completion_time
    avg_waiting_time = sum(waiting_time) / n 
    avg_turnaround_time = sum(turn_around_time) / n  
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")  
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
input_filename = "processes.txt"  
sjf(input_filename)
