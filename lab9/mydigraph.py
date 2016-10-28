import networkx as nx
import matplotlib.pyplot as plt #Used for plotting

#Create an empty graph
DG = nx.DiGraph()

#Adding edges to a graph
#Direction will be from source to destination
DG.add_edge('u','v')
DG.add_edge('u','x')
DG.add_edge('v','y')
DG.add_edge('x','v')
DG.add_edge('w','y')
DG.add_edge('w','z')
DG.add_edge('z','z')

#Print nodes of graph
print("Nodes of graph")
print(list(DG.nodes()))
#Print edges of graph
print('Edges of graph')
print(list(DG.edges()))
#Print traversal using BFS
print("Traversal using BFS")
print(list(nx.bfs_edges(DG, 'u')))
#Print the edge travesal using DFS
print("Edge traversal using DFS")
print(list(nx.edge_dfs(DG, 'u')))
#Print the graph

#Use layout for graph plot
pos = nx.spring_layout(DG)
#Plot nodes
nx.draw_networkx_nodes(DG, pos)
#Create node labels and plot labels
labels = {'u':'u', 'v':'v', 'w':'w', 'x':'x','y':'y','z':'z'}
nx.draw_networkx_labels(DG, pos, labels,font_size=16)
#Plot the edges
nx.draw_networkx_edges(DG, pos, arrows=True)
#Display the graph plot
plt.show()