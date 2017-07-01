class UnorderedList:
	
	def __init__(self):
		self.head = None
		
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		
	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
				
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	
	def search(self, item):
		current = self.head
		found = False
		while != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
				
		return found
		
		
	def isEmpty(self):
		return self.head == None
		
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		
		return count
	
	def append(self, item):
		self.items.append(item)
		
	def index(self, item):
		self.items.index(item)
		
	def insert(self, pos, item):
		self.items.insert(pos, item)
		
	def pop(self):
		self.items.pop()
		
	def pop(self, pos):
		self.items.pop(pos)
		
		
	
