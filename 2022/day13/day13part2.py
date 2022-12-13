import ast
from functools import cmp_to_key

def compareLists(left, right):
	returnVal = 0
	if(len(left)==0 and len(right)>0):
		return 1
	for i in range(len(left)):
		# Right ran out of elements
		if(i >= len(right)):
			return -1
		if(isinstance(left[i], int) and isinstance(right[i], int)):
			if(left[i] > right[i]):
				return -1
			elif(left[i] < right[i]):
				return 1
		elif(isinstance(left[i], list) and isinstance(right[i], list)):
			returnVal = compareLists(left[i], right[i])
			if(returnVal == -1 or returnVal == 1):
				return returnVal
		elif(isinstance(left[i], int) and isinstance(right[i], list)):
			returnVal = compareLists([left[i]], right[i])
			if(returnVal == -1 or returnVal == 1):
				return returnVal
		elif(isinstance(left[i], list) and isinstance(right[i], int)):
			returnVal = compareLists(left[i], [right[i]])
			if(returnVal == -1 or returnVal == 1):
				return returnVal
		if(i == len(left)-1 and i<len(right)-1):
			return 1
	return returnVal

# Using readlines()
file1 = open('day13input.txt', 'r')
Lines = file1.readlines()

firstList = []
secondList = []

readingFirst = True
readingSecond = False
readingBlankLine = False

allPackets = []
allPackets.append([[2]])
allPackets.append([[6]])

for line in Lines:
	line = line.strip()

	if(readingFirst):
		firstList = line
		readingFirst = False
		readingSecond = True
	elif(readingSecond):
		secondList = line
		readingSecond = False
		readingBlankLine = True

		firstList = ast.literal_eval(firstList)
		secondList = ast.literal_eval(secondList)

		allPackets.append(firstList)
		allPackets.append(secondList)
	elif(readingBlankLine):
		readingBlankLine = False
		readingFirst = True

packetsSorted = sorted(allPackets, key=cmp_to_key(compareLists), reverse=True)

firstPacket = packetsSorted.index([[2]])+1
secondPacket = packetsSorted.index([[6]])+1

print(firstPacket*secondPacket)