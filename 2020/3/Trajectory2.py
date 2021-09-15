# Advent of Code December 3, 2020 Part 2
#
# Toboggan Trajectory
# Calculate the number of trees (#) in a given slope
#
# Part 2 calulates number of trees for slopes:
#	Right 1, down 1
#	Right 3, down 1 (Part 1)
#	Right 5, down 1
#	Right 7, down 1
#	Right 1, down 2
# Then multiply the number of trees together to get the answer

def checkPath(array, slope):
	numTrees = 0
	arrSize = len(array)

	if(slope != .5):
		for i in range(arrSize):
			pos = (i * slope) % 31
			line = array[i]
		
			if(line[pos] == '#'):
				numTrees += 1

	# If slope is .5, we need to check every other line
	# String indices must be integers
	else:
		for i in range(arrSize):
			if(i % 2 == 0):
				pos = int(i/2) % 31
				line = array[i]

				if(line[pos] == '#'):
					numTrees += 1

	return numTrees


def main():
	# Initalize an empty list
	array = []

	# Store slopes in an array
	slopes = [1, 3, 5, 7, .5]

	# Read in file
	with open('input.txt') as f:
		for line in f:
			array.append(line.strip("\n"))

	result = 1

	for i in slopes:	
		# Check path for trees in given slope
		numTrees = checkPath(array, i)

		# Print result
		print(f'{numTrees} trees in slope {i}')

		# Multiply for result
		result *= numTrees

	# Print end result
	print(f'Multiplied together = {result}')


if __name__ == '__main__':
	main()