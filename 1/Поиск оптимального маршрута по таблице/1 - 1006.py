from graph import Graph, Node


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
 
g = Graph([a,b,c,d,e,f])
 
g.connect(a, b, 4)

g.connect(b, a, 4)
g.connect(b, c, 6)
g.connect(b, d, 3)
g.connect(b, e, 6)

g.connect(c, b, 6)
g.connect(c, e, 4)

g.connect(d, b, 3)
g.connect(d, e, 2)

g.connect(e, b, 6)
g.connect(e, c, 4)
g.connect(e, d, 2)
g.connect(e, f, 5)

g.connect(f, e, 5)

# print([(weight, [n.data for n in node]) for (weight, node) in g.dijkstra(a)])

print(g.dijkstra(a)[-1][0])


# Ответ: 14