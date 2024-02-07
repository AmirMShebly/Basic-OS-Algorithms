
class Process:
    def __init__(self, number, process_time, priority):
        self.number = number
        self.process_time = process_time
        self.priority = priority
        self.wait_time = 0
        self.turn_around_time = 0


number_of_processes = int(input("Enter the amount of processes: "))

processes = []

for i in range(1, number_of_processes + 1):
    print(f"Process {i} ")
    process_time = float(input("Duration: "))
    priority = int(input("Priority: "))
    processes.append(Process(i, process_time, priority))

processes.sort(key=lambda x: x.priority)

exit_time = 0

for process in processes:
    exit_time += process.process_time
    process.wait_time = exit_time - process.process_time
    process.turn_around_time = exit_time

average_waiting_time = sum(process.wait_time for process in processes) / number_of_processes
average_turn_around_time = sum(process.turn_around_time for process in processes) / number_of_processes

print("-----------------------------------------------------------------------------")
print("| Process   | Waiting Time | Process Time | Turn Around Time                 |")
print("-----------------------------------------------------------------------------")
for process in processes:
    print(f"| process {process.number:<3} | {process.wait_time:<10} | {process.process_time:<10} | {process.turn_around_time:<34}|")
print("-----------------------------------------------------------------------------")

print("Average Waiting time:", average_waiting_time)
print("Average Turn Around time:", average_turn_around_time)
