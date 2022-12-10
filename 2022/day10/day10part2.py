def drawPix(screenLine, X):
	newPixPos = len(screenLine)
	if(abs(X - newPixPos) <= 1):
		screenLine += '#'
	else:
		screenLine += '.'
	return screenLine

# Using readlines()
file1 = open('day10input.txt', 'r')
Lines = file1.readlines()

X = 1
cycle = 1

screenLine = ""

for line in Lines:
	line = line.strip()

	if(line[0:4] == "addx"):
		V = int(line[5:])

		screenLine = drawPix(screenLine, X)
		if(len(screenLine) == 40):
			print(screenLine)
			screenLine = ""
		cycle += 1

		screenLine = drawPix(screenLine, X)
		if(len(screenLine) == 40):
			print(screenLine)
			screenLine = ""
		cycle += 1
		X += V
	elif(line[0:4] == "noop"):
		screenLine = drawPix(screenLine, X)
		if(len(screenLine) == 40):
			print(screenLine)
			screenLine = ""
		cycle += 1