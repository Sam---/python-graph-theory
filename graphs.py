#!/usr/bin/python3
import collections
import sys

Conn = collections.namedtuple('Conn', ['node', 'weight'])

def info(*tt):
    print(*tt, file=sys.stderr)

class Node:
    finf = float('inf')

    def __init__(self):
        self.connected = []
        self.origin = None
        self.dist = self.finf
        info("Created node")

    def wipe_dists(self):
        info("Wiping own distance")
        if self.dist != self.finf:
            self.dist = self.finf
            for node in connected:
                node.wipe_dists()

    def connect_to(self, node, path_weight):
        info("Connecting up")
        self.connected.append(Conn(node, path_weight))
        node.connected.append(Conn(self, path_weight))

    def set_origin(self):
        info("Setting origin")
        self.wipe_dists()
        self.build_dist(0, self)

    def build_dist(self, dd, obj):
        info("Building distance")
        self.origin = obj
        self.dist = dd
        needs_build = []
        for conn in self.connected:
            if conn.node.dist > self.dist + conn.weight:
                conn.node.build_dist(self.dist + conn.weight, obj)

    def shortest_path_to(self, nodes):
        self.set_origin()
        return [node.dist for node in nodes]

    def __repr__(self):
        return 'Node(dist={}, conn={})'.format(
                repr(self.dist), repr(self.connected))
