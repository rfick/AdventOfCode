import re

# Using readlines()
file1 = open('day4input.txt', 'r')
Lines = file1.readlines()

numContainedPairs = 0

counter = 0

for line in Lines:
	line = line.strip()

	firstMin, firstMax, secondMin, secondMax = map(int, re.findall('\d+', line))

	# First pair is fully contained or second pair is fully contained
	if((firstMin <= secondMin and firstMax >= secondMax) or (secondMin <= firstMin and secondMax >= firstMax)):
		numContainedPairs += 1

print(numContainedPairs)