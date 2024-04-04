import sys
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
    graph[i].sort(reverse=True) # 정점 내림차순 정렬

cnt = 1
def dfs(R):
    global cnt
    visited[R] = cnt

    for x in graph[R]:
        if visited[x] == 0:
            cnt+=1
            dfs(x)

dfs(R)
for x in range(1, N+1):
    print(visited[x])