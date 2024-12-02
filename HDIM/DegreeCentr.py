import networkx as nx
import snap
import re

def Degree(d, e):
    f = open(d)
    s = f.read()
    s1 = re.split('\n', s)
    G1 = snap.PUNGraph.New()
    # G1 = nx.DiGraph()
    hom_influ = 0.8


    a = re.split(' ', s1[0])

    for i in range(0, int(a[0])):
     G1.AddNode(i)

    # for i in range(int(a[2]) + 1, int(a[2]) + int(a[0]) + 1):
    #     # for i in range(0, int(a[0])):
    #     # p = np.array([0.8, 0.2])
    #     # G.node[i]['Attributes'] =np.random.choice(["a", "b"], p=p.ravel())
    #     # # G.node[i]['Attributes'] =random.choice('ab')for i in range(0, int(a[0])):
    #     c = re.split(' ', s1[i])
    #     # print("22222")
    #     print(c)
    #     G1.add_node(int(c[0]))
    #     # p = np.array([0.8, 0.2])
    #     # G.node[int(c[0])]['Attributes'] =c[1]
    #     G1.node[int(c[0])]['Attributes'] = c[1]

    # print(G1.Nodes)

    # for i in range(1, int(a[1]) + 1):
    for i in range(1, int(a[2]) + 1):
     b = re.split(' ', s1[i])
     G1.AddEdge(int(b[0]), int(b[1]))

    DegCentr = dict()

    for NI in G1.Nodes():
     DegCentr[NI.GetId()] = snap.GetDegreeCentr(G1, NI.GetId())
     # print "node: %d centrality: %f" % (NI.GetId(), DegCentr)

    # print DegCentr
    EdgePara = dict()
    EP = dict()
    # for i in range(1, int(a[1]) + 1):
    for i in range(1, int(a[2]) +1):
        c = re.split(' ', s1[i])
        EdgePara[(int(c[0]), int(c[1]))] = e * DegCentr[int(c[0])] / (DegCentr[int(c[0])] + DegCentr[int(c[1])])
        # EdgePara[(int(c[1]), int(c[0]))] = e * DegCentr[int(c[1])] / (DegCentr[int(c[0])] + DegCentr[int(c[1])])
        # if G.node[(int(c[0])]['Attributes'] == G.node[(int(c[1])]['Attributes']



    return EdgePara
if __name__ == "__main__":
    G = nx.read_gpickle("Graph/retweet1.gpickle")
    d = "Graphdata/retweet1.txt"
    EdgePara1 = Degree(d, 1)
    print(EdgePara1)
