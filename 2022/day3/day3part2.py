# Using readlines()
file1 = open('day3input.txt', 'r')
Lines = file1.readlines()

firstLine = ''
secondLine = ''
thirdLine = ''

totalScore = 0

for line in Lines:
	line = line.strip()
	
	if(firstLine == ''):
		firstLine = line
		continue
	elif(firstLine != '' and secondLine == ''):
		secondLine = line
		continue
	else:
		thirdLine = line

	sharedElement = list(set(firstLine).intersection(secondLine).intersection(thirdLine))[0]

	thisScore = 0

	if(sharedElement == 'a'):
		thisScore = 1
	elif(sharedElement == 'b'):
		thisScore = 2
	elif(sharedElement == 'c'):
		thisScore = 3
	elif(sharedElement == 'd'):
		thisScore = 4
	elif(sharedElement == 'e'):
		thisScore = 5
	elif(sharedElement == 'f'):
		thisScore = 6
	elif(sharedElement == 'g'):
		thisScore = 7
	elif(sharedElement == 'h'):
		thisScore = 8
	elif(sharedElement == 'i'):
		thisScore = 9
	elif(sharedElement == 'j'):
		thisScore = 10
	elif(sharedElement == 'k'):
		thisScore = 11
	elif(sharedElement == 'l'):
		thisScore = 12
	elif(sharedElement == 'm'):
		thisScore = 13
	elif(sharedElement == 'n'):
		thisScore = 14
	elif(sharedElement == 'o'):
		thisScore = 15
	elif(sharedElement == 'p'):
		thisScore = 16
	elif(sharedElement == 'q'):
		thisScore = 17
	elif(sharedElement == 'r'):
		thisScore = 18
	elif(sharedElement == 's'):
		thisScore = 19
	elif(sharedElement == 't'):
		thisScore = 20
	elif(sharedElement == 'u'):
		thisScore = 21
	elif(sharedElement == 'v'):
		thisScore = 22
	elif(sharedElement == 'w'):
		thisScore = 23
	elif(sharedElement == 'x'):
		thisScore = 24
	elif(sharedElement == 'y'):
		thisScore = 25
	elif(sharedElement == 'z'):
		thisScore = 26
	elif(sharedElement == 'A'):
		thisScore = 27
	elif(sharedElement == 'B'):
		thisScore = 28
	elif(sharedElement == 'C'):
		thisScore = 29
	elif(sharedElement == 'D'):
		thisScore = 30
	elif(sharedElement == 'E'):
		thisScore = 31
	elif(sharedElement == 'F'):
		thisScore = 32
	elif(sharedElement == 'G'):
		thisScore = 33
	elif(sharedElement == 'H'):
		thisScore = 34
	elif(sharedElement == 'I'):
		thisScore = 35
	elif(sharedElement == 'J'):
		thisScore = 36
	elif(sharedElement == 'K'):
		thisScore = 37
	elif(sharedElement == 'L'):
		thisScore = 38
	elif(sharedElement == 'M'):
		thisScore = 39
	elif(sharedElement == 'N'):
		thisScore = 40
	elif(sharedElement == 'O'):
		thisScore = 41
	elif(sharedElement == 'P'):
		thisScore = 42
	elif(sharedElement == 'Q'):
		thisScore = 43
	elif(sharedElement == 'R'):
		thisScore = 44
	elif(sharedElement == 'S'):
		thisScore = 45
	elif(sharedElement == 'T'):
		thisScore = 46
	elif(sharedElement == 'U'):
		thisScore = 47
	elif(sharedElement == 'V'):
		thisScore = 48
	elif(sharedElement == 'W'):
		thisScore = 49
	elif(sharedElement == 'X'):
		thisScore = 50
	elif(sharedElement == 'Y'):
		thisScore = 51
	elif(sharedElement == 'Z'):
		thisScore = 52

	totalScore += thisScore

	firstLine = ''
	secondLine = ''
	thirdLine = ''

print(totalScore)