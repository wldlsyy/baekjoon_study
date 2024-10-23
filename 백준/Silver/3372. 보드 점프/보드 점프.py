def board_jump(n):
    for i in range(n):
        for j in range(n):
            if i == n - 1 and j == n - 1:
                return dp[i][j]

            step = board[i][j]

            if i + step < n:
                dp[i + step][j] += dp[i][j]
            if j + step < n:
                dp[i][j + step] += dp[i][j]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

print(board_jump(N))