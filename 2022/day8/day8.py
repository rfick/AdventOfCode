import numpy as np

# Using readlines()
file1 = open('day8input.txt', 'r')
Lines = file1.readlines()

trees = np.zeros((99, 99))

row = 0

for line in Lines:
	line = line.strip()

	for i in range(len(line)):
		trees[row, i] = line[i]

	row += 1

visibleTrees = 0

for row in range(trees.shape[0]):
	for col in range(trees.shape[1]):
		leftSlice = trees[:row, col]
		rightSlice = trees[row+1:, col]
		upSlice = trees[row, :col]
		downSlice = trees[row, col+1:]

		if(all(i < trees[row, col] for i in leftSlice)):
			visibleTrees += 1
		elif(all(i < trees[row, col] for i in rightSlice)):
			visibleTrees += 1
		elif(all(i < trees[row, col] for i in upSlice)):
			visibleTrees += 1
		elif(all(i < trees[row, col] for i in downSlice)):
			visibleTrees += 1

print(visibleTrees)