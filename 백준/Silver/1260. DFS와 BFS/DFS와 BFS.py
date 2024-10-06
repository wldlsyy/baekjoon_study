from collections import deque

def dfs(v, graph):
    visited = [False for _ in range(n + 1)]
    # 첫 노드 추가
    s = deque()
    s.append(v)

    # 스택이 빌 때까지 반복
    while s:
        # 스택에서 최상단 노트 pop
        curr = s.pop()

        # 해당 노드를 아직 방문하지 않았다면
        if visited[curr] == False:
            # 방문 표시하고 출력
            visited[curr] = True
            print(curr, end=" ")

            s.extend(graph[curr])

def bfs(v, graph):
    visited = [False for _ in range(n + 1)]

    q = deque()
    q.append(v)

    while q:
        curr = q.popleft()

        if visited[curr] is False:
            visited[curr] = True
            print(curr, end=" ")

            for i in range(len(graph[curr]) - 1, -1, -1):
                q.append(graph[curr][i])


n, m, v = map(int, input().split())
graph = dict()
for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

dfs(v, graph)
print() # 한줄 바꿈
bfs(v, graph)