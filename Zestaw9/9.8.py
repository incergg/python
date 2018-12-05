class Tree:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)


def bst_max(top):
	if top.data == None:
		raise ValueError("Drzewo  puste!")
	while(top.right):
		top = top.right
	return top.data

def bst_min(top):

	if top.data == None:
		raise ValueError("Drzewo jest puste!")
	while(top.left):
		top = top.left
	return top.data

root = Tree(4)
root.left = Tree(3)
root.right = Tree(5)
root.left.left = Tree(1)
root.left.right = Tree(2)
root.right.left = Tree(6)
root.right.right = Tree(7)

print ("Min: ", bst_min(root))
print ("Max: ", bst_max(root))