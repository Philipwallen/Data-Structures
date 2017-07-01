from binary_tree import BinaryTree
from stack_class import Stack

def buildParseTree(math_exp):
	mExpList = math_exp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	
	for i in mExpList:
		
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
			
		elif i not in ['+', '-', '*', '/', ')']:
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
			
		elif i in ['+', '-', '*', '/',]:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
			
		elif i == ')':
			currentTree = pStack.pop()
			
		else:
			raise ValueError
	return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 ) ")	

print(pt)
