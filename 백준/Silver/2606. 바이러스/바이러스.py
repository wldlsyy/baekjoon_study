from collections import deque
def bfs(start):
    visited = [False for _ in range(n+1)]
    q = deque([start])
    cnt = 0

    while q:
        curr = q.popleft()

        if visited[curr] is False:
            visited[curr] = True
            cnt += 1
            q.extend(graph[curr])

    return cnt

# 입력받기
n = int(input())
v = int(input())
# graph 선언
graph = dict()
for i in range(1, n+1):
    graph[i] = []
# 연결 쌍 추가
for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(1) - 1 # 1번은 빼야 되니까
print(result)