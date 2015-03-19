import graphs

node0 = graphs.Vertex(name='0')
node1 = graphs.Vertex(name='1')
node2 = graphs.Vertex(name='2')
node3 = graphs.Vertex(name='3')

g = graphs.Graph()

g.connect(node0, node1, weight=-5)
g.connect(node0, node3, weight=3)
g.connect(node0, node2, weight=2)
g.connect(node1, node2, weight=4)
g.connect(node3, node2, weight=1)

