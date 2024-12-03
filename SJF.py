def sjf_scheduling(processes): # ফাংশানের নাম নির্ধারণ 
    n = len(processes) # প্রসেসের সংখ্যা গণনার জন্য 
    processes.sort(key=lambda x: x[1])  # বার্ষ্ট টাইম অনুযায়ী সর্ট করার জন্য 

    waiting_time = [0] * n # ও্যেটিং টাইম গণনার জন্য ০ ইনিশিয়ালাইজ করা 
    turn_around_time = [0] * n # টার্ন এরাউন্ড টাইম গণনার জন্য ০ ইনিশিয়ালাইজ করা 
    completion_time = 0 # সম্পূর্ণ সময় গণনার জন্য 

    for i in range(n): # Waiting and Turnaround Times গণনার জন্য 
        waiting_time[i] = completion_time
        completion_time += processes[i][1]
        turn_around_time[i] = completion_time

    avg_waiting_time = sum(waiting_time) / n # এভারেজ ওয়েটিং টাইম গণনার জন্য 
    avg_turnaround_time = sum(turn_around_time) / n # টার্ন এরাউন্ড টাইম গণনার জন্য 

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time") #রেজাল্ট প্রিন্টের জন্য 
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

#উদাহরণ  
processes_sjf = [("P1", 6), ("P2", 8), ("P3", 7), ("P4", 3)]  # (Process ID, Burst Time)
sjf_scheduling(processes_sjf)
