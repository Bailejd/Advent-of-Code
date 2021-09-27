# Day 4: Passport Processing

import re

def check_data(data_list):
    boolDict = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
    for i in range(len(data_list)):
        key = data_list[i][:3]
        value = data_list[i][4:]
        try:
            if(key == 'byr'):
                if(int(value) >= 1920 and int(value) <= 2002):
                    boolDict['byr'] = True
            if(key == 'iyr'):
                if(int(value) >= 2010 and int(value) <= 2020):
                    boolDict['iyr'] = True
            if(key == 'eyr'):
                if(int(value) >= 2020 and int(value) <= 2030):
                    boolDict['eyr'] = True
            if(key == 'hgt'):
                if(value[-2:] == 'cm'):
                    if(int(value[:-2]) >= 150 and int(value[:-2]) <= 193):
                        boolDict['hgt'] = True
                else:
                    if(int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
                        boolDict['hgt'] = True
            if(key == 'hcl'):
                if(re.match(r'^#[0-9a-f]{6}$', value)):
                    boolDict['hcl'] = True
            if(key == 'ecl'):
                if(value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    boolDict['ecl'] = True
            if(key == 'pid'):
                if(re.match(r'^[0-9]{9}$', value)):
                    boolDict['pid'] = True
        except:
            pass

    for key in boolDict:
        if(boolDict[key] == False):
            return False
    
    return True


def check(data_list):
    boolDict = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
    for i in range(len(data_list)):
        key = data_list[i][:3]
        if(key in boolDict):
            boolDict[key] = True
    for key in boolDict:
        if(boolDict[key] == False):
            return False
    
    return True


def part_one(data_list):
    num_valid = 0
    for i in range(len(data_list)):
        if(check(data_list[i])):
            num_valid += 1
    
    return num_valid



def part_two(data_list):
    num_valid = 0
    for i in range(len(data_list)):
        if(check_data(data_list[i])):
            num_valid += 1
    
    return num_valid


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.replace(' ', '\n').split('\n\n')
    data_list = [i.split('\n') for i in data_list]

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')
  
    
if __name__ == '__main__':
    main()