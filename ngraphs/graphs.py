from collections import namedtuple
inf = float('inf')

Edge = namedtuple('Edge', ['verts', 'weight'])


class Vertex:
    def __init__(self, name=None, dist=inf, stack=None):
        self.name = name
        self.dist = dist
        self.stack = stack if stack else []

    def __repr__(self):
        return '⟦{} ({})⟧'.format(
            '→ '.join(self.stack + [self.name]), self.dist)


class Graph:
    def __init__(self, edges=None, verts=None):
        self.edges = edges if edges else set()
        self.verts = verts if verts else set()

    def connect(self, a, b, weight=1):
        b.dist = a.dist = inf
        b.stack = []
        a.stack = []
        self.verts.add(a)
        self.verts.add(b)
        self.edges.add(Edge(verts=(a, b), weight=weight))

    def _connected_to(self, v):
        for edge in self.edges:
            if v in edge.verts:
                # second part is crazy but works
                yield edge, edge.verts[edge.verts.index(v) - 1]

    def path_from(self, v):
        self._clear_dists()
        v.dist = 0
        v.stack = []
        self._propagate(v)

    def _propagate(self, v):
        for edge, node in self._connected_to(v):
            if node.name not in v.stack and v.dist + edge.weight < node.dist:
                node.dist = v.dist + edge.weight
                node.stack = v.stack + [v.name]
                self._propagate(node)

    def _clear_dists(self):
        for vert in self.verts:
            vert.dist = inf
            vert.stack = []

    def __repr__(self):
        return "Graph(verts={}, edges={})".format(
            repr(self.verts), repr(self.edges))
