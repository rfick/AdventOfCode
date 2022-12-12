import numpy as np
import math

def dijkstra(nodes, edges, startNode):
	visitedNodes = {}
	visitedNodes[startNode] = 0

	workingVisited = []
	workingVisited.append(startNode)

	while(True):
		bestNode = -1
		bestDist = math.inf

		nodesToDelete = []
		for i in range(len(workingVisited)):
			node = workingVisited[i]
			nodeIsSuperfluous = True

			for connectedNode in edges[node]:
				if(connectedNode in visitedNodes):
					continue
				else:
					nodeIsSuperfluous = False
					distToNode = visitedNodes[node] + 1
					if(distToNode < bestDist):
						bestNode = connectedNode
						bestDist = distToNode
			if(nodeIsSuperfluous):
				nodesToDelete.append(node)

		for node in nodesToDelete:
			workingVisited.remove(node)

		# Path is impossible, return -1
		if(bestNode == -1):
			return -1

		visitedNodes[bestNode] = bestDist
		workingVisited.append(bestNode)

		# end node
		if(nodes[bestNode] == 'E'):
			return bestDist


# Using readlines()
file1 = open('day12input.txt', 'r')
Lines = file1.readlines()

grid = []

for line in Lines:
	line = line.strip()

	grid.append(line)

nodes = {}
edges = {}

for i in range(len(grid)):
	for j in range(len(grid[0])):
		nodes[(i, j)] = grid[i][j]
		edges[(i, j)] = []

allPossStarts = []

for i in range(len(grid)):
	for j in range(len(grid[0])):
		thisNode = nodes[(i, j)]

		if((i-1, j) in nodes):
			leftNode = nodes[(i-1, j)]
		else:
			leftNode = -1

		if((i+1, j) in nodes):
			rightNode = nodes[(i+1, j)]
		else:
			rightNode = -1

		if((i, j-1) in nodes):
			upNode = nodes[(i, j-1)]
		else:
			upNode = -1

		if((i, j+1) in nodes):
			downNode = nodes[(i, j+1)]
		else:
			downNode = -1

		# Convert start node S to a and end node E to z
		if(thisNode == 'S'):
			allPossStarts.append((i, j))
			thisNode = 'a'
		elif(thisNode == 'E'):
			thisNode = 'z'
		elif(thisNode == 'a'):
			allPossStarts.append((i, j))

		if(leftNode == 'S'):
			leftNode = 'a'
		elif(leftNode == 'E'):
			leftNode = 'z'

		if(rightNode == 'S'):
			rightNode = 'a'
		elif(rightNode == 'E'):
			rightNode = 'z'

		if(upNode == 'S'):
			upNode = 'a'
		elif(upNode == 'E'):
			upNode = 'z'

		if(downNode == 'S'):
			downNode = 'a'
		elif(downNode == 'E'):
			downNode = 'z'

		if(leftNode != -1):
			if(ord(leftNode) - ord(thisNode) <= 1):
				edges[(i, j)].append((i-1, j))

		if(rightNode != -1):
			if(ord(rightNode) - ord(thisNode) <= 1):
				edges[(i, j)].append((i+1, j))

		if(upNode != -1):
			if(ord(upNode) - ord(thisNode) <= 1):
				edges[(i, j)].append((i, j-1))

		if(downNode != -1):
			if(ord(downNode) - ord(thisNode) <= 1):
				edges[(i, j)].append((i, j+1))

allPossAnswers = []

for node in allPossStarts:
	pathCost = dijkstra(nodes, edges, node)
	if(pathCost != -1):
		allPossAnswers.append(pathCost)

print(min(allPossAnswers))