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

    total_distance = 0
    print("Lintasan terpendek: ")
    for i in range(len(path)-1):
        node1 = path[i]
        node2 = path[i+1]
        edge = graph_data.get_edge(node1, node2)
        distance = sqrt((node2.lat - node1.lat)**2 + (node2.lon - node1.lon)**2)
        total_distance += distance
        print(f"{node1.name} - {node2.name}: {distance:.2f} km")
    print(f"Jarak lintasan terpendek: {total_distance:.2f} km")

    # Visualisasi dengan folium
    m = folium.Map(location=[start_node.lat, start_node.lon], zoom_start=15)

    # Tambahkan marker untuk setiap node
    for node in graph_data.nodes:
        if node == start_node:
            color = 'red'  # node awal diberi warna merah
        elif node == goal_node:
            color = 'green'  # node akhir diberi warna hijau
        else:
            color = 'blue'  # node lain diberi warna biru
        folium.Marker(
            location=[node.lat, node.lon],
            icon=folium.Icon(color=color)
        ).add_to(m)

    # Tambahkan polyline untuk lintasan terpendek
    for i in range(len(path)-1):
        node1 = path[i]
        node2 = path[i+1]
        folium.PolyLine(
            locations=[[node1.lat, node1.lon], [node2.lat, node2.lon]],
            color='blue'
        ).add_to(m)

    m.save("map.html")