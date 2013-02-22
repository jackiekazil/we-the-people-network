import matplotlib.pyplot as plt
import networkx as nx

def trim_degrees(g, degree=1):
    g2=g.copy() 
    d=nx.degree(g2)
    [g2.remove_node(n) for n in g2.nodes() if d[n]<=degree] 
    return g2

def add_edge_or_weight(G, f, t):
    '''
    This function adds a new edge value to the list or increases the weight
    of an existing value.
    '''
    if G.has_edge(f,t):
        G[f][t]['weight']+=1
    else:
        G.add_edge(f,t,weight=1)
    return G

def create_edgelist(node_edgelist):

    # Create graph
    G = nx.Graph()

    for f in node_edgelist:
        for t in node_edgelist:
            # Make sure we are equal to ourself
            if t != f:
                # Make sure we don't connect to our own node
                if f[0] != t[0]:
                    if f[1] == t[1]:
                        add_edge_or_weight(G, f[0], t[0])

    return G


def graph_degree(G):

    deg = nx.degree(G)
    h=plt.hist(deg.values(),100)
    plt.loglog(h[1][1:],h[0])
    plt.savefig('graph3.png')

def visualize_graph(G, degree=1):

    #print len(G.nodes())
    #print len(G.edges())
    # Let's shave some weak ties to get to the core.

    # Let's shave some weak ties to get to the core.
    neighbors = []
    for node in G.nodes():
        neighbors.append(len(G.neighbors(node)))

    print sorted(neighbors)

    g2 = trim_degrees(G, degree)

    print len(G)
    print len(g2)

    #graph_degree(G)

    #print len(G.nodes())
    #print len(G.edges())

    ##Find Structural Holes
    # from hw2.network_analysis_utils.structural_holes import *
    # print ego_density(G)

    pos=nx.spring_layout(G,iterations=100)
    plt.figure(1,figsize=(10,10))
    nx.draw_networkx_nodes(G,pos,node_size=40,alpha=0.6,node_color='g')
    nx.draw_networkx_edges(G,pos,alpha=0.2)
    plt.show()

    pos=nx.spring_layout(G,iterations=1000)
    plt.figure(1,figsize=(10,10))
    nx.draw_networkx_nodes(g2,pos,node_size=75,alpha=0.7,node_color='g')
    nx.draw_networkx_edges(g2,pos,alpha=0.05)
    plt.show()

##    # Create parititions with hierarchical clustering partitions=hc.create_hc(H)
#
#    X=nx.connected_component_subgraphs(G)[0]
##    #pos=nx.spring_layout(G,iterations=100)
#    pos=nx.spring_layout(X)
##
#    # pos is dictionary of plot points for for graph
#    # exmaple: 'HEALTHY HABITS': array([ 0.28358263,  0.29900914]), 'HYDE LEADERSHIP PCS WASH': array([ 0.39406232,  0.11402111]),
##
#    plt.figure(1,figsize=(10,10))
#    nx.draw_networkx_nodes(X,pos,node_size=20,alpha=0.6,node_color='g')
#    nx.draw_networkx_edges(X,pos,alpha=0.2)
##
##
##    #nx.draw_networkx_labels(X,pos,alpha=0.5)
##    #plt.axis('equal')
#    plt.axis('off')
###    plt.show()
#    plt.savefig('graphX.png')
