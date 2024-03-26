s = set()

def find_constructor(n):
    # 일의 자리
    a = n%10
    # 십의 자리
    b = n//10%10
    # 백의 자리
    c = n//100%10
    # 천의 자리
    d = n//1000%10
    return n+a+b+c+d


if __name__ == '__main__':
    all = set(range(1, 10001))
    constructor = set()
    for i in range(1, 10001):
        constructor.add(find_constructor(i))

    self_number = sorted(all - constructor)

    for num in self_number:
        print(num)