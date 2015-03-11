from queue import PriorityQueue
from collections import namedtuple

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', '_cost'])

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_node(self, newnode):
        self.nodes.add(newnode)

    def connect(self, node1, node2):
        if node1 in self.nodes:
            if node2 in self.nodes:
                if node1 != node2:
                    self.edges.add((node1, node2))
                else:
                    raise ValueError("Can't connect node {0} to itself".format(
                        repr(node1)))
            else:
                raise ValueError("Node {0} not in graph".format(repr(node2)))
        else:
            raise ValueError("Node {0} not in graph".format(repr(node1)))

    def disconnect(self, node1, node2):
        tup = (node1, node2)
        if tup in self.edges:
            self.edges.discard(tup)
        else:
            raise ValueError("Edge {0} already in graph".format(repr(tup)))

    def delnode(self, node, clean_edges=True):
        if node in self.nodes:
            if clean_edges:
                for n1, n2 in self.edges:
                    if n1 == node or n2 == node:
                        self.edges.discard((n1, n2))
            self.nodes.discard(node)
        else:
            raise ValueError("Node {0} not in graph".format(repr(node)))

    def __repr__(self):
        myrepr = []
        put = myrepr.append

        put("<Graph: ")

        for node in self.nodes:
            put("[{0} -> ".format(repr(node)))
            for edge in self.edges:
                if node == edge[0]:
                    put("({0})".format(edge[1]))
                elif node == edge[1]:
                    put("({0})".format(edge[0]))
            put("]")

        put(">")

        return "".join(myrepr)

def dijkstra_shortest_path(gg, source, weight=(lambda a,b: 0)):
    pq = PriorityQueue()
    dist = {} dict
    dist[start] = 0
    for node in gg.nodes:
        pq.put((dist.setdefault(node), node))

    while not pq.empty():
        currentn = pq.get()
        for nextn in gg.get_edges(currentn):
            new_dist = dist[currentn] + weight(currentn, nextn)
            if new_dist < dist[nextn]:
                dist[nextn] = new_dist
                nextn.set_pred(currentn)
                pq.decrease

