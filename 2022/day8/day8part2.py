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

bestScoreSoFar = 0

for row in range(trees.shape[0]):
	for col in range(trees.shape[1]):
		leftSlice = trees[:row, col]
		rightSlice = trees[row+1:, col]
		upSlice = trees[row, :col]
		downSlice = trees[row, col+1:]

		leftSlice = np.flip(leftSlice)
		upSlice = np.flip(upSlice)

		leftScore = 0
		for i in range(len(leftSlice)):
			if(leftSlice[i] < trees[row, col]):
				leftScore += 1
			else:
				leftScore += 1
				break

		rightScore = 0
		for i in range(len(rightSlice)):
			if(rightSlice[i] < trees[row, col]):
				rightScore += 1
			else:
				rightScore += 1
				break

		upScore = 0
		for i in range(len(upSlice)):
			if(upSlice[i] < trees[row, col]):
				upScore += 1
			else:
				upScore += 1
				break

		downScore = 0
		for i in range(len(downSlice)):
			if(downSlice[i] < trees[row, col]):
				downScore += 1
			else:
				downScore += 1
				break

		thisScore = leftScore * rightScore * upScore * downScore

		if(thisScore > bestScoreSoFar):
			bestScoreSoFar = thisScore

print(bestScoreSoFar)