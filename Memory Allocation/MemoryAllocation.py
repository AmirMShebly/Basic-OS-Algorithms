def worst_fit(memory_blocks, process_sizes):
    memory_allocation = [-1] * len(process_sizes)
    block_fragmentation = [0] * len(memory_blocks)

    for i in range(len(process_sizes)):
        worst_fit_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if worst_fit_index == -1 or memory_blocks[j] > memory_blocks[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            memory_allocation[i] = worst_fit_index
            block_fragmentation[worst_fit_index] = memory_blocks[worst_fit_index] - process_sizes[i]
            memory_blocks[worst_fit_index] = -1

    return memory_allocation, block_fragmentation


def best_fit(memory_blocks, process_sizes):
    memory_allocation = [-1] * len(process_sizes)
    block_fragmentation = [0] * len(memory_blocks)

    for i in range(len(process_sizes)):
        best_fit_index = -1
        min_fragmentation = float('inf')

        for j in range(len(memory_blocks)):
            if memory_blocks[j] != -1 and memory_blocks[j] >= process_sizes[i]:
                fragmentation = memory_blocks[j] - process_sizes[i]
                if fragmentation < min_fragmentation:
                    min_fragmentation = fragmentation
                    best_fit_index = j

        if best_fit_index != -1:
            memory_allocation[i] = best_fit_index
            block_fragmentation[best_fit_index] = min_fragmentation

            memory_blocks[best_fit_index] = -1

    return memory_allocation, block_fragmentation


def first_fit(memory_blocks, process_sizes):
    memory_allocation = [-1] * len(process_sizes)
    block_fragmentation = [0] * len(memory_blocks)

    for i in range(len(process_sizes)):
        allocated = False
        for j in range(len(memory_blocks)):
            if memory_blocks[j] != -1 and memory_blocks[j] >= process_sizes[i]:
                memory_allocation[i] = j
                block_fragmentation[j] = memory_blocks[j] - process_sizes[i]

                memory_blocks[j] = -1
                allocated = True
                break

        if not allocated:
            memory_allocation[i] = -1

    return memory_allocation, block_fragmentation


def main():

    option = input("Specify the memory allocation technique\n(w for worst fit, b for best fit and f for first fit):").lower()
    memory_blocks = []
    process_sizes = []
    num_blocks = int(input("Enter the number of blocks available in the memory: "))
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_blocks):
        memory_blocks.append(int(input(f"The size of the block {i+1} : ")))

    for i in range(num_processes):
        process_sizes.append(int(input(f"Enter the amount of memory required for the process {i + 1}: ")))

    if option == 'w':
        allocated_blocks, block_fragmentation = worst_fit(memory_blocks, process_sizes)

    if option == 'b':
        allocated_blocks, block_fragmentation = best_fit(memory_blocks, process_sizes)

    if option == 'f':
        allocated_blocks, block_fragmentation = first_fit(memory_blocks, process_sizes)

    print("Process #N\tProcess Size\tBlock #N\tFragmentation")
    total_fragmentation = 0
    for i in range(len(process_sizes)):
        print(f"{i + 1}\t\t\t\t\t{process_sizes[i]}\t\t", end="")
        if allocated_blocks[i] != -1:
            print(f"{allocated_blocks[i] + 1}\t\t\t\t{block_fragmentation[allocated_blocks[i]]}")
            total_fragmentation += block_fragmentation[allocated_blocks[i]]
        else:
            print("Not Allocated")

    print(f"\nTotal Fragmentation: {total_fragmentation}")


if __name__ == "__main__":
    main()

