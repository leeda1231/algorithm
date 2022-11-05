n = int(input())
meetings = [list(map(int,input().split())) for _ in range(n)]
meetings.sort(key = lambda x:(x[0],x[1]))
end = meetings[0][1]
answer = 1

for i in range(1,n):
    if meetings[i][0] < end:
        answer += 1
        if meetings[i][1] < end:
            end = meetings[i][1]
    else:
        end = meetings[i][1]
    print(end)

print(answer)
'''
4
0 5
0 10
8 20
10 15
'''