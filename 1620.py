from collections import defaultdict
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