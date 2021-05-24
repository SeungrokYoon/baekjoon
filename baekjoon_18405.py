"""
백준 18405 - 경쟁적 전염
개념: DFS/BFS
"""
import sys
from collections import deque
from collections import defaultdict

def bfs(N, graph,first_q):
    dx= [0,0,-1,1]
    dy= [-1,1,0,0]
    q= deque([])
    for i in first_q:
        visited[i[0]][i[1]] =0
        q.append(i)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx= dx[i] +x
            ny= dy[i] +y
            if nx<1 or ny<1 or nx>N or ny>N:
                continue
            if graph[nx][ny] ==0 and visited[nx][ny] ==-1:
                #visited에서 K번째 바이러스가 다음 사이클에서 전염되는 시간을 체크하기 위해,
                #이전 사이클 좌표에 저장된 시간에  +1을 한다.
                visited[nx][ny] = visited[x][y] +1
                #graph에서는 같은 바이러스 번호를 기록해준다.
                graph[nx][ny] = graph[x][y]
                q.append((nx,ny))


input = sys.stdin.readline

N, K = map(int, input().split())
graph = [[0for _ in range(N+1)]]
#바이러스 번호를 기록할 graph 그래프작성
for _ in range(N):
    graph.append([0]+list(map(int, input().split())))
#시간을 기록할 visited 그래프 작성
visited=  [[ -1 for _ in range(N+1)] for _ in range(N+1)]

#초와 목표 좌표 입력받기
S ,X ,Y = map(int, input().split())
first_q = []
first_d = defaultdict(list)

#bfs알고리즘 적용 이전에 번호 순서별 바이러스 초기 위치 좌표를 입력받기 위해 first_q 작성

#시간을 줄이기 위해 dictionary 형태로 바이러스 번호 별 좌표 등장 리스트를 작성하고 first_q에 extend한다.
for x in range(1, N+1):
    for y in range(1, N+1):
        if graph[x][y] !=0:
            first_d[graph[x][y]].append((x,y))
for i in range(1,K+1):
    first_q.extend(first_d[i])

bfs(N, graph, first_q)
#결과 출력
if visited[X][Y] > S :
    print(0)
else:
    print(graph[X][Y])