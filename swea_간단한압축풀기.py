T = int(input())
for tc in range(T):
    n = int(input())
    str = ''
    for _ in range(n):
        w,cnt = input().split()
        cnt = int(cnt)
        str += w*cnt
    print(f'#{tc+1}')
    for i in range(0,len(str),10):
        print(str[i:i+10])