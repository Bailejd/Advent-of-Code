# Day 6: Lanternfish

def calc_population(population, cycles):
    for i in range(cycles):
        new_fish = 0
        temp_population = [0] * 9
        for idx, pop in enumerate(population):
            if(idx == 0):
                new_fish = pop
            else:
                temp_population[idx-1] = pop
        
        if(new_fish > 0):
            temp_population[8] = new_fish
            temp_population[6] += new_fish

        population = temp_population

    return sum(population)


def part_one(population):
    return calc_population(population, cycles=80)


def part_two(population):
    return calc_population(population, cycles=256)


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = [int(i) for i in data_list.split(',')]
    population = [0] * 9
    
    for spawn_timer in data_list:
        population[spawn_timer] += 1

    # Part 1
    print(f'Part 1: {part_one(population)}')

    # Part 2
    print(f'Part 2: {part_two(population)}')


if __name__ == '__main__':
    main()
