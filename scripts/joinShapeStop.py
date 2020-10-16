import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# GET CURRENT PATH
PATH = "C:/Users/danie/Desktop/Extras/CRC/Network-Analysis--Lisbon-Public-Transports/"

#parse shape.txt into a vector
def main():
    with open(PATH + "data/metro/shapes.txt", "r", encoding="utf8") as f:
        shape_data = f.read()

    vec_shape = shape_data.split("\n")
    for i in range(len(vec_shape)):
        vec_shape[i] = vec_shape[i].split(",")
    
    del vec_shape[0]
    del vec_shape[-1]


    with open(PATH + "data/metro/stops.txt", "r", encoding="utf8") as f:
        stops_data = f.read()

    vec_stops = stops_data.split("\n")
    for i in range(len(vec_stops)):
        vec_stops[i] = vec_stops[i].split(",")

    del vec_stops[0]
    del vec_stops[-1]


    for shape in vec_shape:
        for stop in vec_stops:
            if(shape[1] == stop[4] and shape[2] == stop[5]):
                shape.append(stop[2])
    

    #['401', '38.70085', '-9.41792', '1', '', 'Cascais']

    
    G = nx.Graph()

    for shape in vec_shape:
        route = int(shape[0])
        x = shape[1]
        y = shape[2]
        id = int(shape[3])
        location = shape[5]
        G.add_nodes_from([ (x + ":" + y, {"location": location, "route": route, "id": id, "x": x, "y": y}) ])
    

    nodes = dict(G.nodes)
    # O(N^2) very bad
    for k, v in nodes.items():
        for k2, v2 in nodes.items():
            if(v["route"] == v2["route"] and (v["id"] == v2["id"]+1 or v["id"] == v2["id"]-1)):
                G.add_edge(k, k2)

    print(G.edges)

    
    plt.subplot(121)

    nx.draw(G, with_labels=True, font_weight='bold')

    plt.show()
    '''
    place = {'city'   : 'Lisbon',
            'country': 'Portugal'}
    G = ox.graph_from_place(place, network_type='drive', truncate_by_edge=True)
    fig, ax = ox.plot_graph(G, figsize=(10, 10), node_size=0, edge_color='y', edge_linewidth=0.2)
    

    Go = ox.graph.graph_from_point((38.70085,-9.41792))

    ox.plot.plot_graph(Go, bbox=(38.70085+0.00300, 38.70085-0.00300, -9.41792+0.00300, -9.41792-0.00300))
    '''






main()
