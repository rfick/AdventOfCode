def spawnRock(highestRock, rockOrder):
	rockCoords = []
	if(rockOrder%5 == 0):
		rockCoords.append((3, highestRock+4))
		rockCoords.append((4, highestRock+4))
		rockCoords.append((5, highestRock+4))
		rockCoords.append((6, highestRock+4))
	elif(rockOrder%5 == 1):
		rockCoords.append((3, highestRock+5))
		rockCoords.append((4, highestRock+5))
		rockCoords.append((5, highestRock+5))
		rockCoords.append((4, highestRock+4))
		rockCoords.append((4, highestRock+6))
	elif(rockOrder%5 == 2):
		rockCoords.append((3, highestRock+4))
		rockCoords.append((4, highestRock+4))
		rockCoords.append((5, highestRock+4))
		rockCoords.append((5, highestRock+5))
		rockCoords.append((5, highestRock+6))
	elif(rockOrder%5 == 3):
		rockCoords.append((3, highestRock+4))
		rockCoords.append((3, highestRock+5))
		rockCoords.append((3, highestRock+6))
		rockCoords.append((3, highestRock+7))
	elif(rockOrder%5 == 4):
		rockCoords.append((3, highestRock+4))
		rockCoords.append((4, highestRock+4))
		rockCoords.append((3, highestRock+5))
		rockCoords.append((4, highestRock+5))
	return rockCoords

def pushRockSideways(chamber, rockCoords, jet):
	rockMoveIsValid = True
	newRockCoords = []
	if(jet == '>'):
		for coord in rockCoords:
			if((coord[0]+1) < 1 or (coord[0]+1) > 7):
				rockMoveIsValid = False
			if((coord[0]+1, coord[1]) in chamber):
				rockMoveIsValid = False
			newRockCoords.append((coord[0]+1, coord[1]))
	elif(jet == '<'):
		for coord in rockCoords:
			if((coord[0]-1) < 1 or (coord[0]-1) > 7):
				rockMoveIsValid = False
			if((coord[0]-1, coord[1]) in chamber):
				rockMoveIsValid = False
			newRockCoords.append((coord[0]-1, coord[1]))

	if(rockMoveIsValid):
		return newRockCoords
	else:
		return rockCoords

def rockFallsDown(chamber, rockCoords):
	rockMoveIsValid = True
	newRockCoords = []
	for coord in rockCoords:
		if((coord[0], coord[1]-1) in chamber):
			rockMoveIsValid = False
		newRockCoords.append((coord[0], coord[1]-1))

	if(rockMoveIsValid):
		return newRockCoords
	else:
		return rockCoords

# Using readlines()
file1 = open('day17input.txt', 'r')
Lines = file1.readlines()

jetPattern = ''

for line in Lines:
	line = line.strip()
	jetPattern = line

# chamber coords are (x, y)
# chamber is 7 units wide, from 1 to 7 in x (0 and 8 are walls)
# chamber floor is y=0
chamber = {}
chamber[(1, 0)] = 1
chamber[(2, 0)] = 1
chamber[(3, 0)] = 1
chamber[(4, 0)] = 1
chamber[(5, 0)] = 1
chamber[(6, 0)] = 1
chamber[(7, 0)] = 1

# tracks current highest stationary rock
highestRock = 0

# rockOrder % 5 determines next spawning rock
rockOrder = 0

# jetOrder % len(jetPattern) determines next jet
jetOrder = 0

numRocks = 1000000000000

cycleFound = False
cycleJet = 0
cycleRock = 0
cycleStartHeight = 0
cycleIncrementHeight = 0
cycleStartRock = 0
cycleIncrementRock = 0

finishedJets = {}

for i in range(numRocks):
	rockCoords = spawnRock(highestRock, rockOrder)
	rockOrder += 1
	while(True):
		jet = jetPattern[jetOrder%len(jetPattern)]
		jetOrder += 1
		rockCoords = pushRockSideways(chamber, rockCoords, jet)
		newRockCoords = rockFallsDown(chamber, rockCoords)

		if(newRockCoords == rockCoords):
			for coord in newRockCoords:
				chamber[coord] = 1
				if(coord[1] > highestRock):
					highestRock = coord[1]
			break
		else:
			rockCoords = newRockCoords

	if(rockOrder%5 == 0):
		if((jetOrder%len(jetPattern), rockOrder%5) not in finishedJets):
			finishedJets[(jetOrder%len(jetPattern), rockOrder%5)] = ([highestRock], [rockOrder])
		else:
			finishedJets[(jetOrder%len(jetPattern), rockOrder%5)][0].append(highestRock)
			finishedJets[(jetOrder%len(jetPattern), rockOrder%5)][1].append(rockOrder)
			heights = finishedJets[(jetOrder%len(jetPattern), rockOrder%5)][0]
			rocks = finishedJets[(jetOrder%len(jetPattern), rockOrder%5)][1]
			heightDiffs = [j-i for i, j in zip(heights[:-1], heights[1:])]
			rockDiffs = [j-i for i, j in zip(rocks[:-1], rocks[1:])]
			
			if(len(heights) > 10):
				unique_set = list(set(heightDiffs))
				if(len(unique_set) == 1):
					cycleFound = True
					cycleJet = jetOrder%len(jetPattern)
					cycleRock = rockOrder%5
					cycleStartHeight = heights[1]
					cycleIncrementHeight = heightDiffs[0]
					cycleStartRock = rocks[1]
					cycleIncrementRock = rockDiffs[0]
	if(cycleFound):
		break

numCycles = int((numRocks - cycleStartRock)/cycleIncrementRock)

heightAtCycleEnd = cycleStartHeight + numCycles*cycleIncrementHeight


newNumRocks = cycleStartRock + (numRocks - (cycleStartRock + numCycles*cycleIncrementRock))




# chamber coords are (x, y)
# chamber is 7 units wide, from 1 to 7 in x (0 and 8 are walls)
# chamber floor is y=0
chamber = {}
chamber[(1, 0)] = 1
chamber[(2, 0)] = 1
chamber[(3, 0)] = 1
chamber[(4, 0)] = 1
chamber[(5, 0)] = 1
chamber[(6, 0)] = 1
chamber[(7, 0)] = 1

# tracks current highest stationary rock
highestRock = 0

# rockOrder % 5 determines next spawning rock
rockOrder = 0

# jetOrder % len(jetPattern) determines next jet
jetOrder = 0

finishedJets = {}

for i in range(newNumRocks):
	rockCoords = spawnRock(highestRock, rockOrder)
	rockOrder += 1
	while(True):
		jet = jetPattern[jetOrder%len(jetPattern)]
		jetOrder += 1
		rockCoords = pushRockSideways(chamber, rockCoords, jet)
		newRockCoords = rockFallsDown(chamber, rockCoords)

		if(newRockCoords == rockCoords):
			for coord in newRockCoords:
				chamber[coord] = 1
				if(coord[1] > highestRock):
					highestRock = coord[1]
			break
		else:
			rockCoords = newRockCoords

print(heightAtCycleEnd + (highestRock - cycleStartHeight))