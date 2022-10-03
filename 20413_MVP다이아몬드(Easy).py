n = int(input())
payment = dict()
payment["B"], payment["S"], payment["G"], payment["P"] = map(lambda x:x-1, map(int,input().split()))
# 한달에 최대 다이아몬드 등급 기준액까지만 과금 가능
payment["D"] = payment["P"] + 1
level = list(input())

amount = 0
num = -1
for i in range(n-1,-1,-1):
    if level[i] == "D":
        amount += payment["D"]
    else:
        num = i
        break

for i in range(num,-1,-2):
    amount += payment[level[i]]

print(amount)