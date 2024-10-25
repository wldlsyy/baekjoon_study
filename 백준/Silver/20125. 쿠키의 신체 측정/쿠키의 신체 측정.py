N = int(input()) # NxN 행렬
board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(len(line)):
        board[i][j] = line[j]

heo, l_leg, r_leg = 0, 0, 0
def find_heart():
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                return (i, j), (i + 1, j)


head, heart = find_heart()

l_arm = board[heart[0]][:heart[1]].count('*')
r_arm = board[heart[0]][heart[1] + 1:].count('*')

for i in range(heart[0] + 1, N):
    if board[i][heart[1]] != '*':
        last_heo = (i, heart[1])
        break
    else:
        heo += 1

for i in range(last_heo[0], N):
    if board[i][heart[1] - 1] == '*':
        l_leg += 1

    if board[i][heart[1] + 1] == '*':
        r_leg += 1


print(heart[0] + 1, heart[1] + 1)
print(l_arm, r_arm, heo, l_leg, r_leg)