# Day 1: Report Repair

import pathlib

DIR = pathlib.Path(__file__).parent.absolute()

def part_one(data_list):
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            if(i != j and data_list[i] + data_list[j] == 2020):
                return(data_list[i] * data_list[j])


def part_two(data_list):
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            for k in range(len(data_list)):
                if(i != j and j != k and data_list[i] + data_list[j] + data_list[k] == 2020):
                    return(data_list[i] * data_list[j] * data_list[k])


def main():
    # Read input file
    with open(DIR / "input.txt", "r") as f:
        data_list = f.read()

    data_list = data_list.split('\n')
    data_list = [int(i) for i in data_list]

    print(f'Part 1: {part_one(data_list)}')

    print(f'Part 2: {part_two(data_list)}')


if __name__ == '__main__':
    main()