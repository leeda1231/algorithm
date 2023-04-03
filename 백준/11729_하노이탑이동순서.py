def hanoi(n):
    if n == 1:
        return 1
    return 2*hanoi(n-1)+1

def move(n,s,t,m):
    if n == 1:
        print(s,t)
        return
    #n-1개 원판을 2로 이동
    move(n-1,s,m,t)
    #n번째 원판을 3으로 이동
    print(s,t)
    #n-1번째 원판을 3으로 이동
    move(n-1,m,t,s)

n = int(input())
print(hanoi(n))
move(n,1,3,2)