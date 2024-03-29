n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp1, temp2 = basket[i-1], basket[j-1]
    basket[i-1] = temp2
    basket[j-1] = temp1

for item in basket:
    print(item, end=" ")