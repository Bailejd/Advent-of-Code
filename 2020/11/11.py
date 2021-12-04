# Day 11: Seating System
#
# A somewhat inefficient/slow solution using standard python lists

import sys

# Enable/Disable debug printing
# Not recomended for large inputs
DEBUG = False

def debug_print_format(array):
	for i in range(len(array)):
		for j in range(len(array[0])):
			print(array[i][j], end='')
		print()


def debug_print_found(array, x, y):
	print(f'found {array[y][x]} at {y} {x}')


def check_adjacent(array, xPos, yPos):
	numAdjacent = 0
	check = [[xPos-1, yPos-1], [xPos, yPos-1], [xPos+1, yPos-1], [xPos-1, yPos],
		[xPos+1, yPos], [xPos-1, yPos+1], [xPos, yPos+1], [xPos+1, yPos+1]]
	i = 0

	while(i <= len(check)-1):
		if(check[i][0] < 0 or check[i][0] >= len(array[0])):
			check.pop(i)
		elif(check[i][1] < 0 or check[i][1] >= len(array)):
			check.pop(i)
		else:
			i += 1
		
	for coord in check:
		position = array[coord[1]]
		position = position[coord[0]]
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
				numAdjacent = check_adjacent(array, xPos, yPos)
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

	for i in range(len(array)):
		for j in range(len(array[0])):
			if(array[i][j] == '#'):
				numOccupied += 1

	return numOccupied


# Part 2 version of check_adjacent
# Checks on vertical, horizontal, and diagonals
# Stops at first seat on each cardinal/ordinal direction
def check_lines(array, xPos, yPos):

	# Keep track of directions where a seat has been found
	# Once found stop checking that direction
	found_seat = [0,0,0,0,0,0,0,0]

	# Keep track of how many found seats are taken and direction
	# This could be replaced with an incrementing integer value since direction
	#	does not matter
	taken = [0,0,0,0,0,0,0,0]

	# Avoid checking out of bounds
	MAX_X = len(array[0])-1
	MAX_Y = len(array)-1

	n = 1
	end = False

	if(DEBUG):
		print(f'({yPos},{xPos})')
	
	while(not end):
		end = True

		# North
		if(yPos - n >= 0 and found_seat[0] == 0):
			end = False
			char = array[yPos-n][xPos]
			if(char == '#'):
				taken[0] = 1
				found_seat[0] = 1
				if(DEBUG):
					debug_print_found(array, xPos, yPos-n)
			elif(char == 'L'):
				found_seat[0] = 1

		# North East
		if(xPos + n <= MAX_X and yPos - n >= 0 and found_seat[1] == 0):
			end = False
			char = array[yPos-n][xPos+n]
			if(char == '#'):
				taken[1] = 1
				found_seat[1] = 1
				if(DEBUG):
					debug_print_found(array, xPos+n, yPos-n)
			elif(char == 'L'):
				found_seat[1] = 1

		# East
		if(xPos + n <= MAX_X and found_seat[2] == 0):
			end = False
			char = array[yPos][xPos+n]
			if(char == '#'):
				taken[2] = 1
				found_seat[2] = 1
				if(DEBUG):
					debug_print_found(array, xPos+n, yPos)
			elif(char == 'L'):
				found_seat[2] = 1

		# South East
		if(xPos + n <= MAX_X and yPos + n <= MAX_Y and found_seat[3] == 0):
			end = False
			char = array[yPos+n][xPos+n]
			if(char == '#'):
				taken[3] = 1
				found_seat[3] = 1
				if(DEBUG):
					debug_print_found(array, xPos+n, yPos+n)
			elif(char == 'L'):
				found_seat[3] = 1

		# South
		if(yPos + n <= MAX_Y and found_seat[4] == 0):
			end = False
			char = array[yPos+n][xPos]
			if(char == '#'):
				taken[4] = 1
				found_seat[4] = 1
				if(DEBUG):
					debug_print_found(array, xPos, yPos+n)
			elif(char == 'L'):
				found_seat[4] = 1

		# South West
		if(xPos - n >= 0 and yPos + n <= MAX_Y and found_seat[5] == 0):
			end = False
			char = array[yPos+n][xPos-n]
			if(char == '#'):
				taken[5] = 1
				found_seat[5] = 1
				if(DEBUG):
					debug_print_found(array, xPos-n, yPos+n)
			elif(char == 'L'):
				found_seat[5] = 1

		# West
		if(xPos - n >= 0 and found_seat[6] == 0):
			end = False
			char = array[yPos][xPos-n]
			if(char == '#'):
				taken[6] = 1
				found_seat[6] = 1
				if(DEBUG):
					debug_print_found(array, xPos, yPos-n)
			elif(char == 'L'):
				found_seat[6] = 1

		# North West
		if(xPos - n >= 0 and yPos - n >= 0 and found_seat[7] == 0):
			end = False
			char = array[yPos-n][xPos-n]
			if(char == '#'):
				taken[7] = 1
				found_seat[7] = 1
				if(DEBUG):
					debug_print_found(array, xPos-n, yPos-n)
			elif(char == 'L'):
				found_seat[7] = 1
		
		n += 1

	return sum(taken)



def part2(array):
	changed = True
	numOccupied = 0

	while(changed == True):
		changed = False
		tempArray = []

		for yPos in range(len(array)):
			tempLine = []
			for xPos in range(len(array[0])):
				pos = array[yPos][xPos]
				if(pos == '.'):
					tempLine.append(pos)
				else:
					numVisible = check_lines(array, xPos, yPos)
					if(pos == 'L' and numVisible == 0):
						tempLine.append('#')
						changed = True
					elif(pos == '#' and numVisible >= 5):
						tempLine.append('L')
						changed = True
					else:
						tempLine.append(pos)

			tempArray.append(tempLine)

		array = tempArray

		if(DEBUG):
			print('\n-----\n')
			debug_print_format(array)
			print()
			quit = input('Press enter to continue (q to quit): ')
			if(quit == 'q'):
				print('Exiting\n')
				sys.exit()
			print()

	for i in range(len(array)):
		for j in range(len(array[0])):
			if(array[i][j] == '#'):
				numOccupied += 1

	if(DEBUG):
		print('\n--- end ---\n')
		debug_print_format(array)
		print()

	return numOccupied


def main():
	# Create empty list
	array = []

	# Read in data from file
	with open('input.txt') as f:
		for line in f:
			chars = list(line.strip("\n"))
			array.append(chars)

	# Calculate and print results
	if(DEBUG):
		partNum = int(sys.argv[2])
		print(f'Debugging Part {partNum}')
		if(partNum == 1):
			# In this case there are no debug prints for part 1
			print(f'Part 1 debug: {part1(array)}')
		if(partNum == 2):
			print(f'Part 2 debug: {part2(array)}')
	else:
		print(f'Part 1: {part1(array)}')
		print(f'Part 2: {part2(array)}')


if __name__ == '__main__':
	if(len(sys.argv) == 3):
		if(sys.argv[1] == 'debug' or sys.argv[1] == 'd'):
			DEBUG = True

	main()