import re
from collections import deque

# Hard coded input lists
stack1 = deque()
stack1.append('F');stack1.append('C');stack1.append('J');stack1.append('P');stack1.append('H');stack1.append('T');stack1.append('W')
stack2 = deque()
stack2.append('G');stack2.append('R');stack2.append('V');stack2.append('F');stack2.append('Z');stack2.append('J');stack2.append('B');stack2.append('H')
stack3 = deque()
stack3.append('H');stack3.append('P');stack3.append('T');stack3.append('R')
stack4 = deque()
stack4.append('Z');stack4.append('S');stack4.append('N');stack4.append('P');stack4.append('H');stack4.append('T')
stack5 = deque()
stack5.append('N');stack5.append('V');stack5.append('F');stack5.append('Z');stack5.append('H');stack5.append('J');stack5.append('C');stack5.append('D')
stack6 = deque()
stack6.append('P');stack6.append('M');stack6.append('G');stack6.append('F');stack6.append('W');stack6.append('D');stack6.append('Z')
stack7 = deque()
stack7.append('M');stack7.append('V');stack7.append('Z');stack7.append('W');stack7.append('S');stack7.append('J');stack7.append('D');stack7.append('P')
stack8 = deque()
stack8.append('N');stack8.append('D');stack8.append('S')
stack9 = deque()
stack9.append('D');stack9.append('Z');stack9.append('S');stack9.append('F');stack9.append('M')

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

# Using readlines()
file1 = open('day5input.txt', 'r')
Lines = file1.readlines()

for line in Lines:
	line = line.strip()

	numToMove, source, dest = map(int, re.findall('\d+', line))

	boxesInOrder = []

	for i in range(numToMove):
		box = stacks[source-1].pop()
		boxesInOrder.append(box)

	boxesInOrder.reverse()

	for box in boxesInOrder:
		stacks[dest-1].append(box)

finalanswer = ''

for stack in stacks:
	finalanswer += stack.pop()

print(finalanswer)