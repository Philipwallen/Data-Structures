class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		self.items.pop()
	
	def peep(self):
		return self.items[len(self.items) - 1]
		
	def size(self):
		return len(self.items)
		

def revstring(mystr):
	list1 = Stack()
	
	
	for i in mystr:
		list1.push(i)
	
	string = ''
	while not list1.isEmpty():
		string = string + str(list1.pop())
	
	return(string)
	
print(revstring('philip'))
	
	
	
