A, B = input().split()
num1 = []
num2 = []
for a in A:
    num1.append(a)
for b in B:
    num2.append(b)
num1.reverse()
num2.reverse()
a1 = ''
b1 = ''
for v1 in num1:
    a1+=v1
for v2 in num2:
    b1+=v2
if int(a1)>int(b1):
    print(int(a1))
else:
    print(int(b1))
