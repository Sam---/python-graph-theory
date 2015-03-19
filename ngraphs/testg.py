import graphs
import sys

usa = graphs.Vertex(name="USA")
mexico = graphs.Vertex(name="Mexico")
canada = graphs.Vertex(name="Canada")
algeria = graphs.Vertex(name="Algeria")
uk = graphs.Vertex(name="UK")

g = graphs.Graph()
g.connect(usa, mexico, weight=3)
g.connect(usa, canada, weight=60)
g.connect(algeria, canada, weight=2)
g.connect(uk, algeria, weight=1)
g.connect(uk, usa, weight=10)
