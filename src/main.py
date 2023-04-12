import graph
import folium

def main():
    filename = input("Masukkan nama file: ")
    algorithm = input("Masukkan algoritma (A* atau UCS): ")

    graph_data = graph.read_file(filename)

    start_node_name = input("Masukkan nama node awal: ")
    goal_node_name = input("Masukkan nama node tujuan: ")

    start_node = None
    goal_node = None

    for node in graph_data.nodes:
        if node.name == start_node_name:
            start_node = node
        elif node.name == goal_node_name:
            goal_node = node

    if algorithm == "A*":
        path = graph.A_star(start_node, goal_node)
    elif algorithm == "UCS":
        path = graph.ucs(start_node, goal_node)

    print("Lintasan terpendek: ")
    for node in path:
        print(node.name)

    # Visualisasi dengan folium
    m = folium.Map(location=[start_node.lat, start_node.lon], zoom_start=15)

    folium.Marker(
        location=[start_node.lat, start_node.lon],
        icon=folium.Icon(color='green')
    ).add_to(m)

    folium.Marker(
        location=[goal_node.lat, goal_node.lon],
        icon=folium.Icon(color='red')
    ).add_to(m)

    for i in range(len(path)-1):
        node1 = path[i]
        node2 = path[i+1]
        folium.PolyLine(
            locations=[[node1.lat, node1.lon], [node2.lat, node2.lon]],
            color='blue'
        ).add_to(m)
        
        folium.Marker(
            location=[node1.lat, node1.lon],
            icon=folium.Icon(color='blue')
        ).add_to(m)

        folium.Marker(
            location=[goal_node.lat, goal_node.lon],
            icon=folium.Icon(color='green')
        ).add_to(m)

    m.save("map.html")
    
if __name__ == "__main__":
    main()