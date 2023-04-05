# Langkah 1: Mengumpulkan data graf (matriks ketetanggaan berbobot)
# Data graf dapat diambil dari sumber terpercaya seperti pemerintah daerah atau Google Maps API

# Langkah 2: Membuat fungsi untuk membaca data graf dari file input
def read_graph(filename):
    graph = []
    with open(filename) as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            graph.append(row)
    return graph

# Langkah 3: Membuat fungsi untuk menampilkan peta/graf
# Fungsi ini dapat menggunakan library grafik seperti Matplotlib atau Google Maps API (jika bonus ingin dicapai)

# Langkah 4: Membuat fungsi untuk menerima input simpul asal dan simpul tujuan
def get_source_dest():
    source = int(input("Masukkan simpul asal: "))
    dest = int(input("Masukkan simpul tujuan: "))
    return source, dest

# Langkah 5: Membuat fungsi untuk mengimplementasikan algoritma UCS dan A*
# Implementasi algoritma UCS dan A* akan tergantung pada struktur data graf yang digunakan
# Contoh implementasi algoritma UCS dan A* pada matriks ketetanggaan berbobot:
def ucs(graph, source, dest):
    queue = [(0, source, [])]
    visited = set()

    while queue:
        (cost, current_node, path) = queue.pop(0)
        if current_node == dest:
            return (cost, path + [current_node])
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, neighbor_cost in enumerate(graph[current_node]):
            if neighbor_cost == 0 or neighbor in visited:
                continue
            queue.append((cost + neighbor_cost, neighbor, path + [current_node]))

def heuristic(node, dest):
    x1, y1 = node
    x2, y2 = dest
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def a_star(graph, source, dest):
    queue = [(0, source, [])]
    visited = set()

    while queue:
        (cost, current_node, path) = queue.pop(0)
        if current_node == dest:
            return (cost, path + [current_node])
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, neighbor_cost in enumerate(graph[current_node]):
            if neighbor_cost == 0 or neighbor in visited:
                continue
            priority = cost + neighbor_cost + heuristic(neighbor, dest)
            queue.append((priority, neighbor, path + [current_node]))

# Langkah 6: Membuat fungsi untuk menampilkan lintasan terpendek di peta/graf
# Fungsi ini akan menandai jalan-jalan yang menyatakan lintasan terpendek dengan warna merah

# Langkah 7: Menggabungkan semua fungsi yang telah dibuat menjadi program utama
# Program ini dapat ber

# Contoh program utama command line
if __name__ == '__main__':
    filename = 'graph.txt'
    graph = read_graph(filename)
    source, dest = get_source_dest()
    cost, path = ucs(graph, source, dest)
    print("Lintasan terpendek: ", path)
    print("Jarak lintasan terpendek: ", cost)