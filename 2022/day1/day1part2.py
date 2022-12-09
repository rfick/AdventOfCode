# Using readlines()
file1 = open('day1input.txt', 'r')
Lines = file1.readlines()

maxElfCalories = 0
secondMaxElfCalories = 0
thirdMaxElfCalories = 0
thisElfCalories = 0

for line in Lines:
	line = line.strip()
	if(len(line) > 0):
		thisElfCalories += int(line)
	else:
		if(thisElfCalories > maxElfCalories):
			thirdMaxElfCalories = secondMaxElfCalories
			secondMaxElfCalories = maxElfCalories
			maxElfCalories = thisElfCalories
		elif(thisElfCalories > secondMaxElfCalories):
			thirdMaxElfCalories = secondMaxElfCalories
			secondMaxElfCalories = thisElfCalories
		elif(thisElfCalories > thirdMaxElfCalories):
			thirdMaxElfCalories = thisElfCalories
		thisElfCalories = 0

print(maxElfCalories+secondMaxElfCalories+thirdMaxElfCalories)