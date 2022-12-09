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

headX = 0
headY = 0
tailX = 0
tailY = 0

allTailPos = []
allTailPos.append((tailX, tailY))

for line in Lines:
	line = line.strip()

	direction = line[0]
	length = int(line[2:])

	for i in range(length):
		if(direction == "L"):
			headX -= 1
		elif(direction == "R"):
			headX += 1
		elif(direction == "D"):
			headY -= 1
		elif(direction == "U"):
			headY += 1

		if(isAdjacent(headX, headY, tailX, tailY) == False):
			tailX, tailY = tailMovement(headX, headY, tailX, tailY)

			if((tailX, tailY) not in allTailPos):
				allTailPos.append((tailX, tailY))

print(len(allTailPos))