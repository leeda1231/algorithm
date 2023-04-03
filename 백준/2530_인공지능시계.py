a,b,c = map(int,input().split())
d = int(input())

# 초
s = (c+d) % 60
c += d
# 분
m = (b + (c//60)) % 60

# 시
h = (a + ((b + (c//60))//60)) % 24

print(h,m,s)