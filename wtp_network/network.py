import networkx as nx


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
