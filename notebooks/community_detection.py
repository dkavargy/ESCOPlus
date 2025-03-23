# community_detection.py

import networkx as nx
import igraph as ig
import leidenalg
import pandas as pd


def nx_to_igraph(G):
    """
    Converts a NetworkX graph to an iGraph graph.
    """
    mapping = dict(zip(G.nodes(), range(len(G.nodes()))))
    reverse_mapping = {v: k for k, v in mapping.items()}

    g = ig.Graph()
    g.add_vertices(len(mapping))
    g.add_edges([(mapping[u], mapping[v]) for u, v in G.edges()])

    # Optional: add weights if they exist
    if 'weight' in list(G.edges(data=True))[0][2]:
        g.es['weight'] = [G[u][v]['weight'] for u, v in G.edges()]

    return g, reverse_mapping


def run_leiden_community_detection(G_nx, resolution=1.0):
    """
    Applies the Leiden algorithm to a NetworkX graph and returns communities.
    """
    g_ig, reverse_mapping = nx_to_igraph(G_nx)
    partition = leidenalg.find_partition(
        g_ig,
        leidenalg.RBConfigurationVertexPartition,
        resolution_parameter=resolution,
        weights='weight' if 'weight' in g_ig.es.attributes() else None
    )

    communities = {}
    for community_id, community in enumerate(partition):
        for node_index in community:
            node_name = reverse_mapping[node_index]
            communities[node_name] = community_id

    return communities


def assign_communities_to_nodes(G_nx, resolution=1.0):
    """
    Adds community IDs as node attributes to the original NetworkX graph.
    """
    communities = run_leiden_community_detection(G_nx, resolution)
    nx.set_node_attributes(G_nx, communities, "community")
    return G_nx


# Example usage
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Example graph
    G = nx.karate_club_graph()
    G = assign_communities_to_nodes(G)

    # Visualize
    colors = [G.nodes[n]['community'] for n in G.nodes()]
    nx.draw(G, with_labels=True, node_color=colors, cmap=plt.cm.Set3)
    plt.show()
