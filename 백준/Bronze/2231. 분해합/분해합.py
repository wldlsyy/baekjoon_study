n = int(input())

result=0
for i in range(1, n+1):
    nums = list(map(int, str(i))) # i가 123이면, [1,2,3]으로 리스트에 저장
    result = sum(nums)+i # i + i의 각 자리수의 합
    if result == n:
        print(i)
        break
    if i==n:
        print(0)