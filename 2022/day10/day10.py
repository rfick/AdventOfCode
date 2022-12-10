# Using readlines()
file1 = open('day10input.txt', 'r')
Lines = file1.readlines()

X = 1
cycle = 1

signalStr = 0

for line in Lines:
	line = line.strip()

	if(line[0:4] == "addx"):
		V = int(line[5:])

		cycle += 1
		if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
			signalStr += cycle * X

		cycle += 1
		X += V
		if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
			signalStr += cycle * X
	elif(line[0:4] == "noop"):
		cycle += 1
		if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
			signalStr += cycle * X

print(signalStr)