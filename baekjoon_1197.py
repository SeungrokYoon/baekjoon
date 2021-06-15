#Prim's MST

import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline


class Graph:
    def __init__(self, n):
        self.V = n
        self.adj_list = defaultdict(list)

    def addEdge(self, u, v, w):
        # undirected니까
        self.adj_list[u].append((w, v))
        self.adj_list[v].append((w, u))

    def prim(self):
        cost=0
        visited=set()
        visited.add(1)
        heap =[ _ for _ in self.adj_list[1]]
        heapq.heapify(heap)
        while heap and len(visited)!= (self.V):
            dist, neighbor= heapq.heappop(heap)

            if neighbor not in visited:
                print(neighbor)
                visited.add(neighbor)
                cost+=dist
                for new_dist, new_neighbor in self.adj_list[neighbor]:
                    if new_neighbor not in visited:
                        heapq.heappush(heap,(new_dist, new_neighbor))

        return cost

#n정점개수 m간선개수
n,m = map(int, (input().rstrip().split()))
graph = Graph(n)
for _ in range(m):
    u, v, w = list(map(int, input().rstrip().split()))
    graph.addEdge(u, v, w)

print(graph.prim())
