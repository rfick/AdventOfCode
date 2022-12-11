class monkey():
	items = []
	opCode = ''
	operand = 0

	testVal = 0
	testTrueTarget = 0
	testFalseTarget = 0

	def operation(self, ind):
		if(self.opCode == '+'):
			self.items[ind] = self.items[ind] + self.operand
		elif(self.opCode == '*'):
			if(self.operand > 0):
				self.items[ind] = self.items[ind] * self.operand
			else:
				self.items[ind] = self.items[ind] * self.items[ind]

	def bored(self, ind):
		self.items[ind] = int(self.items[ind]/3)

	def test(self, ind):
		if(self.items[ind] % self.testVal == 0):
			target = self.testTrueTarget
		else:
			target = self.testFalseTarget

		return target

	def roundEnds(self):
		self.items = []

	def receiveItem(self, item):
		self.items.append(item)

monkey0 = [75, 63]
monkey1 = [65, 79, 98, 77, 56, 54, 83, 94]
monkey2 = [66]
monkey3 = [51, 89, 90]
monkey4 = [75, 94, 66, 90, 77, 82, 61]
monkey5 = [53, 76, 59, 92, 95]
monkey6 = [81, 61, 75, 89, 70, 92]
monkey7 = [81, 86, 62, 87]

monkeys = [monkey(), monkey(), monkey(), monkey(), monkey(), monkey(), monkey(), monkey()]
monkeys[0].items = monkey0
monkeys[0].opCode = '*'
monkeys[0].operand = 3
monkeys[0].testVal = 11
monkeys[0].testTrueTarget = 7
monkeys[0].testFalseTarget = 2

monkeys[1].items = monkey1
monkeys[1].opCode = '+'
monkeys[1].operand = 3
monkeys[1].testVal = 2
monkeys[1].testTrueTarget = 2
monkeys[1].testFalseTarget = 0

monkeys[2].items = monkey2
monkeys[2].opCode = '+'
monkeys[2].operand = 5
monkeys[2].testVal = 5
monkeys[2].testTrueTarget = 7
monkeys[2].testFalseTarget = 5

monkeys[3].items = monkey3
monkeys[3].opCode = '*'
monkeys[3].operand = 19
monkeys[3].testVal = 7
monkeys[3].testTrueTarget = 6
monkeys[3].testFalseTarget = 4

monkeys[4].items = monkey4
monkeys[4].opCode = '+'
monkeys[4].operand = 1
monkeys[4].testVal = 17
monkeys[4].testTrueTarget = 6
monkeys[4].testFalseTarget = 1

monkeys[5].items = monkey5
monkeys[5].opCode = '+'
monkeys[5].operand = 2
monkeys[5].testVal = 19
monkeys[5].testTrueTarget = 4
monkeys[5].testFalseTarget = 3

monkeys[6].items = monkey6
monkeys[6].opCode = '*'
monkeys[6].operand = -1
monkeys[6].testVal = 3
monkeys[6].testTrueTarget = 0
monkeys[6].testFalseTarget = 1

monkeys[7].items = monkey7
monkeys[7].opCode = '+'
monkeys[7].operand = 8
monkeys[7].testVal = 13
monkeys[7].testTrueTarget = 3
monkeys[7].testFalseTarget = 5

rounds = 20

monkeyInspections = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(rounds):
	for j in range(len(monkeys)):
		for k in range(len(monkeys[j].items)):
			monkeys[j].operation(k)
			monkeys[j].bored(k)
			target = monkeys[j].test(k)

			monkeys[target].receiveItem(monkeys[j].items[k])

			monkeyInspections[j] += 1

		monkeys[j].roundEnds()

monkeyInspections.sort(reverse=True)
print(monkeyInspections[0]*monkeyInspections[1])