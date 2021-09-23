# Day 10: Adapter Array

def part_one(data_list):
    current = 0

    diff = {'1': 0, '2': 0, '3': 0}

    for i in range(len(data_list)):
        difference = data_list[i] - current
        if(difference == 1):
            diff['1'] += 1
        elif(difference == 2):
            diff['2'] += 1
        elif(difference == 3):
            diff['3'] += 1
        else:
            print("Error")
        current = data_list[i]

    # Device is always 3 higher
    diff['3'] += 1

    result = diff['1'] * diff['3']

    return result


def part_two(data_list):
    numPaths = []
    data_list.insert(0, 0)
    
    # Setup lists
    for i in range(len(data_list)):
        numPaths.append(0)

    # Set first item to 1 path
    numPaths[0] = 1

    # Loop through adapters
    for i in range(len(data_list)):
        # If adapter can reach another (+1, +2, +3)
        # Add numPaths to each adapter it can reach
        currentPlus1 = data_list[i] + 1
        currentPlus2 = data_list[i] + 2
        currentPlus3 = data_list[i] + 3

        if(currentPlus1 in data_list):
            numPaths[i+1] += numPaths[i]
        if(currentPlus2 in data_list):
            numPaths[data_list.index(currentPlus2)] += numPaths[i]
        if(currentPlus3 in data_list):
            numPaths[data_list.index(currentPlus3)] += numPaths[i]

    return numPaths[-1]


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')
    data_list = [int(i) for i in data_list]

    # Sort list
    data_list.sort()

    # Print results
    print(f'Part 1 result: {part_one(data_list)}')
    print(f'Part 2 result: {part_two(data_list)}')


if __name__ == '__main__':
    main()