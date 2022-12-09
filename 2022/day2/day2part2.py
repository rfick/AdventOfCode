# Using readlines()
file1 = open('day2input.txt', 'r')
Lines = file1.readlines()

totalScore = 0

for line in Lines:
	line = line.strip()
	thisScore = 0
	if(len(line) > 0):
		oppChoice = line[0]
		outcome = line[2]

		myChoice = ''

		if(oppChoice == 'A'):
			if(outcome == 'X'):
				myChoice = 'C'
			elif(outcome == 'Y'):
				myChoice = 'A'
			elif(outcome == 'Z'):
				myChoice = 'B'
		elif(oppChoice == 'B'):
			if(outcome == 'X'):
				myChoice = 'A'
			elif(outcome == 'Y'):
				myChoice = 'B'
			elif(outcome == 'Z'):
				myChoice = 'C'
		elif(oppChoice == 'C'):
			if(outcome == 'X'):
				myChoice = 'B'
			elif(outcome == 'Y'):
				myChoice = 'C'
			elif(outcome == 'Z'):
				myChoice = 'A'

		# Score for the selection
		if(myChoice == 'A'):
			thisScore += 1
		elif(myChoice == 'B'):
			thisScore += 2
		elif(myChoice == 'C'):
			thisScore += 3

		# Score for the outcome
		if(outcome == 'X'):
			thisScore += 0
		elif(outcome == 'Y'):
			thisScore += 3
		elif(outcome == 'Z'):
			thisScore += 6
		

	totalScore += thisScore

print(totalScore)