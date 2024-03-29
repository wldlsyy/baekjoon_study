n=int(input())
number = list(map(int, input().split()))
target = int(input())

cnt=0
for num in number:
    if num == target:
        cnt+=1
print(cnt)