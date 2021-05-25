"""
백준 18428 - 감시 피하기
개념: DFS/BFS + 완전탐색
특징: 삼성전자 같은 기업의 코딩 테스트에서 많이 출제된다고 한다. by NDB
난관:
무엇을 먼저 해야 하는가.
1. 그래프 만들기 : 해당 그래프는 좌표지도이기 때문에 그냥 N X N 형식의 그리드를 입력받으면 된다.
2. 무엇을 탐색할 것인가:
2-1. 무엇에서부터 탐색을 시작할 것인가: ?
어떻게 선생님들의 감시 경로를 구현할 것인가
어떻게 선생님들의 감시망에 걸리는 학생들을 찾아낼 것인가.

초기 접근법:
실제로는 장애물을 설치한다고 하였지만, 장애물을 설치하는 가지수가 많은 까닭에, 장애물 설치를
위한 좌표를 찾는 것은 의미가 없는 것 같다. -> 문제풀이가 막힘

꺠달음:
N이 최대 6이기 때문에, 장애물 설치를 할 수 있는 모든 좌표들의 조합을 구하여 완전탐색을 진행하는 방법이
가능

교휸:
학창시절 수학문제와 같이 알고리즘 문제 또한 어떠한 핵심 개념이 교묘하게 포장되어 있는 것에 불과하다.
문제를 보고 어떤 핵심 개념을 사용해야 하는지, 또 그 개념이 이 문제에는 어떻게 적용되는지를 생각해보자.
문제를 보고 맨 처음 생각한 접근법이 반드시 맞는 것은 아니다.
"""

import sys
from itertools import combinations
input =sys.stdin.readline

N = int(input())
graph = []
#비어있는 초기 좌표 받아들이기.
empty_spot = []
teachers = []
for x in range(N):
    graph.append(input().rstrip().split())
    for y in range(N):
        if graph[x][y] =='X':
            empty_spot.append((x,y))
        if  graph[x][y] =='T':
            teachers.append((x,y))

#장애물을 만드는 모든 가능한 조합 산출
combi = []
for i in combinations(empty_spot, 3):
    combi.append(i)



def oversee(x,y,direction):
    #상
    if direction == 0:
        stop=False
        while not stop:
            x= x-1
            y= y
            if x<0 or x>= len(graph) or y<0 or y>=len(graph):
                stop=True
            elif graph[x][y] == 'O':
                stop=True
            elif graph[x][y] == 'S':
                return True
        return False



    #하
    if direction ==1:
        stop = False
        while not stop:
            x = x + 1
            y = y
            if x<0 or x>= len(graph) or y<0 or y>=len(graph):
                stop = True
            elif graph[x][y] == 'O':
                stop = True
            elif graph[x][y] == 'S':
                return True
        return False


    #좌
    if direction ==2:
        stop = False
        while not stop:
            x = x
            y = y -1
            if x<0 or x>= len(graph) or y<0 or y>=len(graph):
                stop = True
            elif graph[x][y] == 'O':
                stop = True
            elif graph[x][y] == 'S':
                return True
        return False



    #우
    if direction ==3:
        stop = False
        while not stop:
            x = x
            y = y +1
            if x<0 or x>= len(graph) or y<0 or y>=len(graph):
                stop = True
            elif graph[x][y] == 'O':
                stop = True
            elif graph[x][y] == 'S':
                return True
        return False







#주어진 combi를 활용해서 완전탐색 시작하기
#선생님들의 위치를 기준으로 탐색을 시작한다.
def process():
    #선생이 있는 위치를 시작으로
    #4방향으로 탐색을 해야 함.
    for x,y in teachers:
        for direction in range(4):
            if oversee(x,y,direction):
                return True
    return False


find =False
#장애물 조합 별로
for c in combi:
    for x, y in c:
        graph[x][y] = 'O'
    if not process():
        find= True
        break
    for x, y in c:
        graph[x][y] = 'X' #원래대로 돌려주기

if find:
    print("YES")
else:
    print("NO")



















