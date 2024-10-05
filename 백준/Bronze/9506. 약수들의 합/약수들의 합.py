def result(number):
    # 약수 구하기
    a = []
    total = 0
    for i in range(1, number//2+1):
        if number % i == 0:
            if i == number:
                continue
            total += i
            a.append(i)

    if total == number:
        print(f'{number} =', end=" ")
        for i in range(len(a)):
            if i==len(a)-1:
                print(a[i])
            else:
                print(f'{a[i]} +', end=" ")
    else:
        print(f'{number} is NOT perfect.')


n=[]
while True:
    number = input()
    if number == '-1':
        break
    n.append(int(number))

for i in range(len(n)):
    result(n[i])