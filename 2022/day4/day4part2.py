import re

# Using readlines()
file1 = open('day4input.txt', 'r')
Lines = file1.readlines()

numOverlappingPairs = 0

counter = 0

for line in Lines:
	line = line.strip()

	firstMin, firstMax, secondMin, secondMax = map(int, re.findall('\d+', line))

	# First pair is fully contained or second pair is fully contained
	if((firstMin >= secondMin and firstMin <= secondMax) or (firstMax >= secondMin and firstMax <= secondMax) or \
	   (secondMin >= firstMin and secondMin <= firstMax) or (secondMax >= firstMin and secondMax <= firstMax)):
		numOverlappingPairs += 1

print(numOverlappingPairs)