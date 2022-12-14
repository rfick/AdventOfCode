def moveSandDown(bigWindow, sandLoc):
	if(bigWindow[sandLoc[0], sandLoc[1]+1] == 0):
		sandLoc = (sandLoc[0], sandLoc[1]+1)
	elif(bigWindow[sandLoc[0]-1, sandLoc[1]+1] == 0):
		sandLoc = (sandLoc[0]-1, sandLoc[1]+1)
	elif(bigWindow[sandLoc[0]+1, sandLoc[1]+1] == 0):
		sandLoc = (sandLoc[0]+1, sandLoc[1]+1)
	
	return sandLoc

def dropSand(bigWindow):
	sandFellThroughTheWorld = False
	numberOfRestingSand = 0
	while(sandFellThroughTheWorld == False):
		sandLoc = (500, 0)
		while(True):
			priorSandLoc = sandLoc
			sandLoc = moveSandDown(bigWindow, priorSandLoc)
			if(priorSandLoc == sandLoc):
				bigWindow[sandLoc[0], sandLoc[1]] = 1
				numberOfRestingSand += 1
				break
			elif(sandLoc[1]+1 == bigWindow.shape[1]):
				sandFellThroughTheWorld = True
				break
	return numberOfRestingSand

import numpy as np

# Using readlines()
file1 = open('day14input.txt', 'r')
Lines = file1.readlines()

bigWindow = np.zeros((600, 200))

for line in Lines:
	line = line.strip()

	points = line.split("->")

	firstPoint = True

	for i in range(len(points)):
		coords = points[i].split(",")
		x = int(coords[0])
		y = int(coords[1])
		bigWindow[x, y] = 1
		if(firstPoint == False):
			if(lastX == x):
				if(lastY < y):
					bigWindow[lastX, lastY:y+1] = 1
				if(y < lastY):
					bigWindow[lastX, y:lastY+1] = 1
			if(lastY == y):
				if(lastX < x):
					bigWindow[lastX:x+1, lastY] = 1
				if(x < lastX):
					bigWindow[x:lastX+1, lastY] = 1
		lastX = x
		lastY = y
		firstPoint = False

print(dropSand(bigWindow))