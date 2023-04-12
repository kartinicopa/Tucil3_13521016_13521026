import graph
import folium
import os

def get_filename():
    while True:
        filename = input("Masukkan nama file: ")
        try:
            graph_data = graph.read_file(filename)
            return filename, graph_data
        except FileNotFoundError:
            print(f"File {filename} tidak ditemukan.")

def get_algorithm():
    while True:
        algorithm = input("Masukkan algoritma (A* atau UCS): ")
        if algorithm in ["A*", "UCS"]:
            return algorithm
        print("Algoritma tidak valid.")

def get_node_name(prompt, nodes):
    while True:
        node_name = input(prompt)
        if node_name in nodes:
            return node_name
        print("Nama node tidak valid.")

def main():
    filename, graph_data = get_filename()
    algorithm = get_algorithm()

    nodes = [node.name for node in graph_data.nodes]

    while True:
        start_node_name = get_node_name("Masukkan nama node awal: ", nodes)
        goal_node_name = get_node_name("Masukkan nama node tujuan: ", nodes)

        start_node = None
        goal_node = None

        for node in graph_data.nodes:
            if node.name == start_node_name:
                start_node = node
            elif node.name == goal_node_name:
                goal_node = node

        if not start_node or not goal_node:
            print("Node awal atau tujuan tidak ditemukan.")
        else:
            break

    if algorithm == "A*":
        path, tot_cost = graph.A_star(start_node, goal_node)
    elif algorithm == "UCS":
        path, tot_cost = graph.ucs(start_node, goal_node)

    print(f"Panjang jarak lintasan terpendek: {tot_cost} meter")
    print("Lintasan terpendek: ")
    for i in range(len(path)-1):
            print(path[i].name, "->", end=" ")
    print(path[-1].name)

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

    map_filename = os.path.splitext(filename)[0] + ".html"
    m.save(map_filename)

if __name__ == "__main__":
    main()
