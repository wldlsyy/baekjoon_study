import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort() # 정점 오름차순 정렬

cnt = 1
def bfs():
    global cnt
    q=deque([R])
    visited[R] = cnt

    while q:
        x = q.popleft()
        for point in graph[x]:
            if visited[point] == 0:
                cnt+=1
                q.append(point)
                visited[point] = cnt

bfs()
for x in range(1, N+1):
    print(visited[x])