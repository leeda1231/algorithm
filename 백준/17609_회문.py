def palindrome(word):
    global ans
    s = 0
    e = len(word) - 1
    while s < e:
        if word[s] != word[e]:
            # 유사회문
            pseudo_palindrome(s+1,e,word)
            pseudo_palindrome(s,e-1,word)
            return
        s += 1
        e -= 1
    ans = 0


def pseudo_palindrome(s,e,word):
    global ans
    while s < e:
        if word[s] != word[e]:
            return
        s += 1
        e -= 1
    ans = 1


T = int(input())
for _ in range(T):
    word = input()
    ans = 2
    palindrome(word)
    print(ans)

'''
# 회문
def check1(w):
    global ans
    left = 0
    right = len(w) - 1
    while left < right:
        if w[left] == w[right]:
            left += 1
            right -= 1
            continue
        else:
            check2(w,left+1,right)
            check2(w,left,right-1)
        return
    ans = 0
    return

# 유사회문
def check2(w, start, end):
    global ans
    left = start
    right = end
    while left < right:
        if w[left] == w[right]:
            left += 1
            right -= 1
            continue
        return
    ans = 1
    return
    
T = int(input())
for _ in range(T):
    word = input()
    ans = 2
    check1(word)
    print(ans)
'''