from queue import PriorityQueue
from collections import namedtuple

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end'])

class Graph:
    def __init__(self, edges, weight=lambda e: 1):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.nodes = set(sum(([e.start, e.end] for e in edges2), []))

    def __repr__(self):
        myrepr = []
        put = myrepr.append

        put("<Graph: ")

        for node in self.nodes:
            put("[{0} -> ".format(repr(node)))
            for edge in self.edges:
                if node == edge.start:
                    put("({0})".format(edge.end))
                elif node == edge.end:
                    put("({0})".format(edge.start))
            put("]")

        put(">")

        return "".join(myrepr)

    def dijkstra(self, source, dest):
        assert source in self.nodes
        dist = {node: inf for node in self.nodes}
        previous = {node: None for node in self.nodes}
        dist[source] = 0
        q = self.nodes.copy()
        neighbors = {node: set() for node in self.nodes}
        for start, end in self.edges:
            neighbors[start].add((end, self.weight(Edge(start, end))))

