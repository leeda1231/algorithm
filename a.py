a = [[0,0],[1,1]]
b = [arr[:] for arr in a]
b[1][0] = 2
print(b)
print(a)