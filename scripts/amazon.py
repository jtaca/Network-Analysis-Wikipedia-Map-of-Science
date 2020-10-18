import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import pickle


# GET CURRENT PATH
PATH = "C:/Users/danie/Desktop/Extras/CRC/Network-Analysis--Lisbon-Public-Transports/"
# sys.getPath() something like this...

def main():
    with open("amazon_graph", "rb") as f:
        G = pickle.load(f)


    print(len(G.nodes)) # 262111
    #print(len(G.edges)) # 899792

    #print(nx.average_clustering(G)) # 0.419780014607673
    #print(nx.average_degree_connectivity(G)) # ~10secs, dict with (probabilities?)
    #print(nx.average_neighbor_degree(G)) # ~10secs, dict with (values?)
    
    
    #print(nx.average_shortest_path_length(G)) #takes too long
    #print(nx.diameter(G)) # takes too long
    
    #print(nx.radius(G)) # 


    #print(G.nodes)
    '''
    Characterize the average degree 
    and degree distribution of the network. 
    Clustering coefficient and average path length. 

    Infer the importance (centrality) of each node (choose one relevant centrality measure for the chosen dataset and justify your choice).   
    Suggest a set of principles responsible for the self-organization and creation of such network topology/topologies
    '''


def create_graph():
    with open(PATH + "data/Amazon0302.txt", "r") as f:
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
NAME                                VALUE               CHECKED?

Nodes                               262111              Y
Edges 	                            1234877             Y
Nodes in largest WCC 	            262111 (1.000)          N
Edges in largest WCC 	            1234877 (1.000)         N
Nodes in largest SCC 	            241761 (0.922)          N
Edges in largest SCC 	            1131217 (0.916)         N
Average clustering coefficient 	    0.4198              Y
Number of triangles 	            717719                  N
Fraction of closed triangles 	    0.09339                 N
Diameter (longest shortest path) 	32                      N
90-percentile effective diameter 	11                      N
'''