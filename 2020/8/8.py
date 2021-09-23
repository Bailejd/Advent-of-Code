# Day 8: Handheld Halting

def part_one(array):
    acc = 0
    index = 0

    while(array[index][2] != 2):
        if(array[index][0] == 'nop'):
            index += 1
        elif(array[index][0] == 'jmp'):
            inc = array[index][1]
            if(inc[0] == '+'):
                index += int(inc[1:])
            else:
                index -= int(inc[1:])
        elif(array[index][0] == 'acc'):
            inc = array[index][1]
            if(inc[0] == '+'):
                acc += int(inc[1:])
                index += 1
            else:
                acc -= int(inc[1:])
                index += 1
        array[index][2] += 1

    return acc


def part_two(array):
    acc = 0
    index = 0

    # Add end of file 
    array.append(['eof', '0', 0])

    for i in range(len(array)):
        # Swap a jmp or nop
        if(array[i][0] == 'jmp'):
            array[i][0] = 'nop'
        elif(array[i][0] == 'nop'):
            array[i][0] = 'jmp'

        while(array[index][2] != 2 and array[index] != 'eof'):
            if(array[index][0] == 'nop'):
                index += 1
            elif(array[index][0] == 'jmp'):
                inc = array[index][1]
                if(inc[0] == '+'):
                    index += int(inc[1:])
                else:
                    index -= int(inc[1:])
            elif(array[index][0] == 'acc'):
                inc = array[index][1]
                if(inc[0] == '+'):
                    acc += int(inc[1:])
                    index += 1
                else:
                    acc -= int(inc[1:])
                    index += 1
            array[index][2] += 1

            if(array[index][0] == 'eof'):
                return acc

        # Swap back
        if(array[i][0] == 'jmp'):
            array[i][0] = 'nop'
        elif(array[i][0] == 'nop'):
            array[i][0] = 'jmp'

        # Reset
        for j in range(len(array)-1):
            array[j][2] = 0
        index = 0
        acc = 0


def main():
    # Create an empty list
    array = []

    # Read in data from file
    with open('input.txt') as f:
        for line in f:
            text = line.split()
            text.append(0)
            array.append(text)

    # Part 1
    print(f'Part 1: {part_one(array)}')

    # Part 2
    print(f'Part 2: {part_two(array)}')

if __name__ == '__main__':
    main()
