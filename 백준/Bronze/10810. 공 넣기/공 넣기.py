n, m = map(int, input().split())
bucket = {}
for key in range(1, n+1):
    bucket[key] = 0

for num in range(1, m+1):
    i, j, k  = map(int, input().split())
    for idx in range(i, j+1, 1):
        bucket[idx] = k

for value in bucket.values():
    print(value, end=" ")