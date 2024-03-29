n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    change = basket[i-1:j]
    change.reverse()
    basket = basket[:i-1] + change + basket[j:]

for v in basket:
    print(v, end=" ")