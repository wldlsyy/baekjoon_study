pieces = list(map(int, input().split()))
for i in range(len(pieces)):
    if i==0 or i==1:
        print(1-pieces[i], end=" ")
    elif i==2 or i==3 or i==4:
        print(2-pieces[i], end=" ")
    else:
        print(8-pieces[i], end=" ")