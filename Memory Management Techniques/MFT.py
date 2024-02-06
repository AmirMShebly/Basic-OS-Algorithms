def mft_simulation():
    total_memory = int(input("Enter the total memory available (in Bytes): "))
    block_size = int(input("Enter the block size: "))
    num_processes = int(input("Enter the number of processes: "))
    memory_blocks = int(input("Enter the number of blocks available in memory: "))

    processes = []
    internal_fragmentation = 0
    external_fragmentation = total_memory - memory_blocks * block_size

    for i in range(num_processes):
        memory_required = int(input(f"Enter memory required for process {i + 1}: "))
        if memory_required <= block_size and memory_blocks > 0:
            memory_blocks -= 1
            processes.append((f"Process {i + 1}", memory_required, "YES", block_size - memory_required))
            internal_fragmentation += block_size - memory_required
        else:
            if not(i == num_processes - 1):
                processes.append((f"Process {i + 1}", memory_required, "NO", 0))

    print("\nOUTPUT")
    print(f"{'Process':<12}{'Memory Required':<20}{'ALLOCATED':<12}{'INTERNAL FRAGMENTATION':<30}")
    for process in processes:
        print(f"{process[0]:<12}{process[1]:<25}{process[2]:<12}{process[3]:<30}")

    print("Memory is full, remaining processes can not be accommodated")
    print(f"Total Internal Fragmentation: {internal_fragmentation} Bytes")
    print(f"Total External Fragmentation: {external_fragmentation} Bytes")


if __name__ == "__main__":
    mft_simulation()

