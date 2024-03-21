n = int(input())
count = 0

while (n>=0):
    if (n%5==0):
        count += (n//5)
        print(count)
        break
    elif (n%5!=0):
        n -= 3
        if n < 0:
            print(-1)
            break
        count += 1
    if n < 0:
        print(-1)
        break