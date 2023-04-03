n = int(input())
customers_x = []
customers_y = []
answer = 0
for _ in range(n):
    x,y = map(int,input().split())
    customers_x.append((x))
    customers_y.append((y))

customers_x.sort()
customers_y.sort()

mart_x = customers_x[n//2]
mart_y = customers_y[n//2]

for i in range(n):
    answer += abs(mart_x - customers_x[i]) + abs(mart_y - customers_y[i])

print(answer)