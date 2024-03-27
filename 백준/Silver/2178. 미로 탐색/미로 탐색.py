from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    info = input().rstrip()
    for char in info:
        graph[i].append(int(char))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:  # (N, M) 위치에 도착
            print(visited[x][y])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] != 0 or graph[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

bfs()