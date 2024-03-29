leftovers = set()
for _ in range(10):
    num = int(input())
    leftovers.add(num%42)
print(len(leftovers))