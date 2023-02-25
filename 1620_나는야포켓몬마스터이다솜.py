from collections import defaultdict
import sys

# 2
input = sys.stdin.readline
n,m = map(int,input().split())
pokedex = defaultdict(str)
for i in range(1,n+1):
    pokedex[i] = input().rstrip()
pokedex_reverse = dict(map(reversed,pokedex.items()))
for _ in range(m):
    x = input().rstrip()
    if x.isalpha():
        print(pokedex_reverse[x])
    else:
        print(pokedex[int(x)])


# 1
n,m = map(int,input().split())
pokedex = defaultdict(str)
pokedex_reverse = defaultdict(int)
for i in range(1,n+1):
    pokemon = input()
    pokedex[i] = pokemon
    pokedex_reverse[pokemon] = i
for _ in range(m):
    value = input()
    if value.isalpha():
        print(pokedex_reverse[value])
    else:
        print(pokedex[int(value)])