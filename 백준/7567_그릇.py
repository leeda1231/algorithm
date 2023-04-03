plate = list(input())
ans = 10
last = plate[0]

for i in range(1,len(plate)):
    if plate[i] != last:
        ans += 5
        last = plate[i]
    ans += 5

print(ans)