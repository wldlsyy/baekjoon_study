n = int(input())
target1, target2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = result[v]+1
            dfs(i)

dfs(target1)
if result[target2] > 0:
    print(result[target2])
else:
    print(-1)