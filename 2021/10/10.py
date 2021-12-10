# Day 10: Syntax Scoring
#
# Results
# Part 1: 215229
# Part 2: 1105996483

from statistics import median

def part_one(data_list):
    errors = []
    error_score = 0
    for line in data_list:
        stack = []
        for char in line:
            if(char == '(' or char == '[' or char == '{' or char == '<'):
                stack.append(char)
            else:
                last = stack[-1]
                if(last == '(' and char == ')'):
                    stack.pop()
                elif(last == '[' and char == ']'):
                    stack.pop()
                elif(last == '{' and char == '}'):
                    stack.pop()
                elif(last == '<' and char == '>'):
                    stack.pop()
                else:
                    errors.append(char)
                    break
    
    for error in errors:
        if(error == ')'):
            error_score += 3
        elif(error == ']'):
            error_score += 57
        elif(error == '}'):
            error_score += 1197
        else:
            error_score += 25137
    
    return error_score


def part_two(data_list):
    complete_score = []
    index = 0
    while(index < len(data_list)):
        stack = []
        score = 0
        line = data_list[index]
        corrupt = False
        for char in line:
            if(char == '(' or char == '[' or char == '{' or char == '<'):
                stack.append(char)
            else:
                last = stack[-1]
                if(last == '(' and char == ')'):
                    stack.pop()
                elif(last == '[' and char == ']'):
                    stack.pop()
                elif(last == '{' and char == '}'):
                    stack.pop()
                elif(last == '<' and char == '>'):
                    stack.pop()
                else:
                    # Remove corrupted lines
                    data_list.remove(line)
                    corrupt = True
                    index -= 1
                    break
        
        if(not corrupt):
            while(len(stack) != 0):
                if(stack[-1] == '('):
                    stack.pop()
                    score *= 5
                    score += 1
                elif(stack[-1] == '['):
                    stack.pop()
                    score *= 5
                    score += 2
                elif(stack[-1] == '{'):
                    stack.pop()
                    score *= 5
                    score += 3
                else:
                    stack.pop()
                    score *= 5
                    score += 4
        
            complete_score.append(score)
        
        complete_score.sort()
        index += 1
    
    return int(median(complete_score))


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read().split('\n')

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')


if __name__ == '__main__':
    main()
