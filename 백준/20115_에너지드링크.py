n = int(input())
drinks = list(map(int,input().split()))
drinks.sort()
total = sum(drinks) / 2 + drinks[-1] / 2
print(total)