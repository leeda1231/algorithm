n = int(input())
stack = []
ans = []
cnt = 0

for i in range(n):
    x = int(input())
    while cnt < x: #cnt: 오름차순 입력 위해
        cnt += 1
        stack.append(cnt)
        ans.append('+')

    if stack[-1] == x: # pop은 언제 하는 것? input값이 젤 위에 있을 때 
        stack.pop()
        ans.append('-')
    else:
        ans = 'NO'
        break

if ans == 'NO':
    print(ans)
else:
    print(*ans, sep='\n')
