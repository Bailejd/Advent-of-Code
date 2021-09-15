# Day 5

import math

# Globals
rows = 128
columns = 8

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
    pass


def find_seat(seats):
    """
    Find the your seat (the only open seat).

    However some seats are missing from the front and back of the plane
    """
    pass


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')

    seats = get_seats(data_list)

    # Part 1: Find maximum id
    print(f'Max ID: {find_max_id(seats)}')

    # Part 2: Find your seat
    print(f'Your seat: {find_seat(seats)}')




if __name__ == '__main__':
    main()