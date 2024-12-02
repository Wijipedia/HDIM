import random
from copy import deepcopy
import networkx as nx
import re

import numpy as np
from networkx import DiGraph

f = open("E:\IM\dyn-homnet-Centrality-Influence-Maximization-master\Graphdata\\test1.txt")
s = f.read()
s1 = re.split('\n', s)
# print(s1)
G = nx.DiGraph()  # type: DiGraph
Time = {}

a = re.split(' ', s1[0])
# print(a)

for i in range(int(a[2]) + 1, int(a[2]) + int(a[0]) + 1):
    # for i in range(0, int(a[0])):
    # p = np.array([0.8, 0.2])
    # G.node[i]['Attributes'] =np.random.choice(["a", "b"], p=p.ravel())
    # # G.node[i]['Attributes'] =random.choice('ab')for i in range(0, int(a[0])):
    c = re.split(' ', s1[i])
    # print("22222")
    # print(c)
    G.add_node(int(c[0]))
    # p = np.array([0.8, 0.2])
    # G.node[int(c[0])]['Attributes'] =c[1]
    G.node[int(c[0])]['Attributes'] = c[1]

# print(G.node)

# for i in range(1, int(a[1]) + 1):
for i in range(1, int(a[2]) + 1):
    b = re.split(' ', s1[i])
    # print("111111")
    print(b)
    time_key=()
    G.add_edge(int(b[0]), int(b[1]))
    time_key=(int(b[0]), int(b[1]))
    time_value=b[2]
    Time.update({time_key:time_value})
    print(Time)
    G[int(b[0])][int(b[1])]['weight'] = 1

nx.write_gpickle(G, "test1.gpickle")

# G1 = nx.read_gpickle("graphs/test.gpickle")
# print G1[0][1]['weight']
