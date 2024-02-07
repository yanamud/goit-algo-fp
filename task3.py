import heapq

import networkx as nx
import pylab

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # шукаємо вершину з найкоротшим шляхом
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # якщо новий шлях кращий за раніше знайдений
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    'R1': {'R2': 4, 'R3': 3, 'R4': 6},
    'R2': {'R1': 4, 'R3': 4, 'R8': 4},
    'R3': {'R1': 3, 'R2': 4, 'R6': 3, 'R7': 3},
    'R4': {'R1': 6,'R5': 6, 'R6': 3},
    'R5': {'R4': 6, 'R11': 3, 'R12': 6},
    'R6': {'R3': 3, 'R4': 3, 'R7': 5, 'R11': 3},
    'R7': {'R3': 3, 'R6': 5, 'R8': 5, 'R10': 3},
    'R8': {'R2': 4, 'R7': 5, 'R9': 3},
    'R9': {'R8': 3, 'R10': 5, 'R16': 3},
    'R10': {'R7': 3, 'R9': 5, 'R14': 3, 'R15': 3},
    'R11': {'R5': 3, 'R6': 3, 'R12': 3, 'R14': 3},
    'R12': {'R5': 6, 'R11': 3, 'R13': 5},
    'R13': {'R12': 5, 'R14': 6, 'R19': 5},
    'R14': {'R10': 3, 'R11': 3, 'R13': 6, 'R18': 3},
    'R15': {'R10': 3, 'R16': 6, 'R17': 4, 'R18': 3},
    'R16': {'R9': 3, 'R15': 6, 'R17': 3},
    'R17': {'R15': 4, 'R16': 3, 'R20': 2},
    'R18': {'R14': 3, 'R15': 3, 'R19': 4, 'R20': 3},
    'R19': {'R13': 5, 'R18': 4, 'R20': 4},
    'R20': {'R17': 2, 'R18': 3, 'R19': 4}
}

G = nx.DiGraph(graph)

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='R1')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='R1')

# виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів
print('\nнайкоротший шляхи від початкового вузла до всіх інших вузлів (перелік вузлів)')

sorted_paths = dict(sorted(shortest_paths.items()))
for top, way in shortest_paths.items():
        print(f"{top} | {way}")


print('\nдовжина найкоротшого шляху від початкового вузла до всіх інших вузлів (кількість вузлів)')
print(shortest_path_lengths) 

print('\nдовжина найкоротшого шляху від початкового вузла до всіх інших вузлів (сума всіх ваг вузлів)')
print(dijkstra(graph, 'R1'))

# візуалізація графа
pylab.figure(figsize=(8, 8))
nx.draw_networkx(G, with_labels=True)
pylab.show()