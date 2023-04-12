# File: main.py
# Program utama dan visualisasi map

import folium
import graph as g

# PROGRAM UTAMA
# PROGRAM UTAMA
file_name = input("Masukkan nama file dalam format .txt: ")
g.initialize(file_name)

# print enter

# Daftar node
print("Daftar node:")
print('\n'.join(g.list_of_names))

# Input start node
start_node = ""
while start_node not in g.list_of_names:
    start_node = input("Masukkan start node: ")
    if start_node not in g.list_of_names:
        print("Node tidak valid, silakan coba lagi.")

# Input goal node
goal_node = ""
while goal_node not in g.list_of_names:
    goal_node = input("Masukkan goal node: ")
    if goal_node not in g.list_of_names:
        print("Node tidak valid, silakan coba lagi.")

# Pilihan algoritma pencarian
alg_choice = ""
while alg_choice not in ["1", "2"]:
    alg_choice = input("Pilih algoritma pencarian (1 untuk UCS, 2 untuk A*): ")
    if alg_choice not in ["1", "2"]:
        print("Pilihan tidak valid, silakan coba lagi.")
        
if alg_choice == "1":
    print("Hasil (UCS): ")
    solusiPath = g.ucs(start_node, goal_node)
elif alg_choice == "2":
    print("Hasil (A*): ")
    solusiPath = g.astar(start_node, goal_node)


list_path = g.path_coords(solusiPath)
g.print_route(solusiPath)

def color(name, solution):
    # kalau starting point
    if name == solution[0][0]:
        color = 'red'
    else:
        # kalau di path
        if name in solution[0]:
            color = 'green'
        else:
            color = 'blue'
    return color
    
map = folium.Map(location=[g.avg_lat(g.list_lat),g.avg_lon(g.list_lon)],zoom_start=15)

# make markers
for point in range(0, len(g.list_of_coordinates)):
    folium.Marker(g.list_of_coordinates[point], popup=g.list_of_names[point], icon=folium.Icon(color=color(g.list_of_names[point], solusiPath))).add_to(map)

# make path
fg = folium.FeatureGroup("Path")
line = folium.vector_layers.PolyLine(list_path, color='red', weight=10).add_to(fg)
fg.add_to(map)

# add title
# add title and metadata
title_html = '''
             <head>
             <meta charset="utf-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <meta name="description" content="Tucil 3 Strategi Algoritma">
             <meta name="author" content="13521016 dan 13521026">
             <title>Tucil 3 Strategi Algoritma</title>
             </head>
             <h3 align="center" style="font-size:15px"><b>Nama file: {}</b>
             </h3>
             '''.format(file_name)

map.get_root().html.add_child(folium.Element(title_html))

# add lintasan terpendek
solution = g.string_route(solusiPath)
htmlSolusi = '''
             <h3 align="center" style="font-size:16px"><b>{}</b>
             </h3>
             '''.format(solution)
map.get_root().html.add_child(folium.Element(htmlSolusi))
            
map.add_child(folium.LayerControl())
map.save(outfile='map.html')