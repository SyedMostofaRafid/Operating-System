def fcfs_scheduling_from_file(filename): 
    with open(filename, "r") as file:
        lines = file.readlines()
    # ইনপুট ফাইল থেকে প্রসেসের তথ্য লোড
    processes = []
    for line in lines:
        data = line.strip().split()  # স্পেস দিয়ে আলাদা করে প্রসেস আইডি এবং বার্স্ট টাইম
        processes.append((data[0], int(data[1])))
    n = len(processes)  # প্রসেসের সংখ্যা গণনার জন্য 
    waiting_time = [0] * n  # ওয়েটিং টাইম ইনিশিয়ালাইজ করা 
    turn_around_time = [0] * n  # টার্ন এরাউন্ড টাইম ইনিশিয়ালাইজ করা 
    for i in range(1, n):  # ওয়েটিং টাইম গণনা 
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]
    for i in range(n):  # টার্নএরাউন্ড টাইম গণনা 
        turn_around_time[i] = waiting_time[i] + processes[i][1]
    avg_waiting_time = sum(waiting_time) / n  # এভারেজ ওয়েটিং টাইম গণনা
    avg_turnaround_time = sum(turn_around_time) / n  # এভারেজ টার্ন এরাউন্ড টাইম গণনা 
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")  # রেজাল্ট প্রিন্ট 
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
# উদাহরণ
input_filename = "process.txt"  # ইনপুট ফাইলের নাম
fcfs_scheduling_from_file(input_filename)
