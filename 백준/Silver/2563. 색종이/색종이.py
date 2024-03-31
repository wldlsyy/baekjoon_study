arr = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = 0
for row in range(100):
    result += arr[row].count(1)

print(result)