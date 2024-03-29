from collections import deque

def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[x+dx][y+dy] != '#' and board[x+dx][y+dy] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited.append((rx, ry, bx, by))
    cnt=0

    while q:
        rx, ry, bx, by = q.popleft()
        if cnt >= 10:
            break

        for i in range(4): # 네 방향 모두 탐색
            nrx, nry, rcount = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcount = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == 'O': # 파란 구슬이 구멍에 먼저 들어가면 실패
                continue
            if board[nrx][nry] == 'O': # 빨간 구슬이 구멍에 들어가면 성공
                print(cnt)
                return

            if nrx==nbx and nry==nby: # 두 구슬이 위치가 같다면:
                if rcount > bcount: # 더 많이 이동한 구슬 한칸 뒤로
                    nrx-=dx[i]
                    nry-=dy[i]
                else:
                    nbx-=dx[i]
                    nby-=dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                cnt+=1
                q.append((nrx, nry, nbx, nby))

    print(-1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [[0 for col in range(n)] for row in range(m)]

    for x in range(n):
        str = input().rstrip()
        for y in range(m):
            board[x][y] = str[y]
            if str[y] == 'R':
                rx, ry = x, y
            elif str[y] == 'B':
                bx, by = x, y

    # 방향 L, R, D, U
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = []
    bfs(rx, ry, bx, by)
