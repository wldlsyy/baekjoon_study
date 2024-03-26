pattern={
    1:'c=', 2:'c-', 3:'dz=', 4:'d-', 5:'lj', 6:'nj', 7:'s=', 8:'z='
}

def find_pattern(pat, str):
    cnt = 0
    i = 0
    j = 0
    while i<len(str):
        if str[i] == pat[j]:
            if pat == 'z=':
                if str[i-1] == 'd':
                    i+=1; j=0
                    continue
            i+=1; j+=1
        else:
            if j==0:
                i+=1
            else:
                j = 0

        if j==len(pat):
            j=0
            cnt+=1

    return cnt


if __name__ == '__main__':
    str = input()
    cnt=0
    temp=0
    str_len = len(str)
    for i in range(1, 9):
        if ('-' in pattern[i] or '=' in pattern[i]) and ('-' not in str and '=' not in str):
            continue
        pat_cnt = find_pattern(pattern[i], str)
        if pat_cnt>0:
            cnt+=pat_cnt
            temp += pat_cnt*len(pattern[i])
    single_alpha = len(str) - temp
    cnt+=single_alpha

    print(cnt)
