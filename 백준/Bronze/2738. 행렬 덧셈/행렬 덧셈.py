n, m = map(int, input().split())
A = []
B = []

for row in range(n):
    A.append(list(map(int, input().split())))

for row in range(n):
    B.append(list(map(int, input().split())))

for row in range(n):
    for col in range(m):
        print(A[row][col]+B[row][col], end=' ')
    print()