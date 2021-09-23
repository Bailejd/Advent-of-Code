# Day 5: Binary Boarding

import math

def get_seat(code):
    row = [0, 127]
    col = [0, 7]
    for char in code:
        if(char == 'F'):
            diff = row[1] - row[0]
            row[1] = row[1] - math.ceil(diff / 2)
        elif(char == 'B'):
            diff = row[1] - row[0]
            row[0] = row[0] + math.ceil(diff / 2)
        elif(char == 'L'):
            diff = col[1] - col[0]
            col[1] = col[1] - math.ceil(diff / 2)
        elif(char == 'R'):
            diff = col[1] - col[0]
            col[0] = col[0] + math.ceil(diff / 2)
        
    return([row[0], col[0]])


def get_seats(data_list):
    seats = []
    
    for code in data_list:
        seats.append(get_seat(code))
    
    return seats


def find_max_id(seats):
    """
    Find the maximum seat id from the input data.

    Parameters:
    seats (list): rows and cols for each seat

    Returns:
    int: The maximum Id
    """
    ids = []
    for seat in seats:
        # id = row * 8 + col
        ids.append(seat[0] * 8 + seat[1])

    return(max(ids))


def fill_seats(seats):
    plane = [[0]*8 for i in range(128)]

    for i in range(len(seats)):
        row = seats[i][0]
        col = seats[i][1]

        plane[row][col] = 1
    
    return plane


def find_seat(seats):
    """
    Find the your seat (the only open seat).

    However some seats are missing from the front and back of the plane
    """
    plane = fill_seats(seats)

    # Some seats in the front and back of the plane do not exist
    # Set to True to signal beginning of seats that exist
    exists = False

    for i in range(len(plane)):
        for j in range(len(plane[0])):
            if(exists and plane[i][j] == 0):
                your_id = i * 8 + j
                return your_id
            elif(not exists and plane[i][j] == 1):
                exists = True


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')

    seats = get_seats(data_list)

    # Part 1: Find maximum id
    print(f'Max ID: {find_max_id(seats)}')

    # Part 2: Find your seat id
    print(f'Your ID: {find_seat(seats)}')


if __name__ == '__main__':
    main()