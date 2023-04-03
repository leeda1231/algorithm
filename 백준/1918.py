stc = input()
stack = []
ans = []
opr = ['+','-','*','/']


for x in stc:
    if x in opr:
        stack.append(x)

    else:
        ans.append(x)
    
print(''.join(ans))