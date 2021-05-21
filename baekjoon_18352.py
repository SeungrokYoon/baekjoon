
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
            node = queue.popleft()
            if node[1] ==k:
                answer.append(node[0])
            if node[1] > k:
                break
            for i in range(1,n+1):
                if adj[node[0]][i] ==1 and visited[i] == 0:
                    visited[i] = 1
                    queue.append((i, node[1]+1))

        return sorted(answer)

    result= bfs(adj,x,k)
    if len(result) ==0 :
        return -1
    else:
        for i in result:
            print(i)
        return result

if __name__ == '__main__':
    print(solution())
