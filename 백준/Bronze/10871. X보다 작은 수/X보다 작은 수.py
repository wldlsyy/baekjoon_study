n, x = map(int, input().split())
array = list(map(int, input().split()))

for num in array:
    if num<x:
        print(num, end=" ")