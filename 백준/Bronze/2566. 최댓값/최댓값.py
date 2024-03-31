board = []
for row in range(9):
    board.append(list(map(int, input().split())))

max_row = 0
max_col = 0
max_num = -1
for row in range(9):
    curr_max = max(board[row])
    if max_num < curr_max:
        max_num = curr_max
        max_row = row

for col in range(9):
    if max_num == board[max_row][col]:
        max_col = col

print(max_num)
print(max_row+1, max_col+1)