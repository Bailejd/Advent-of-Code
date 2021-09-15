# Advent of Code December 3, 2020 Part 1
#
# Toboggan Trajectory
# Calculate the number of trees (#) in the given slope
#	Slope: right 3, down 1

def checkPath(array):
	numTrees = 0
	arrSize = len(array)

	for i in range(arrSize):
		pos = (i * 3) % 31
		line = array[i]

		if(line[pos] == '#'):
			numTrees += 1

	return numTrees


def main():
	# Initalize an empty list
	array = []

	# Read in file
	with open('input.txt') as f:
		for line in f:
			array.append(line.strip("\n"))

	# Check path for trees
	numTrees = checkPath(array)

	# Print results
	print(f'{numTrees} trees')


if __name__ == '__main__':
	main()