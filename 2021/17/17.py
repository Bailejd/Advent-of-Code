# Day 17: Trick Shot
#
# Results
# Part 1: 4186
# Part 2: 2709

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Target():
    def __init__(self, right_x, left_x, upper_y, lower_y):
        self.right_x = int(right_x)
        self.left_x = int(left_x)
        self.upper_y = int(upper_y)
        self.lower_y = int(lower_y)

    def __str__(self):
        return f'({self.left_x},{self.upper_y}) ({self.right_x},{self.lower_y})'

    def point_inside_target(self, curr: Point) -> bool:
        return (self.left_x <= curr.x <= self.right_x) and (self.lower_y <= curr.y <= self.upper_y)


def check_trajectory(target: Target, velocity: Point) -> tuple[bool, list[Point]]:
    step = 0
    curr_position = Point(0, 0)
    path = [curr_position]
    hit_target = False

    while not hit_target:
        curr_velocity = calc_velocity(velocity, step)
        curr_position = Point(curr_position.x + curr_velocity.x, curr_position.y + curr_velocity.y)
        path.append(curr_position)

        if(curr_velocity.x == 0 and curr_position.x < target.left_x):
            break
        if(curr_position.x > target.right_x or curr_position.y < target.lower_y):
            break
        if(target.point_inside_target(curr_position)):
            hit_target = True
            break

        step += 1

    return hit_target, path


def calc_velocity(velocity: Point, step: int) -> Point:
    if(step < velocity.x):
        x = abs(velocity.x) - step
    else:
        x = 0

    y = velocity.y - step

    return Point(x, y)


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data = f.read()
    
    data = data[13:].replace(' ', '')
    data = data.split(',')
    data = [ele[2:].lstrip().split('..') for ele in data]

    target = Target(data[0][1], data[0][0], data[1][1], data[1][0])

    success = {}
    max_y = 0

    for x in range(1, target.right_x + 1):
        for y in range(target.lower_y, abs(target.lower_y)):
            velocity = Point(x,y)
            hit_target, path = check_trajectory(target, velocity)
            if(hit_target):
                temp_max = max(point.y for point in path)
                success[velocity] = temp_max

                if(temp_max > max_y):
                    max_y = temp_max
    
    print(f'Max hight: {max_y}')
    print(f'Num of successful trajectories: {len(success)}')


if __name__ == '__main__':
    main()
