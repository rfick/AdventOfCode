# Using readlines()
file1 = open('day2input.txt', 'r')
Lines = file1.readlines()

totalScore = 0

for line in Lines:
	line = line.strip()
	thisScore = 0
	if(len(line) > 0):
		oppChoice = line[0]
		myChoice = line[2]

		# Score for the selection
		if(myChoice == 'X'):
			thisScore += 1
		elif(myChoice == 'Y'):
			thisScore += 2
		elif(myChoice == 'Z'):
			thisScore += 3

		# Score for the outcome
		if(oppChoice == 'A'):
			if(myChoice == 'X'):
				thisScore += 3
			elif(myChoice == 'Y'):
				thisScore += 6
			elif(myChoice == 'Z'):
				thisScore += 0
		elif(oppChoice == 'B'):
			if(myChoice == 'X'):
				thisScore += 0
			elif(myChoice == 'Y'):
				thisScore += 3
			elif(myChoice == 'Z'):
				thisScore += 6
		elif(oppChoice == 'C'):
			if(myChoice == 'X'):
				thisScore += 6
			elif(myChoice == 'Y'):
				thisScore += 0
			elif(myChoice == 'Z'):
				thisScore += 3

	totalScore += thisScore

print(totalScore)