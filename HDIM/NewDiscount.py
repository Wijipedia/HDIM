from string import count

from priorityQueue import PriorityQueue as PQ # priority queue
import networkx as nx
from PageRankCentr import PageRank
from ClosenessCentr import Closeness
from DegreeCentr import Degree
from EccentricCentr import Eccentric

def NewDiscount(G, k, p):

    S = []
    # print(len(S))
    dd = PQ() # degree discount
    t = dict() # number of adjacent vertices that are in S
    d = dict() # degree of each vertex
    G_node_num = G.number_of_nodes() #the total number of nodes in the graph
    print(G_node_num)
    Attribute=dict()
    G_node_a = 0
    list_a=[]
    list_b=[]
    for u in G.nodes():
        Attribute[u]=G.node[u]['Attributes']
        if Attribute[u]=='a':
            G_node_a=G_node_a+1
            list_a.append(u)
    for u in G.nodes():
        Attribute[u]=G.node[u]['Attributes']
        if Attribute[u]=='b':
            list_b.append(u)
    print(list_a) #store nodes of category a in the list
    print(list_b) #store nodes of category b in the list
    print(G_node_a)  #number of nodes whose category is a
    G_node_b=G_node_num- G_node_a
    print(G_node_b)  #Number of nodes whose category is b
    a_b_pro=float(G_node_a)/float(G_node_b)
    print (a_b_pro)
    # print(Attribute)
    k_pro_a=float(G_node_a)/float(G_node_num)
    print(k_pro_a)   #Proportion of nodes whose category is a in a node

    # k_a=int(k*k_pro_a)+1
    k_a=int(k*k_pro_a)
    ka=k_a #The number of seed nodes with the label a passed to the propagation model
    print(k_a)
    k_b=k-k_a
    kb=k_b #The number of seed nodes with the label b passed to the propagation model
    print(k_b)
    print('\n')


    # initialize degree discount
    for u in G.nodes():
        d[u] = sum([G[u][v]['weight'] for v in G[u]]) # each edge adds degree 1
        # d[u] = len(G[u]) # each neighbor adds degree 1
        dd.add_task(u, -d[u]) # add degree of each node
        t[u] = 0


    # add vertices to S greedily
    # for i in range(k):
    while len(S)<k:
        u, priority = dd.pop_item() # extract node with maximal degree discount
        Attribute[u] = G.node[u]['Attributes']
        # print(Attribute[u])
        if Attribute[u]=='a':
            if k_a>0:
                S.append(u)
                k_a = k_a - 1
                # print(k_a)
            # else:
            #     i=i-1
            #     print(i)



        if Attribute[u] == 'b':
            if k_b>0:
                S.append(u)
                k_b = k_b - 1
                # print(k_b)
            # else:
            #     i=i-1
            #     print(i)

        for v in G[u]:
            if v not in S:
                t[v] += G[u][v]['weight'] # increase number of selected neighbors
                priority = d[v] - 2*t[v] - (d[v] - t[v])*t[v]*p[u, v] # discount of degree
                dd.add_task(v, -priority)
    return S,ka,kb

if __name__ == "__main__":
    import time
    start = time.time()

    G = nx.read_gpickle("Graph/test1.gpickle")

    print ("Read graph G")
    print (time.time() - start)

    d = "Graphdata/test1.txt"

    EdgePara = PageRank(d, 1)

    S = NewDiscount(G, 5, EdgePara)
    print (S)
    print (time.time() - start)

