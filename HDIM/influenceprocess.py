import copy
import re

import networkx as nx
import random
from PageRankCentr import PageRank
from ClosenessCentr import Closeness
from DegreeCentr import Degree
from duibi_newdiscount import DUIBI_NewDiscount
from EccentricCentr import Eccentric
from NewDiscount import NewDiscount
from GreedyCIC import GreedyCIC
from degreeDiscount import degreeDiscountIC
from GeneralParameter import General
from newGreedyIC import newGreedyIC

# def influence(G, S, Ep):
# 	F = []
#
# 	F += S
#
# 	for s in S:
# 		for i in range(0, len(G.neighbors(s))):
# 			if G.neighbors(s)[i] not in F:
# 				if random.random() > (1 - Ep[s, G.neighbors(s)[i]]):
# 					F.append(G.neighbors(s)[i])
# 				else:
# 					continue
# 	return F
f = open("E:\IM\dyn-homnet-Centrality-Influence-Maximization-master\Graphdata\\test1.txt")
s = f.read()
s1 = re.split('\n', s)
Time = {}
a = re.split(' ', s1[0])

for i in range(1, int(a[2]) + 1):
    b = re.split(' ', s1[i])
    # print("111111")
    print(b)
    time_key = ()
    time_key = (int(b[0]), int(b[1]))
    time_value = b[2]
    Time.update({time_key: time_value})
    print(Time)


def influence(G, S, Ep, k_a, k_b):
    newActive = True
    currentActiveNodes = copy.deepcopy(S)
    # print(currentActiveNodes)
    newActiveNodes = set()
    activatedNodes = copy.deepcopy(S)  # Biar ga keaktivasi 2 kali
    influenceSpread = len(S)
    Attribute = dict()
    EP = dict()
    k_a = k_a
    k_b = k_b
    print(k_a)
    print(k_b)
    act_a = 0
    act_b = 0

    # Define the initial active time of the seed node as 0
    Act = {}
    for v in S:
        Act[v] = 0
    print(Act)

    while (newActive):
        for node in currentActiveNodes:
            for neighbor in G.neighbors(node):
                if (neighbor not in activatedNodes):
                    if G.node[node]['Attributes'] == G.node[neighbor]['Attributes']:
                        EP[node, neighbor] = 0.8 * Ep[node, neighbor] + 0.2 * 0.6

                    else:
                        EP[node, neighbor] = 0.8 * Ep[node, neighbor] + 0.2 * 0.4

                    # if (G[node][neighbor]['Ep'] > propProbability):  # flipCoin(propProbability)
                    # if random.random()>(1-EP[node,neighbor]) and Time[(node,neighbor)]<=time:
                    if random.random() > (1 - EP[node, neighbor]) and Act[node] < Time[(node, neighbor)]:
                        # 	print(node,neighbor,Time[(node,neighbor)])
                        newActiveNodes.add(neighbor)
                        Act.update({neighbor: Time[(node, neighbor)]})
                        activatedNodes.append(neighbor)
                        Attribute[neighbor] = G.node[neighbor]['Attributes']
        influenceSpread += len(newActiveNodes)
        if newActiveNodes:
            currentActiveNodes = list(newActiveNodes)
            newActiveNodes = set()
        else:
            newActive = False
    print("activatedNodes", len(activatedNodes), activatedNodes)

    values = Attribute.values()  # Gets the label of the activated node
    for value in values:
        # print(value)
        if (value == 'a'):
            act_a = act_a + 1
        else:
            act_b = act_b + 1

    act_a_sum = k_a + act_a
    act_b_sum = k_b + act_b
    fin_pro = float(act_a_sum) / float(act_b_sum)
    print(fin_pro)

    print(Attribute)
    print(act_a)
    print(act_b)

    return influenceSpread


# def flipCoin(probability):
#     return random.random() < probability

if __name__ == "__main__":
    G = nx.read_gpickle("Graph/test1.gpickle")
    d = "Graphdata/test1.txt"

    EdgePara1 = Degree(d, 0.01)
    # print(EdgePara1[5])
    # EdgePara2 = PageRank(d, 0.01)
    # EdgePara3 = Eccentric(d, 0.01)
    # EdgePara4 = Closeness(d, 0.01)
    # EdgePara = General(d, 1)
    # S1,k_a,k_b = DUIBI_NewDiscount(G, 25, EdgePara1)
    S1, k_a, k_b = NewDiscount(G, 3, EdgePara1)
    print (S1)
    # S2 = NewDiscount(G, 10, EdgePara2)
    # S3 = NewDiscount(G, 10, EdgePara3)
    # S4 = NewDiscount(G, 10, EdgePara4)
    # S5 = degreeDiscountIC(G, 10, 1)
    # S6 = newGreedyIC(G, 10, 1)
    # S7 = GreedyCIC(G, 10, EdgePara1)
    # S8 = GreedyCIC(G, 10, EdgePara2)
    # S9 = GreedyCIC(G, 10, EdgePara3)
    # S10 = GreedyCIC(G, 10, EdgePara4)

    F1 = []
    F2 = []
    F3 = []
    F4 = []
    F5 = []
    F6 = []
    F7 = []
    F8 = []
    F9 = []
    F10 = []

    for i in range(0, 1):
        # for i in range(0, 1000):
        F = influence(G, S1, EdgePara1, k_a, k_b)
        F1.append(F)
    print float(sum(F1) / len(F1))

# for i in range(0, 1000):
# 	F = influence(G, S2, EdgePara2)
# 	F2.append(len(F))
# print float(sum(F2)/len(F2))

# for i in range(0, 1000):
# 	F = influence(G, S3, EdgePara3)
# 	F3.append(len(F))
# print float(sum(F3)/len(F3))

# for i in range(0, 1000):
# 	F = influence(G, S4, EdgePara4)
# 	F4.append(len(F))
# print float(sum(F4)/len(F4))

# for i in range(0, 1000):
# 	F = influence(G, S5, EdgePara)
# 	F5.append(len(F))
# print float(sum(F5)/len(F5))

# for i in range(0, 1000):
# 	F = influence(G, S6, EdgePara)
# 	F6.append(len(F))
# print float(sum(F6)/len(F6))

# for i in range(0, 1000):
# 	F = influence(G, S7, EdgePara1)
# 	F7.append(len(F))
# print float(sum(F7)/len(F7))

# for i in range(0, 1000):
# 	F = influence(G, S8, EdgePara2)
# 	F8.append(len(F))
# print float(sum(F8)/len(F8))

# for i in range(0, 1000):
# 	F = influence(G, S9, EdgePara3)
# 	F9.append(len(F))
# print float(sum(F9)/len(F9))

# for i in range(0, 1000):
# 	F = influence(G, S10, EdgePara4)
# 	F10.append(len(F))
# print float(sum(F10)/len(F10))
