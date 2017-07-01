class Queue:
	
	def __init__(self):
		self.item = []
		
	def enqueue(self, item):
		self.item.insert(0, item)
	
	def dequeue(self):
		return self.item.pop()
		
	
	def isEmpty(self):
		return self.item == []
		
	def size(self):
		return len(self.item)


def hotPotato(nameList, num):
	simqueue = Queue()
	for name in nameList:
		simqueue.enqueue(name)
		
	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
			
		simqueue.dequeue()
	return simqueue.dequeue()
print(hotPotato(['Will', 'Philip', 'Ben', 'Jon', 'Marvin', 'Wesley'], 7))
