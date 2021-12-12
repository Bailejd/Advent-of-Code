# Day 11: Dumbo Octopus
#
# Results
# Part 1: 1686
# Part 2: 360

# To be more efficient Part 1 and Part 2 can be calculated at the same time

import numpy as np

def flash(flashed, energy, x, y):
    # Do not flash again if already flashed this step
    if(flashed[y][x] == 1):
        return
    else:
        flashed[y][x] = 1

        # Calculate possible adjacent positions
        adj_pos = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]

        # Check if position is inside bounds
        for pos in adj_pos:
            if(pos[0] >= 0 and pos[0] < energy.shape[1]):
                if(pos[1] >= 0 and pos[1] < energy.shape[0]):
                    # Increment adjacent energies
                    energy[pos[1]][pos[0]] += 1

                    # Flash if adjacent energy is greater than 9
                    if(energy[pos[1]][pos[0]] >= 10):
                        flash(flashed, energy, pos[0], pos[1])


def part_one(energy):
    total_flashes = 0

    # Steps
    for i in range(100):
        flashed = np.zeros(energy.shape, dtype=np.int32)

        # Increase each energy by 1
        energy = energy + 1

        # Check each position
        for y, x in np.ndindex(energy.shape):
            # Flash if energy more than 10
            if(energy[y][x] >= 10):
                flash(flashed, energy, x, y)
        
        # Reset energy to 0 after flashing
        reset_pos = np.where(flashed==1)
        for val in zip(reset_pos[0], reset_pos[1]):
            energy[val[0]][val[1]] = 0
        
        # Increment total flashes
        total_flashes += flashed.sum()
    
    return(total_flashes)


def part_two(energy):
    all_flash = False
    step = 0

    while(not all_flash):
        flashed = np.zeros(energy.shape, dtype=np.int32)

        # Increase each energy by 1
        energy = energy + 1

        # Check each position
        for y, x in np.ndindex(energy.shape):
            # Flash if energy more than 10
            if(energy[y][x] >= 10):
                flash(flashed, energy, x, y)
        
        # Reset energy to 0 after flashing
        reset_pos = np.where(flashed==1)
        for val in zip(reset_pos[0], reset_pos[1]):
            energy[val[0]][val[1]] = 0
        
        step += 1
        
        # Increment total flashes
        if(flashed.sum() == (energy.shape[0] * energy.shape[1])):
            return step


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = [[int(i) for i in line] for line in f.read().split('\n')]

    energy = np.array(data_list)

    # Part 1
    print(f'Part 1: {part_one(energy)}')

    # Part 2
    print(f'Part 2: {part_two(energy)}')


if __name__ == '__main__':
    main()
