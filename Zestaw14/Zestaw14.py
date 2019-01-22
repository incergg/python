class Edge:
	"""Klasa dla krawędzi skierowanej z wagą."""
	
	def __init__(self, source, target, weight=1):
		"""Konstruktor krawędzi.."""
		self.source = source
		self.target = target
		self.weight = weight
	
	def __repr__(self):
		"""Zwraca reprezentacje napisowa krawędzi.."""
		if self.weight == 1:
			return "Edge(%s, %s)" % (
				repr(self.source), repr(self.target))
		else:
			return "Edge(%s, %s, %s)" % (
				repr(self.source), repr(self.target), repr(self.weight))
	
	def __cmp__(self, other):
		"""Porównywanie krawędzi."""
		if self.weight > other.weight:
			return 1
		if self.weight < other.weight:
			return -1
		if self.source > other.source:
			return 1
		if self.source < other.source:
			return -1
		if self.target > other.target:
			return 1
		if self.target < other.target:
			return -1
		return 0
	
	def __hash__(self):
		"""Krawędzie są hashowalne."""
		#return hash(repr(self))
		return hash((self.source, self.target, self.weight))
	
	def __invert__(self):
		"""Zwraca krawędź o przeciwnym kierunku."""
		return Edge(self.target, self.source, self.weight)
		
class Graph:
	"""Klasa dla grafu ważonego, skierowanego lub nieskierowanego."""
	
	def __init__(self, n, directed=False):
		self.n = n               # kompatybilność
		self.directed = directed        # bool, czy graf skierowany
		self.graph= {}
	def count_nodes(self):                    # zwraca liczbę wierzchołków
		i=0
		for nodes in self.graph:
			i+=1
		return i
		
	def count_edges(self):                   # zwraca liczbę krawędzi
		i=0
		for nodes,value in self.graph.items():
			for el in value:
				i+=1
		if self.directed == False:
			return int(i/2)
		return i
			
			
	def is_directed(self):              # bool, czy graf skierowany
		return self.directed
	
	def add_node(self, node):       # dodaje wierzchołek
		if node not in self.graph:
			self.graph[node] = []
			
	def has_node(self, node):     # bool
		if node not in self.graph:
			return False
		return True
		
	def del_node(self, node): pass      # usuwa wierzchołek
	
	def add_edge(self, edge):       # wstawienie krawędzi
		if self.directed == True:
			self.add_node(edge.source)
			self.add_node(edge.target)
			if edge.source == edge.target:
				raise ValueError("Pętle zabronione")
			if (edge.target, edge.weight) not in self.graph[edge.source]:
				self.graph[edge.source].append((edge.target, edge.weight))
		else:
			self.add_node(edge.source)
			self.add_node(edge.target)
			if edge.source == edge.target:
				raise ValueError("Pętle zabronione")
			if (edge.target, edge.weight) not in self.graph[edge.source]:
				self.graph[edge.source].append((edge.target, edge.weight))

			if (edge.source, edge.weight) not in self.graph[edge.target]:
				self.graph[edge.target].append((edge.source, edge.weight))
			
				
	def has_edge(self, edge):       # bool
			if (edge.target, edge.weight) not in self.graph[edge.source]:
				if (edge.source, edge.weight) not in self.graph[edge.target]:
					return False
			return True
			
	def del_edge(self, edge): pass      # usunięcie krawędzi
	
	def weight(self, edge): pass        # zwraca wagę krawędzi
	
	def iternodes(self): pass           # iterator po wierzchołkach
	
	def iteradjacent(self, node): pass  # iterator po wierzchołkach sąsiednich
	
	def iteroutedges(self, node): pass  # iterator po krawędziach wychodzących
	
	def iterinedges(self, node): pass   # iterator po krawędziach przychodzących
	
	def iteredges(self): pass           # iterator po krawędziach
	
	def copy(self): pass                # zwraca kopię grafu
	
	def transpose(self): pass           # zwraca graf transponowany
	
	def complement(self): pass          # zwraca dopełnienie grafu
	
	def subgraph(self, nodes): pass     # zwraca podgraf indukowany

	def list_nodes(self):
		n = []
		for key in self.graph:
			n.append(key)
		return n
	
	def list_edges(self):
		e = []
		for key,values in self.graph.items():
			for el in values:
				tempe=(key,el[0])
				e.append(tempe)
		return e
	
	def save_edges(self, filename):
		f= open(filename,"w+")
		m = ""
		id = {}
		n = self.list_nodes()
		for i in range(0,len(n)):
			id[n[i]] = i
		for key,values in self.graph.items():
			for el in values:
				m+=str(id[key])
				m+=" "
				m+=str(id[el[0]])
				m+="\n"
		f.write(m)
	
	
graph = {"A": [("B", 1), ("C", 2)], 
"B": [("C", 3), ("D", 4)], 
"C": [("D", 5)], 
"D": [("C", 6)], 
"E": [("C", 7)], 
"F": []}

g1 = Graph(graph, False)
g2 = Graph(graph, True)
for key,values in graph.items():
	for el in values:
		tempe = Edge(key,el[0],el[1])
		g1.add_edge(tempe)
		g2.add_edge(tempe)

e1 = Edge('A','F',3)
e2 = Edge('F','A',3)
g1.add_edge(e1)
g1.add_edge(e2)
g2.add_edge(e1)
g2.add_edge(e2)


print ("GRAF NIESKIEROWANY\nNODES: ", g1.count_nodes())
print("EDGES: ", g1.count_edges())
print (g1.list_nodes())
print (g1.list_edges())
g1.save_edges("edges1.txt")

print ("\nGRAF SKIEROWANY\nNODES: ", g2.count_nodes())
print("EDGES: ", g2.count_edges())
print (g2.list_nodes())
print (g2.list_edges())
g2.save_edges("edges2.txt")