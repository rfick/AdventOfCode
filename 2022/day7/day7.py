class TreeStructureThatIsntDogshit:
	def __init__(self, name):
		self.name = name
		self.children = []
		self.parent = None

class TreeInfo:
	def __init__(self):
		self.finalAnswer = 0
		self.subTreeSum = 0

def is_integer(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()

def treeWalk(tree, treeInfo):
	if(is_integer(tree.name)):
		treeInfo.subTreeSum = int(tree.name)
		return
	thisSubTree = 0
	for child in tree.children:
		treeWalk(child, treeInfo)
		thisSubTree += treeInfo.subTreeSum
	treeInfo.subTreeSum = thisSubTree
	if(treeInfo.subTreeSum <= 100000):
		treeInfo.finalAnswer += treeInfo.subTreeSum

# Using readlines()
file1 = open('day7input.txt', 'r')
Lines = file1.readlines()

currentFolder = "/"

treeRoot = TreeStructureThatIsntDogshit("/")

currNode = treeRoot

for line in Lines:
	line = line.strip()

	if(line[0] == "$"):
		if(line[2:4] == "cd"):
			folderName = line[5:]
			if(folderName == "/"):
				currentFolder = "/"
			elif(folderName == ".."):
				folderSegments = currentFolder.split("/")
				newFolder = ""
				for i in range(0, len(folderSegments)-2):
					newFolder = newFolder + folderSegments[i] + "/"
				currentFolder = newFolder

				currNode = currNode.parent
			else:
				currentFolder = currentFolder + folderName + "/"

				childNodes = currNode.children
				for i in range(len(childNodes)):
					if(childNodes[i].name == folderName):
						currNode = childNodes[i]
						break
		#elif(line[2:4] == "ls"):
			# Do nothing?
	else:
		if(line[0:3] == "dir"):
			folderName = line[4:]

			childNode = TreeStructureThatIsntDogshit(folderName)
			childNode.parent = currNode
			currNode.children.append(childNode)
		else:
			lineSegments = line.split(" ")
			fileSize = lineSegments[0]
			fileName = lineSegments[1]

			leafNode = TreeStructureThatIsntDogshit(fileSize)
			leafNode.parent = currNode
			currNode.children.append(leafNode)

treeInfo = TreeInfo()

# Start walking the tree
treeWalk(treeRoot, treeInfo)

print(treeInfo.finalAnswer)