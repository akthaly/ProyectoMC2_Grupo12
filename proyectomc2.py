import networkx as nx  # Importar la librería de NetworkX y sirve para crear y manipular grafos
import tkinter as tk # Importar la librería de Tkinter y sirve para crear la interfaz gráfica
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg     # Importar la clase FigureCanvasTkAgg y sirve para mostrar la figura en una ventana de Tkinter
from matplotlib.figure import Figure    # Importar la clase Figure y sirve para crear una figura

G = nx.Graph() # Crear un grafo vacío
root = tk.Tk() # Crear una ventana de Tkinter
root.title("Algoritmos de busqueda en Grafos") # Asignar un título a la ventana

origin_label = tk.Label(root, text="Vertice inicial para la búsqueda:") # Crear una etiqueta para el campo de entrada de vértices
origin_label.pack() # Empaquetar la etiqueta en la ventana

vertex_entry = tk.Entry(root) # Crear un campo de entrada para el vértice
vertex_entry.pack() # Empaquetar el campo de entrada en la ventana

edge1_label = tk.Label(root, text="vertice origen:") # Crear una etiqueta para el campo de entrada de aristas
edge1_label.pack() # Empaquetar la etiqueta en la ventana

edge_entry_1 = tk.Entry(root) # Crear un campo de entrada para las aristas
edge_entry_1.pack() # Empaquetar el campo de entrada en la ventana

edge2_label = tk.Label(root, text="Vertice destino:") # Crear una etiqueta para el campo de entrada de aristas
edge2_label.pack() # Empaquetar la etiqueta en la ventana

edge_entry_2 = tk.Entry(root) # Crear un campo de entrada para las aristas
edge_entry_2.pack() # Empaquetar el campo de entrada en la ventana

def add_edge(): # Crear una función para agregar aristas
    G.add_edge(edge_entry_1.get(), edge_entry_2.get()) # Agregar una arista al grafo
    draw_graph() # Dibujar el grafo

add_edge_button = tk.Button(root, text="Agregar arista", command=add_edge) # Crear un botón para agregar aristas
add_edge_button.pack() # Empaquetar el botón en la ventana

print_info_button = tk.Button(root, text="Info. de datos agregados", command=lambda:print("Numero de vertices:",G.number_of_nodes(),"\nNumero de aristas:",G.number_of_edges())) # Crear un botón para imprimir información de los datos agregados
print_info_button.pack() # Empaquetar el botón en la ventana

figure = Figure(figsize=(5,5)) # Crear una figura
ax = figure.add_subplot(111) # Agregar un subplot a la figura
canvas = FigureCanvasTkAgg(figure, root) # Crear un lienzo para mostrar la figura en la ventana
canvas.get_tk_widget().pack() # Empaquetar el lienzo en la ventana

def draw_graph(traversal_nodes=None, traversal_edges=None): # Crear una función para dibujar el grafo
    ax.clear() # Limpiar el subplot
    if traversal_edges: # Si hay aristas de recorrido
        pos = nx.spring_layout(G) # Asignar posiciones a los nodos
        nx.draw(G, pos=pos, ax=ax, with_labels=True) # Dibujar el grafo
        nx.draw_networkx_edges(G, pos=pos, edgelist=traversal_edges, edge_color='r', ax=ax) # Dibujar las aristas de recorrido
        nx.draw_networkx_nodes(G, pos=pos, nodelist=traversal_nodes, node_color='r', ax=ax) # Dibujar los nodos de recorrido
    else:
        nx.draw(G, ax=ax, with_labels=True) # Dibujar el grafo
    canvas.draw() # Dibujar el lienzo que es la figura en la ventana

def show_traversal(traversal_func): # Crear una función para mostrar el recorrido
    source_node = vertex_entry.get() # Obtener el vértice inicial
    traversal_nodes = [] # Crear una lista para almacenar los nodos visitados
    traversal_edges = [] # Crear una lista para almacenar las aristas visitadas
    if traversal_func== nx.bfs_edges: # Si la función de recorrido es la de búsqueda en anchura
        traversal_edges = list(traversal_func(G, source=source_node)) # Realizar el recorrido en anchura
        traversal_nodes = [source_node] + [v for u, v in traversal_edges] # Almacenar los nodos visitados
    elif traversal_func == nx.dfs_edges: # Si la función de recorrido es la de búsqueda en profundidad
        traversal_edges = list(traversal_func(G, source=source_node)) # Realizar el recorrido en profundidad
        traversal_nodes = [source_node] + [v for u, v in traversal_edges] # Almacenar los nodos visitados
    print("Orden de visita durante la búsqueda:", traversal_nodes) # Imprimir el orden de visita
    draw_graph(traversal_nodes, traversal_edges) # Dibujar el grafo con los nodos y aristas visitados
    canvas.draw() # Dibujar el lienzo que es la figura en la ventana

bfs_button = tk.Button(root, text="Busqueda en Anchura", command=lambda: show_traversal(nx.bfs_edges)) # Crear un botón para la búsqueda en anchura
bfs_button.pack() # Empaquetar el botón en la ventana

dfs_button = tk.Button(root, text="Busqueda en Profundidad", command=lambda: show_traversal(nx.dfs_edges)) # Crear un botón para la búsqueda en profundidad
dfs_button.pack() # Empaquetar el botón en la ventana
def Limpiar_todo():     # Crear una función para limpiar todo
    G.clear()   # Limpiar el grafo
    vertex_entry.delete(0)   # Limpiar el campo de entrada de vértices
    edge_entry_1.delete(0)  # Limpiar el campo de entrada de aristas
    edge_entry_2.delete(0)  # Limpiar el campo de entrada de aristas
    draw_graph() # Dibujar el grafo
    
borrar_button = tk.Button(root, text= "Limpiar todo", command= Limpiar_todo) # Crear un botón para limpiar todo
borrar_button.pack() # Empaquetar el botón en la ventana

root.mainloop() # Mostrar la ventana
