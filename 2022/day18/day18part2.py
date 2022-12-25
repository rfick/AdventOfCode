import re
import math

class ConnectedComponentInfo:
	componentIsInterior = True
	numAdjacentCubes = 0

def BFSSearch(currPosition, cubePositions, visited, info, minx, maxx, miny, maxy, minz, maxz):
	visited.append(currPosition)

	queue = []
	queue.append(currPosition)

	while(len(queue) > 0):
		thisPosition = queue.pop(0)

		if(thisPosition[0]-1 < minx):
			info.componentIsInterior = False
		elif((thisPosition[0]-1, thisPosition[1], thisPosition[2]) in cubePositions):
			info.numAdjacentCubes = info.numAdjacentCubes + 1
		elif((thisPosition[0]-1, thisPosition[1], thisPosition[2]) not in visited):
			visited.append((thisPosition[0]-1, thisPosition[1], thisPosition[2]))
			queue.append((thisPosition[0]-1, thisPosition[1], thisPosition[2]))
		
		if(thisPosition[0]+1 > maxx):
			info.componentIsInterior = False
		elif((thisPosition[0]+1, thisPosition[1], thisPosition[2]) in cubePositions):
			info.numAdjacentCubes = info.numAdjacentCubes + 1
		elif((thisPosition[0]+1, thisPosition[1], thisPosition[2]) not in visited):
			visited.append((thisPosition[0]+1, thisPosition[1], thisPosition[2]))
			queue.append((thisPosition[0]+1, thisPosition[1], thisPosition[2]))

		if(thisPosition[1]-1 < miny):
			info.componentIsInterior = False
		elif((thisPosition[0], thisPosition[1]-1, thisPosition[2]) in cubePositions):
			info.numAdjacentCubes = info.numAdjacentCubes + 1
		elif((thisPosition[0], thisPosition[1]-1, thisPosition[2]) not in visited):
			visited.append((thisPosition[0], thisPosition[1]-1, thisPosition[2]))
			queue.append((thisPosition[0], thisPosition[1]-1, thisPosition[2]))

		if(thisPosition[1]+1 > maxy):
			info.componentIsInterior = False
		elif((thisPosition[0], thisPosition[1]+1, thisPosition[2]) in cubePositions):
			info.numAdjacentCubes = info.numAdjacentCubes + 1
		elif((thisPosition[0], thisPosition[1]+1, thisPosition[2]) not in visited):
			visited.append((thisPosition[0], thisPosition[1]+1, thisPosition[2]))
			queue.append((thisPosition[0], thisPosition[1]+1, thisPosition[2]))

		if(thisPosition[2]-1 < minz):
			info.componentIsInterior = False
		elif((thisPosition[0], thisPosition[1], thisPosition[2]-1) in cubePositions):
			info.numAdjacentCubes = info.numAdjacentCubes + 1
		elif((thisPosition[0], thisPosition[1], thisPosition[2]-1) not in visited):
			visited.append((thisPosition[0], thisPosition[1], thisPosition[2]-1))
			queue.append((thisPosition[0], thisPosition[1], thisPosition[2]-1))

		if(thisPosition[2]+1 > maxz):
			info.componentIsInterior = False
		elif((thisPosition[0], thisPosition[1], thisPosition[2]+1) in cubePositions):
			info.numAdjacentCubes = info.numAdjacentCubes + 1
		elif((thisPosition[0], thisPosition[1], thisPosition[2]+1) not in visited):
			visited.append((thisPosition[0], thisPosition[1], thisPosition[2]+1))
			queue.append((thisPosition[0], thisPosition[1], thisPosition[2]+1))

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

allPositions = []

for x in range(minx, maxx+1):
	for y in range(miny, maxy+1):
		for z in range(minz, maxz+1):
			allPositions.append((x, y, z))

for key in positions.keys():
	allPositions.remove(key)

while(len(allPositions) > 0):
	info = ConnectedComponentInfo()
	visited = []
	BFSSearch(allPositions[0], positions, visited, info, minx, maxx, miny, maxy, minz, maxz)

	if(info.componentIsInterior == True):
		surfaceArea -= info.numAdjacentCubes

	for visitedNode in visited:
		if(visitedNode in allPositions):
			allPositions.remove(visitedNode)

print(surfaceArea)