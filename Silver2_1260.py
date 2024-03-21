n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)] # 인덱스 번호가 정점이고, 원소가 접하는
visited=[0]*(n+1) # 방문한 정점 처리할 배열

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 작은 순대로 정렬
for i in range(1, n+1):
    graph[i].sort()

def dfs(now, visited):
    visited[now] = 1 # 현재 정점 방문처리
    print(now, end=" ")
    for i in graph[now]:
        if visited[i]==0:
            dfs(i, visited)

def bfs(start, visited):
    visited[start] = 1
    print(start, end=" ")
    q = list()
    q.append(start) # 시작점 넣고 시작

    while q:
        curr = q.pop(0)
        for next in graph[curr]: # 현재 정점과 연결된 모든 이웃 정점
            if visited[next]==0:
                visited[next]=1
                print(next, end=" ")
                q.append(next)

dfs(start, visited)
visited=[0]*(n+1) # 배열 초기화
print()
bfs(start, visited)