"""
백준 18352 - 특정 거리의 도시 찾기
메모리 초과가 뜸.
그 이유는 인접행렬을 이용했기 때문.
인접 리스트를 사용해야 메모리 사용이 적다!
"""


# SOLUTION1
import sys
from collections import deque


def solution():
    n,m,k,x = map(int, sys.stdin.readline().rstrip().split())
    #graph 만들기
    adj = [[0 for _ in range(n+1)] for i in range(n+1)]
    for _ in range(m):
        s, t = map(int, sys.stdin.readline().rstrip().split())
        adj[s][t] = 1
    result = []


    def bfs(adj, x,k):
        answer=[]
        visited = [0] * (n+1)
        queue = deque([(x,0)])
        while queue:
            node, count = queue.popleft()
            if count ==k:
                answer.append(node)
            if count > k:
                break
            for i in range(1,n+1):
                if adj[node][i] ==1 and visited[i] == 0:
                    visited[i] = 1
                    queue.append((i, count+1))

        return sorted(answer)

    result= bfs(adj,x,k)
    if len(result) ==0 :
        print(-1)
        return -1
    else:
        for i in result:
            print(i)
        return result


# Solution2

import sys
from collections import deque


def bfs(graph, x, k):
    answer =[]
    visited = [False] *(n+1)
    queue = deque([(x, 0)])
    visited[x] =True
    while queue:
        node, count = queue.popleft()
        if count ==k:
            answer.append(node)
        elif count<k:
            for target in graph[node]:
                if not  visited[target]:
                    visited[target] = True
                    queue.append((target, count+1))
    return answer




n,m,k,x = map(int, sys.stdin.readline().rstrip().split())
#graph 만들기]
graph = [[]for _ in range(n+1)]
for _ in range(m):
    s,t = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append(t)
result =[]

result =  bfs(graph, x, k)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)
