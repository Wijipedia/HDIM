import json
import networkx as nx
from networkx.readwrite import json_graph
from simple_net_gen import SimpleNetGen
import matplotlib.pyplot as plt
from base import NetGen

# G = nx.generators.directed.scale_free_graph(30, 0.33, 0.33, 0.34, 1, 1)
G = NetGen(1, 0.8, 0.33, 0.33, 0.34, 1, 1)
# print(len(G.generate_full_graph()))
# nx.draw(G)
nx.draw(G.generate_full_graph())
plt.show()

# with open('networkdata.json', 'w') as outfile1:
    # outfile1.write(json.dumps(json_graph.node_link_data(G)))

# G = SimpleNetGen(20, 0.8, 1.0 / 3, 1.0 / 3, 1.0 / 3, 1, 1)
# nx.draw(G)
# plt.show()

# with open('networkdata.json', 'w') as outfile1:
#     outfile1.write(json.dumps(G, default=str))
    # outfile1.write(json.dumps(G,cls=MyEncoder,indent=4))
    # outfile1.write(json.dumps(G))