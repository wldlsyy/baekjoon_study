from collections import deque

M, N, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 0 # 하나의 영역에 대한 비어있는 정사각형 개수

    while q:
        cx, cy = q.popleft()

        if not visited[cx][cy]:
            visited[cx][cy] = 1
            cnt += 1

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                # 경계 검사
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue

                # 이미 방문했거나 비어있지 않으면
                if visited[nx][ny] or graph[nx][ny] != 0:
                    continue

                # 가능한 점
                q.append([nx, ny])

    return cnt

total_cnt = []
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 0:
            total_cnt.append(bfs(i, j))

print(len(total_cnt))
total_cnt = sorted(total_cnt)
for c in total_cnt:
    print(c, end=" ")