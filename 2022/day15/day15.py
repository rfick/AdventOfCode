import re

def manhattanDist(sensorX, sensorY, beaconX, beaconY):
	return abs(sensorX - beaconX) + abs(sensorY - beaconY)

def findPointsOnLineToSearch(sensorX, sensorY, dist, lineToSearch):
	yMovement = abs(sensorY - lineToSearch)

	if(yMovement <= dist):
		firstPointX = sensorX - (dist - yMovement)
		secondPointX = sensorX + (dist - yMovement)
	else:
		firstPointX = None
		secondPointX = None

	return firstPointX, secondPointX

# Using readlines()
file1 = open('day15input.txt', 'r')
Lines = file1.readlines()

lineToSearch = 2000000

xValuesCovered = {}
beaconXValuesOnLine = {}

for line in Lines:
	line = line.strip()

	sensorX, sensorY, beaconX, beaconY = map(int, re.findall('[+-]?\d+(?:\.\d+)?', line))

	dist = manhattanDist(sensorX, sensorY, beaconX, beaconY)
	firstPointX, secondPointX = findPointsOnLineToSearch(sensorX, sensorY, dist, lineToSearch)

	if(beaconY == lineToSearch):
		beaconXValuesOnLine[beaconX] = 1

	if(firstPointX != None and secondPointX != None):
		for i in range(firstPointX, secondPointX+1):
			xValuesCovered[i] = 1

answer = len(xValuesCovered)

for key in beaconXValuesOnLine:
	if(key in xValuesCovered):
		answer -= 1
		del xValuesCovered[key]

print(answer)