def mvt_simulation():
    total_memory = int(input("Enter the total memory available (in Bytes): "))
    free_memory = total_memory
    allocated_memory = []

    i = 0
    memory_allocations = []
    while True:
        i += 1
        memory_required = int(input(f"Enter the memory required for the Process {i} (in Bytes): "))

        if memory_required <= free_memory:
            allocated_memory.append(memory_required)
            free_memory -= memory_required
            print(f"Memory is allocated for the Process {i}")
            memory_allocations.append(memory_required)
            flag = input("Do you want to continue?(y/n)")
            flag = flag.lower()
            if flag == 'y':
                pass
            elif flag == 'n':
                break
            else:
                print('Wrong input')
                break
        else:
            print("Memory is full")
            print("PROCESS MEMORY ALLOCATED")
            for i in range(len(memory_allocations)):
                print(f"{i+1} \t {memory_allocations[i]}")
            break

    external_fragmentation = free_memory
    total_allocated_memory = sum(allocated_memory)

    print(f"Total Memory Allocated is {total_allocated_memory} and Total External Fragmentation is {external_fragmentation}")


if __name__ == "__main__":
    mvt_simulation()


