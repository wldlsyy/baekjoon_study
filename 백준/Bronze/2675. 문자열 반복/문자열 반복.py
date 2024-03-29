t = int(input())
for _ in range(t):
    r, S = input().split()
    for s in S:
        print(s*int(r), end="")
    print("")