
import heapq
heuristic = {
        'A': 46,
        'B': 39,
        'C': 41,
        'D': 29,
        'E': 38,
        'F': 17,
        'G': 6,
        'H':0
    }
graph_b = {

          'A' : [('E', 25), ('D', 30), ('B', 22)],
          'B' : [('D', 11), ('C', 22)],
          'D' : [('F', 10)],
          'E' : [('F', 25), ('G', 40)],
          'F' : [('G', 12)],
          'C' : [],
          'G' : [('H', 6)],
          'H' : []
    }
   
def a_star_search(graph, start, goal, h):
    open_set = [(h[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None
# Example usage
start = 'A'
goal = 'H'
path = a_star_search(graph_b, start, goal, heuristic)
print("A* Path from A to H:", path)


