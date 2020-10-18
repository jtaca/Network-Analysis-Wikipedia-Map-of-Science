import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import math

# GET CURRENT PATH
PATH = "C:/Users/danie/Desktop/Extras/CRC/Network-Analysis--Lisbon-Public-Transports/"

#parse shape.txt into a vector
def main():
    meios_de_transporte = ["carris", "cp", "fertagus", "metro", "rodlisboa", "soflusa", "sulfertagus", "transtejo", "tst"]

    graphs = []
    for meio in meios_de_transporte[3:3]:
        graphs.append(createGraph(meio))

    graph = createGraph("metro")

    draw_graph(graph)


def createGraph(name):
    with open(PATH + "data/" + name + "/shapes.txt", "r", encoding="utf8") as f:
        shape_data = f.read()

    vec_shape = shape_data.split("\n")
    for i in range(len(vec_shape)):
        vec_shape[i] = vec_shape[i].split(",")
    
    del vec_shape[0]
    del vec_shape[-1]


    with open(PATH + "data/" + name + "/stops.txt", "r", encoding="utf8") as f:
        stops_data = f.read()

    vec_stops = stops_data.split("\n")
    for i in range(len(vec_stops)):
        vec_stops[i] = vec_stops[i].split(",")

    del vec_stops[0]
    del vec_stops[-1]


    for shape in vec_shape:
        isAppended = False
        for stop in vec_stops:
            if(shape[1] == stop[4] and shape[2] == stop[5] and not isAppended):
                isAppended = True
                shape.append(stop[2])
        
        if(not isAppended):
            shape.append("XXXXXXXXXXXXXXXXXXX")
        



    with open(PATH + "data/" + name + "/joined.txt", "w", encoding="utf8") as f:
        for shape in vec_shape:
            for component in shape:
                f.write(component + " | ")
            f.write("\n")
        
    

    #['401', '38.70085', '-9.41792', '1', '', 'Cascais']
    G = nx.Graph()

    for shape in vec_shape:
        route = int(shape[0])
        x = shape[1]
        y = shape[2]
        id = int(shape[3])
        location = shape[5]
        G.add_nodes_from([ (location, {"location": location, "route": route, "id": id, "x": x, "y": y}) ])
    

    nodes = dict(G.nodes)
    # O(N^2) very bad
    for k, v in nodes.items():
        for k2, v2 in nodes.items():
            if(v["route"] == v2["route"] and (v["id"] == v2["id"]+1 or v["id"] == v2["id"]-1)):
                G.add_edge(k, k2)

    #print(G.edges)
    return G

    


def calcDistance(lat1, lon1, lat2, lon2):
    R = 6371e3 # metres
    x1 = lat1 * math.pi/180 # x, y in radians
    x2 = lat2 * math.pi/180
    dx = (lat2-lat1) * math.pi/180
    dy = (lon2-lon1) * math.pi/180

    a = math.sin(dx/2) * math.sin(dx/2) + math.cos(x1) * math.cos(x2) * math.sin(dy/2) * math.sin(dy/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c # in metres


def draw_graph(graph):
    plt.figure(figsize=(18,18))

    #for graph in graphs:
    #    nx.draw(graph, with_labels=True, font_weight='bold')

    nx.draw_networkx(graph, with_labels=True, font_weight='bold')
    plt.show()

main()