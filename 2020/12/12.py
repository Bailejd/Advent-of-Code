# Day 4: Passport Processing

def part_one(data_list):
    data_list = [(i[:1], int(i[1:])) for i in data_list]
    position = [0, 0]
    direction = 0

    for i in range(len(data_list)):
        if(data_list[i][0] == 'N'):
            position[1] += data_list[i][1]
        elif(data_list[i][0] == 'S'):
            position[1] -= data_list[i][1]
        elif(data_list[i][0] == 'E'):
            position[0] += data_list[i][1]
        elif(data_list[i][0] == 'W'):
            position[0] -= data_list[i][1]
        elif(data_list[i][0] == 'L'):
            direction += data_list[i][1]
            if(direction >= 360):
                direction = direction - 360
        elif(data_list[i][0] == 'R'):
            direction -= data_list[i][1]
            if(direction < 0):
                direction = 360 + direction
        elif(data_list[i][0] == 'F'):
            if(direction == 0):
                position[0] += data_list[i][1]
            elif(direction == 90):
                position[1] += data_list[i][1]
            elif(direction == 180):
                position[0] -= data_list[i][1]
            elif(direction == 270):
                position[1] -= data_list[i][1]

        # print(f'{data_list[i]}, {direction}')
        # print(f'NS:{position[1]}, EW:{position[0]}')
    
    return abs(position[0]) + abs(position[1])


def part_two(data_list):
    data_list = [(i[:1], int(i[1:])) for i in data_list]
    waypoint = [10, 1]
    position = [0, 0]
    direction = 0

    for i in range(len(data_list)):
        if(data_list[i][0] == 'N'):
            waypoint[1] += data_list[i][1]
        elif(data_list[i][0] == 'S'):
            waypoint[1] -= data_list[i][1]
        elif(data_list[i][0] == 'E'):
            waypoint[0] += data_list[i][1]
        elif(data_list[i][0] == 'W'):
            waypoint[0] -= data_list[i][1]
        elif(data_list[i][0] == 'L'):
            direction += data_list[i][1]
            if(data_list[i][1] == 90):
                waypoint = [-waypoint[1], waypoint[0]]
            elif(data_list[i][1] == 180):
                waypoint = [-waypoint[0], -waypoint[1]]
            elif(data_list[i][1] == 270):
                waypoint = [waypoint[1], -waypoint[0]]
        elif(data_list[i][0] == 'R'):
            direction -= data_list[i][1]
            if(data_list[i][1] == 90):
                waypoint = [waypoint[1], -waypoint[0]]
            elif(data_list[i][1] == 180):
                waypoint = [-waypoint[0], -waypoint[1]]
            elif(data_list[i][1] == 270):
                waypoint = [-waypoint[1], waypoint[0]]
        elif(data_list[i][0] == 'F'):
            position[0] += data_list[i][1] * waypoint[0]
            position[1] += data_list[i][1] * waypoint[1]

        # print(f'{data_list[i]}, {direction}')
        # print(f'NS:{position[1]}, EW:{position[0]}')
    
    return abs(position[0]) + abs(position[1])


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')
  
    
if __name__ == '__main__':
    main()