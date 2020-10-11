import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

PATH = "C:/Users/danie/Desktop/Extras/CRC/Network-Analysis--Lisbon-Public-Transports/"

#parse shape.txt into a vector
def main():
    with open(PATH + "data/cp/shapes.txt", "r") as f:
        shape_data = f.read()

    vec_shape = shape_data.split("\n")
    for i in range(len(vec_shape)):
        vec_shape[i] = vec_shape[i].split(",")
    
    del vec_shape[0]
    del vec_shape[-1]


    with open(PATH + "data/cp/stops.txt", "r") as f:
        stops_data = f.read()

    vec_stops = stops_data.split("\n")
    for i in range(len(vec_stops)):
        vec_stops[i] = vec_stops[i].split(",")

    del vec_stops[0]
    del vec_stops[-1]

    some = 1
    for shape in vec_shape:
        for stop in vec_stops:
            if(shape[1] == stop[4] and shape[2] == stop[5]):
                shape.append(stop[2])
    
    #print(vec_shape)


    G = nx.Graph()

    for shape in vec_shape:
        if(shape[0] == "401"):
                G.add_nodes_from([ (shape[3], {"name": shape[5], "x": shape[1], "y": shape[2]}) ])
        else:
            break
    
    nodes = list(G.nodes)
    for i in range(len(nodes)-1):
        G.add_edge(nodes[i], nodes[i+1])

    nodes_dic = dict(G.nodes)
    print(nodes_dic["1"])
    print(G.edges)

    
    plt.subplot(121)

    nx.draw(G, with_labels=True, font_weight='bold')

    plt.show()
    '''

    Go = ox.graph.graph_from_point((38.70085,-9.41792))

    ox.plot.plot_graph(Go, bbox=(38.70085+0.00300, 38.70085-0.00300, -9.41792+0.00300, -9.41792-0.00300))
    '''






main()
