# Day 9: Encoding Error

def part_one(data_list):
    last_25 = []

    # Load first 25 numbers
    for i in range(25):
        last_25.append(data_list[i])

    # Find first invalid
    curr_pos = 25
    for i in range(len(data_list)):
        invalid = True
        for j in range(len(last_25)):
            for k in range(len(last_25)):
                if(last_25[j] == last_25[k] or j > k):
                    continue
                elif(last_25[j] + last_25[k] == data_list[curr_pos]):
                    last_25[curr_pos % 25] = data_list[curr_pos]
                    curr_pos += 1
                    invalid = False
                elif(last_25[j] + last_25[k] != data_list[curr_pos]):
                    invalid_num = data_list[curr_pos]
        if(invalid == True):
            return invalid_num


def part_two(data_list, first_invalid):
    contiguous_nums = []
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            if(i >= j):
                continue
            else:
                contiguous_nums = data_list[i:j]
                if(sum(contiguous_nums) == first_invalid):
                    return (min(contiguous_nums) + max(contiguous_nums))



def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')
    data_list = [int(i) for i in data_list]

    first_invalid = part_one(data_list)

    # Part 1
    print(f'Part 1: {first_invalid}')

    # Part 2
    print(f'Part 2: {part_two(data_list, first_invalid)}')
  
    
if __name__ == '__main__':
    main()