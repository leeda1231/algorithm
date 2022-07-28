n = int(input())

# 가로 줄 수
4*n - 3
# 가운데 수
2*n - 1
# 세로 줄 수
8*n - 7

for i in range(8*n-7):
    if i%2:
        print('')
    else:
        pass