# Day 11: Seating System

def print_format(array):
	print()
	for i in range(len(array)):
		string = ''.join(array[i])
		print(string)
	print()


def checkAdjacent(array, xPos, yPos):
	numAdjacent = 0
	check = [[xPos-1, yPos-1], [xPos, yPos-1], [xPos+1, yPos-1], [xPos-1, yPos], [xPos+1, yPos], [xPos-1, yPos+1], [xPos, yPos+1], [xPos+1, yPos+1]]
	i = 0
	changed = True


	while(i <= len(check)-1):
		# print(f'len(check): {len(check)}, i:{i}')
		if(check[i][0] < 0 or check[i][0] >= len(array[0])):
			# print(f'Removed {check[i]}')
			check.pop(i)
		elif(check[i][1] < 0 or check[i][1] >= len(array)):
			# print(f'Removed {check[i]}')
			check.pop(i)
		else:
			i += 1
		
	for coord in check:
		position = array[coord[1]]
		position = position[coord[0]]
		# print(position)
		if(position == '#'):
			numAdjacent += 1
	
	return numAdjacent


def part1(array):
	changed = True
	numOccupied = 0
	
	while(changed == True):
		changed = False
		tempArray = []

		for yPos in range(len(array)):
			tempLine = []
			for xPos in range(len(array[0])):
				pos = array[yPos][xPos]
				numAdjacent = checkAdjacent(array, xPos, yPos)
				if(pos == 'L' and numAdjacent == 0):
					tempLine.append('#')
					changed = True
				elif(pos == '#' and numAdjacent >= 4):
					tempLine.append('L')
					changed = True
				else:
					tempLine.append(pos)

			tempArray.append(tempLine)

		array = tempArray
		# print_format(array)

	for i in range(len(array)):
		for j in range(len(array[0])):
			if(array[i][j] == '#'):
				numOccupied += 1

	return numOccupied


def main():
	# Create empty list
	array = []

	# Read in data from file
	with open('input.txt') as f:
		for line in f:
			chars = list(line.strip("\n"))
			array.append(chars)

	# print(f'dimensions of input: x:{len(array[0])}, y:{len(array)}')

	# Calculate and print results
	print(f'Part 1: {part1(array)}')


if __name__ == '__main__':
	main()