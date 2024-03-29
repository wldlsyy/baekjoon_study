A, B = input().split()
A = int(A[::-1]) # [::-1] 은 역순을 뜻함!!
B = int(B[::-1])
if A>B:
    print(A)
else:
    print(B)
