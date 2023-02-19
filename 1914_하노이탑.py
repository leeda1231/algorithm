def hanoi(n):
    if n == 1:
        return 1
    return 2*hanoi(n-1)+1

def move(n,s,t,m):
    if n == 1:
        print(s,t)
        return
    #n-1개원판 1->2
    move(n-1,s,m,t)
    #n번째원판 1->3
    print(s,t)
    #n-1개원판 2->3
    move(n-1,m,t,s)

n = int(input())
print(hanoi(n))
if n <= 20:
    move(n,1,3,2)