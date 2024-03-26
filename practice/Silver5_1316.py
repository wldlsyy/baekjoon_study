def is_groupnum(str):
    temp = []
    for i in range(len(str)):
        if i == len(str)-1:
            temp.append(str[-1])
            break
        if str[i] == str[i+1]:
            continue
        else:
            temp.append(str[i])

    if len(temp) == len(set(temp)):
        return True
    else:
        return False



if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for i in range(n):
        str = input()
        if is_groupnum(str):
            cnt += 1
    print(cnt)