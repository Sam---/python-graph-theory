from graphs import Node
from pprint import pprint

A, B, C = Node(), Node(), Node()

A.connect_to(B, 10)
B.connect_to(C, 5)
A.connect_to(C, 12)

pprint([A,B,C])

A.shortest_path_to([C])

pprint([A,B,C])
