# Day 2: Password Philosophy

def part_one(array):
	numValid = 0
	for i in array:
		count = 0
		splitSpaces = i.split()
		min = int(splitSpaces[0].split("-")[0])
		max = int(splitSpaces[0].split("-")[1])
		letter = splitSpaces[1].split(":")[0]
		password = splitSpaces[2]

		for char in password:
			if(char == letter):
				count += 1

		if(count >= min and count <= max):
			numValid += 1

	return numValid


def part_two(array):
	numValid = 0
	for i in array:
		# Keep track of booleans for both positions
		positions = [False, False]

		splitSpaces = i.split()
		pos1 = int(splitSpaces[0].split("-")[0])
		pos2 = int(splitSpaces[0].split("-")[1])
		letter = splitSpaces[1].split(":")[0]
		password = splitSpaces[2]

		# Check positions
		if(password[pos1 - 1] == letter):
			positions[0] = True
		if(password[pos2 - 1] == letter):
			positions[1] = True

		# Check if only one position matched
		if((positions[0] and not positions[1]) or (not positions[0] and positions[1])):
			numValid += 1	

	return numValid

def main():
	# Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()

    data_list = data_list.split('\n')

    print(f'Part 1: {part_one(data_list)}')

    print(f'Part 2: {part_two(data_list)}')


if __name__ == '__main__':
	main()