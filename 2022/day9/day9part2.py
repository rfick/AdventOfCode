def isAdjacent(headX, headY, tailX, tailY):
	if(abs(tailX - headX) <= 1 and abs(tailY - headY) <= 1):
		return True
	else:
		return False

def tailMovement(headX, headY, tailX, tailY):
	if(headX == tailX):
		if(headY > tailY):
			tailY += 1
		elif(headY < tailY):
			tailY -= 1
	elif(headY == tailY):
		if(headX > tailX):
			tailX += 1
		elif(headX < tailX):
			tailX -= 1
	elif(headX > tailX):
		if(headY > tailY):
			tailX += 1
			tailY += 1
		elif(headY < tailY):
			tailX += 1
			tailY -= 1
	elif(headX < tailX):
		if(headY > tailY):
			tailX -= 1
			tailY += 1
		elif(headY < tailY):
			tailX -= 1
			tailY -= 1

	return tailX, tailY

# Using readlines()
file1 = open('day9input.txt', 'r')
Lines = file1.readlines()

# Pos 0 is head, pos 1 is knot 1, pos 2 is knot 2, etc.
allXs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
allYs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

allTailPos = []
allTailPos.append((allXs[9], allYs[9]))

for line in Lines:
	line = line.strip()

	direction = line[0]
	length = int(line[2:])

	for i in range(length):
		if(direction == "L"):
			allXs[0] -= 1
		elif(direction == "R"):
			allXs[0] += 1
		elif(direction == "D"):
			allYs[0] -= 1
		elif(direction == "U"):
			allYs[0] += 1

		for j in range(len(allXs)-1):
			if(isAdjacent(allXs[j], allYs[j], allXs[j+1], allYs[j+1]) == False):
				allXs[j+1], allYs[j+1] = tailMovement(allXs[j], allYs[j], allXs[j+1], allYs[j+1])

		if((allXs[9], allYs[9]) not in allTailPos):
			allTailPos.append((allXs[9], allYs[9]))

print(len(allTailPos))