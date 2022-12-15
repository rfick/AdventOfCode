import re
import numpy as np

def manhattanDist(sensorX, sensorY, beaconX, beaconY):
	return abs(sensorX - beaconX) + abs(sensorY - beaconY)

def findPointsOneAway(sensorX, sensorY, dist):
	firstPointX = sensorX + dist + 1
	firstPointY = sensorY

	secondPointX = sensorX
	secondPointY = sensorY + dist + 1

	thirdPointX = sensorX - dist - 1
	thirdPointY = sensorY

	fourthPointX = sensorX
	fourthPointY = sensorY - dist - 1

	return firstPointX, firstPointY, secondPointX, secondPointY, thirdPointX, thirdPointY, fourthPointX, fourthPointY

def lineFunc(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

# Using readlines()
file1 = open('day15input.txt', 'r')
Lines = file1.readlines()

sensorXs = []
sensorYs = []
beaconXs = []
beaconYs = []

for line in Lines:
	line = line.strip()

	sensorX, sensorY, beaconX, beaconY = map(int, re.findall('[+-]?\d+(?:\.\d+)?', line))

	sensorXs.append(sensorX)
	sensorYs.append(sensorY)
	beaconXs.append(beaconX)
	beaconYs.append(beaconY)

outsidePointEnds = []

maxVal = 4000000

for sensorX, sensorY, beaconX, beaconY in zip(sensorXs, sensorYs, beaconXs, beaconYs):
	dist = manhattanDist(sensorX, sensorY, beaconX, beaconY)
	firstPointX, firstPointY, secondPointX, secondPointY, thirdPointX, thirdPointY, fourthPointX, fourthPointY = findPointsOneAway(sensorX, sensorY, dist)

	outsidePointEnds.append((firstPointX, firstPointY, secondPointX, secondPointY))
	outsidePointEnds.append((secondPointX, secondPointY, thirdPointX, thirdPointY))
	outsidePointEnds.append((thirdPointX, thirdPointY, fourthPointX, fourthPointY))
	outsidePointEnds.append((fourthPointX, fourthPointY, firstPointX, firstPointY))

potentialPoints = []

for i in range(len(outsidePointEnds)):
	for j in range(len(outsidePointEnds)):
		if(i != j):
			line1 = lineFunc((outsidePointEnds[i][0], outsidePointEnds[i][1]), (outsidePointEnds[i][2], outsidePointEnds[i][3]))
			line2 = lineFunc((outsidePointEnds[j][0], outsidePointEnds[j][1]), (outsidePointEnds[j][2], outsidePointEnds[j][3]))
			intersectionPoint = intersection(line1, line2)
			if(intersectionPoint != False):
				potentialPoints.append((int(intersectionPoint[0]), int(intersectionPoint[1])))

for point in potentialPoints:
	if(point[0] < 0 or point[0] > maxVal or point[1] < 0 or point[1] > maxVal):
		continue

	pointIsValid = True
	for sensorX, sensorY, beaconX, beaconY in zip(sensorXs, sensorYs, beaconXs, beaconYs):
		distToBeacon = manhattanDist(sensorX, sensorY, beaconX, beaconY)

		distToPoint = manhattanDist(sensorX, sensorY, point[0], point[1])

		if(distToPoint <= distToBeacon):
			pointIsValid = False
	
	if(pointIsValid):
		xVal = point[0]
		yVal = point[1]
		break

print(xVal*4000000 + yVal)