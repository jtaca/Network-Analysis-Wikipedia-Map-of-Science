import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import pickle
import pathlib


# GET CURRENT PATH
PATH = pathlib.Path().absolute()

def main():
    with open(str(PATH) + "\\amazon_graph", "rb") as f:
        G = pickle.load(f)


    #Z (Characterize the Average Degree)                                     Z = 2E/N undirected graph | Z = E/N directed graph
    
    
    # P(k) (Characterize the Degree Distribution)
    #print(nx.degree_histogram(G))

    # What does nx.degree_assortativity_coefficient mean?
    #for i in ["out", "in"]:
    #    for j in ["out", "in"]:
    #           print(f'x={i:<3}  y={j:<3} => {nx.degree_assortativity_coefficient(G, x=i, y=j, weight=None, nodes=None)}')


    #print(len(G.nodes)) # 262111
    #print(len(G.edges)) # 899792
    #print(nx.average_clustering(G)) # 0.419780014607673

    '''
    sum = 0
    dict_average_degree = nx.average_degree_connectivity(G) # P(k) | ~10secs, dict with (probabilities?), do a graph, probably with log scale or power scale
    for i in range(len(dict_average_degree)):
        if(i in dict_average_degree):
            sum += dict_average_degree[i]
            print(f'{i} : {dict_average_degree[i]}')
    print(sum/len(dict_average_degree))
    print(2*len(G.edges)/len(G.nodes))
    '''

    #print(nx.average_neighbor_degree(G)) # ~10secs, dict with (values?), do a graph, probably with log scale or power scale

    #centrality_measures(G)
    #too_long_to_run(G)



    return 0


def centrality_measures(G):
    print(nx.degree_centrality(G))
    print(nx.in_degree_centrality(G))
    print(nx.out_degree_centrality(G))


    
    return

    
def too_long_to_run(G):
    # APL, takes too long
    print(nx.average_shortest_path_length(G))

    # Diameter, takes too long
    print(nx.diameter(G))

    # Radius, takes too long
    print(nx.radius(G))

    return


def create_graph():
    with open(PATH + "/../data/Amazon0302.txt", "r") as f:
        amazon_data = f.read()

    amazon_list = amazon_data.split("\n")

    del amazon_list[:4]
    del amazon_list[len(amazon_list)-1]
    
    for i in range(len(amazon_list)):
        amazon_list[i] = (int(amazon_list[i].split("\t")[0]), int(amazon_list[i].split("\t")[1]))
    
    G = nx.Graph()

    G.add_edges_from(amazon_list)

    # Serialization of G
    with open("amazon_graph", "wb") as f:
        pickle.dump(G, f)
    
    return G

main()






'''
NAME                                VALUE               CONFIRMED?      Notes:

Nodes                               262111              Y               .
Edges 	                            1234877             Y               .
Nodes in largest WCC 	            262111 (1.000)          N           .
Edges in largest WCC 	            1234877 (1.000)         N           .
Nodes in largest SCC 	            241761 (0.922)          N           .
Edges in largest SCC 	            1131217 (0.916)         N           .
Average clustering coefficient 	    0.4198              Y               .
Number of triangles 	            717719                  N           .
Fraction of closed triangles 	    0.09339                 N           .
Diameter (longest shortest path) 	32                      N           Takes too long
90-percentile effective diameter 	11                      N           .


THINGS TO ADD
Centrality (various types of Centrality, we only need to choose one but we need to justify why we choosed one. Could be by trying a few or just a nice explanation)
Z (Characterize the Average Degree)                                     Z = 2E/N undirected graph | Z = E/N directed graph
P(k) (Characterize the Degree Distribution)


CC (Clustering Coefficient)         
APL (Average Path Length)                                               Takes too long


    Infer the importance (centrality) of each node (choose one relevant centrality measure for the chosen dataset and justify your choice).   
    Suggest a set of principles responsible for the self-organization and creation of such network topology/topologies
'''