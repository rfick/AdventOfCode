# Using readlines()
file1 = open('day6input.txt', 'r')
Lines = file1.readlines()

for line in Lines:
	line = line.strip()

	answer = -1

	for i in range(14, len(line)):
		fourCharSeq = line[i-14:i]
		listSet = set(fourCharSeq)
		uniqueList = list(listSet)
		
		if(len(uniqueList) == 14):
			answer = i
			break

	print(answer)