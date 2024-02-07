import uuid

import heapq
import networkx as nx
import matplotlib.pyplot as plt
import pylab

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

nodes = [] # для створення cписку вузлів
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    nodes.append(tree.nodes(data=True))

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


list = [] # для виведення списку вузлів
def print_heap():
    item  = str(nodes).split(',')
    for el in item:
        if 'label' in el:      
            list.append(int(str(el).split(':')[1].split('}')[0]))
    print("\nСписок вузлів наданого дерева:")
    print(list)

    # Сортування купи
    data = list
    heapq.heapify(data)
    print('\nСтворення бінарної купи на базі наданого дерева:')
    print(data) 

    G = nx.DiGraph()

    G.add_nodes_from(data)
    for i in range(int(len(data)/2)):
        G.add_edge(data[i], data[2*i + 1])
        if 2*i + 2 < len(data):
            G.add_edge(data[i], data[i*2 + 2])          


    pylab.figure(figsize=(4, 4))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos, node_size=200, arrows=True, arrowsize=30, node_color="skyblue")
    pylab.show()

    # візуалізація купи
    print('\nВізуалізація бінарної купи:')

    cnt=0 
    order=[' '*(i*2) for i in range(int(len(data)/2))]
    order[0]=' '
    if len(data)== 1:
            print(data)
    print(order[-1],end='    ')
    try:
        for i in range(int(len(data)/2)):
            for j in order[i]:
                print(order[-i], data[cnt],end='  ')
                cnt+=1
            print('\n')
    except:
        pass

print_heap()
