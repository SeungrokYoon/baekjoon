"""
백준 18405 - 경쟁적 전염
개념: DFS/BFS
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = []
#그래프작성
for _ in range(N):
    graph.append([0]+list(map(int, input().split())))

visited=  [[ 0 for _ in range(n+1)] for _ in range(n+1)]

#초와 목표 좌표 입력받기
S ,X ,Y = map(int, input().split())


print(graph)
print(visited)
for t in range(1,K+1):
    for x in range(1, N+1):
        for y in range(1, N+1):
            if graph[x][y] ==k:
                bfs(graph, (x,y))




def bfs(graph,start):
    dx= [0,0,-1,1]
    dy= [-1,1,0,0]
    x= start[0]
    y= start[1]
    q= deque((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx= dx[i] +x
            ny= dy[i] +y
            if nx<1 or ny<1 or nx>N or ny>N:
                continue
            if graph[nx][ny] !=0 and visited[nx][ny] ==0:
                visited[nx][ny] =1
                q.append((nx,ny))



