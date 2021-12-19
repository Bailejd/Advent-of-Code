# Day 14: Extended Polymerization
#
# Results
# Part 1: 2010
# Part 2: 2437698971143

from collections import defaultdict

def polymerize(polymer, rules, steps):
    polymer_pairs = defaultdict(int)

    # Initialize polymer_pairs
    for idx, char in enumerate(polymer):
        if(idx+1 >= len(polymer)):
            break
        if(polymer_pairs[polymer[idx:idx+2]]):
            polymer_pairs[polymer[idx:idx+2]] += 1
        else:
            polymer_pairs[polymer[idx:idx+2]] = 1
    
    # Step
    for step in range(steps):
        new_pairs = defaultdict(int)

        # Follow polymer pair rules
        for rule in rules:
            if(polymer_pairs[rule[0]]):
                new_pairs[rule[0][0] + rule[1]] += polymer_pairs[rule[0]]
                new_pairs[rule[1] + rule[0][1]] += polymer_pairs[rule[0]]
        
        # Update polymer_pairs
        polymer_pairs = new_pairs

    most_common_element = -1
    least_common_element = -1
    elements = defaultdict(int)

    # Calculate number of each element from each pair
    for key in polymer_pairs:
        left, right = key[0], key[1]
        elements[left] += round((polymer_pairs[key])/2)
        elements[right] += round((polymer_pairs[key])/2)

    # Find most and least common elements
    for key in elements:
        if(least_common_element == -1):
            most_common_element = elements[key]
            least_common_element = elements[key]
        if(elements[key] > most_common_element):
            most_common_element = elements[key]
        if(elements[key] < least_common_element):
            least_common_element = elements[key]
    
    return most_common_element - least_common_element


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        rules = f.read().split('\n')
    
    # Seperate polymer from rules
    polymer = rules[0]

    # format rules into list of tuples
    rules = rules[2:]
    rules = [tuple(rule.split(' -> ')) for rule in rules]

    print(polymer)

    # Part 1
    print(f'Part 1: {polymerize(polymer, rules, steps=10)}')

    # Part 2
    print(f'Part 2: {polymerize(polymer, rules, steps=40)}')


if __name__ == '__main__':
    main()
