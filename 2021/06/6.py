# Day 6: Lanternfish

def part_one(days, population):
    for i in range(80):
        new_fish = 0
        temp_population = [0] * 9
        for idx, pop in enumerate(population):
            if(days[idx] == 0):
                new_fish = pop
            else:
                temp_population[idx-1] = pop
        
        if(new_fish > 0):
            temp_population[8] = new_fish
            temp_population[6] += new_fish

        population = temp_population

    return sum(population)


def part_two(data_list):
    pass


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = [int(i) for i in data_list.split(',')]
    days = [0,1,2,3,4,5,6,7,8]
    population = [0] * 9
    
    for day in data_list:
        population[day] += 1

    # Part 1
    print(f'Part 1: {part_one(days, population)}')

    # Part 2
    print(f'Part 2: {part_two(days)}')


if __name__ == '__main__':
    main()
