import networkx as nx
import matplotlib.pyplot as plt #Used for plotting

#Create an empty graph
G = nx.Graph()

#Adding edges to a graph
#Direction will be from source to destination
G.add_edge('u','v')
G.add_edge('u','x')
G.add_edge('v','y')
G.add_edge('x','v')
G.add_edge('w','y')
G.add_edge('w','z')
G.add_edge('z','z')

#Print nodes of graph
print("Nodes of graph")
print(list(G.nodes()))
#Print edges of graph
print('Edges of graph')
print(list(G.edges()))
#Print traversal using BFS
print("Traversal using BFS")
print(list(nx.bfs_edges(G, 'u')))
#Print the edge travesal using DFS
print("Edge traversal using DFS")
print(list(nx.edge_dfs(G, 'u')))
#Print the graph

#Use layout for graph plot
pos = nx.spring_layout(G)
#Plot nodes
nx.draw_networkx_nodes(G, pos)
#Create node labels and plot labels
labels = {'u':'u', 'v':'v', 'w':'w', 'x':'x','y':'y','z':'z'}
nx.draw_networkx_labels(G, pos, labels,font_size=16)
#Plot the edges
nx.draw_networkx_edges(G, pos, arrows=True)
#Display the graph plot
plt.show()