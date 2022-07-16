n,m = map(int,input().split())

# 최소공배수(lcm) = 최대공약수 * (n//최대공약수) * (m//최대공약수)
# = n * m // gcd
# 유클리드 호제법
# 최대공약수? n%m = r, m과 r의 최대공약수와 같다
def GCD(x,y):
    while y:
        x,y = y, x%y
    return x

gcd = GCD(m,n)
lcm = n * m // gcd

print(gcd)
print(lcm)