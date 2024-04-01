n, m = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = num_list[i] + num_list[j] + num_list[k]
            if total > m:
                continue
            if total > max_sum:
                max_sum = total

print(max_sum)