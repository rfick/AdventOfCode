import re
import math

def findAdjacentPositions(position):
	adjacents = []
	adjacents.append((position[0]-1, position[1], position[2]))
	adjacents.append((position[0]+1, position[1], position[2]))
	adjacents.append((position[0], position[1]-1, position[2]))
	adjacents.append((position[0], position[1]+1, position[2]))
	adjacents.append((position[0], position[1], position[2]-1))
	adjacents.append((position[0], position[1], position[2]+1))
	return adjacents

# Using readlines()
file1 = open('day18input.txt', 'r')
Lines = file1.readlines()

positions = {}

minx = math.inf
maxx = -math.inf
miny = math.inf
maxy = -math.inf
minz = math.inf
maxz = -math.inf

for line in Lines:
	line = line.strip()

	numbers = re.findall('[0-9]+', line)

	numbers[0] = int(numbers[0])
	numbers[1] = int(numbers[1])
	numbers[2] = int(numbers[2])

	positions[(numbers[0], numbers[1], numbers[2])] = 1

	if(numbers[0] < minx):
		minx = numbers[0]
	if(numbers[0] > maxx):
		maxx = numbers[0]
	if(numbers[1] < miny):
		miny = numbers[1]
	if(numbers[1] > maxy):
		maxy = numbers[1]
	if(numbers[2] < minz):
		minz = numbers[2]
	if(numbers[2] > maxz):
		maxz = numbers[2]

surfaceArea = 0

for position in positions:
	adjacents = findAdjacentPositions(position)

	coveredSides = 0

	for adjacent in adjacents:
		if(adjacent in positions):
			coveredSides += 1

	surfaceArea += (6 - coveredSides)

print(surfaceArea)