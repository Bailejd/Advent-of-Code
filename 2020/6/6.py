# Day 6: Custom Customs

def part_one(data_list):
    numYes = 0
    
    # A list of current groups yes answers
    yes = []

    for i in range(len(data_list)):
        # If empty string, end of group
        if(data_list[i] == ''):
            numYes += len(yes)
            
            # Reset list for next group
            yes = []
        else:
            # Add characters to list if not already in list
            for char in data_list[i]:
                if(char not in yes):
                    yes.append(char)

    return numYes


def part_two(data_list):
	numYes = 0
	
	# A dictionary keeping track of answers
	answers = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}

	groupSize = 0

	for i in range(len(data_list)):
		# If empty string, end of group
		if(data_list[i] == ''):
			for key in answers:
				# If number answered yes is equal to group size increment numYes
				if(answers[key] == groupSize):
					numYes += 1

			# Reset dictionary and group size
			for key in answers:
				answers[key] = 0
			groupSize = 0

		else:
			# Increment each question answered yes
			for char in data_list[i]:
				answers[char] = answers[char] + 1

			# Increment the group size
			groupSize += 1

	return numYes


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')
  
    
if __name__ == '__main__':
    main()
