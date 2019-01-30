class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next

	def __str__(self):
		return str(self.data)
		
def print_list(node):
	s = ""
	while node:
		s+=str(node)
		s+=" "
		node=node.next
	print (s, "\n")
		

def remove_head(node):
	if node == None:
		raise ValueError("Lista pusta!")
	tmp = node
	node = node.next
	return node, tmp

def remove_tail(node): 
	if node == None:
		raise ValueError("Lista pusta!")
	head = node
	tmplast = None
	while (node.next):
		tmplast = node
		node = node.next
	if tmplast == None:
		return None, node
	tmplast.next = None
	return head, node
		


print ("REMOVE TAIL!\n")
head1 = None
head1 = Node(1, head1)
print_list(head1)
head1 = Node(2, head1)
print_list(head1)
head1 = Node(3, head1)

print_list(head1)

head1, node = remove_tail(head1)
print_list(head1)

head1, node = remove_tail(head1)
print_list(head1)

head1, node  = remove_tail(head1)
print_list(head1)


print ("REMOVE HEAD!\n")
head1 = None
head1 = Node(1, head1)
head1 = Node(2, head1)
head1 = Node(3, head1)

print_list(head1)

head1, node = remove_head(head1)
print_list(head1)

head1, node = remove_head(head1)
print_list(head1)

head1, node  = remove_head(head1)
print_list(head1)


print_list(head1)
print_list(head1)