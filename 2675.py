T = int(input())
for _ in range(T):
    x,word = input().split()
    for w in word:
        for _ in range(int(x)):
            print(w,end='')
    print()