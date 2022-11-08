from collections import defaultdict

n = int(input())
dict_num = defaultdict(list)
dict_ans = defaultdict(int)
words = []
for _ in range(n):
    word = input()
    words.append(word)
    for i in range(1,len(word)+1):
        if word[i-1] not in set(dict_num[i]):
            dict_num[i].append(word[i-1])

for i in range(8,0,-1):
    if dict_num[i]:
        if len(dict_num[i]) == 1 and not dict_ans[dict_num[i][0]]:
            dict_ans[dict_num[i]] = i
        elif len(dict_num[i]) > 1:
            pass

















'''
dict_alpha = defaultdict(set)
dict_num = defaultdict(set)
dict_answer = defaultdict(int)
words = []

for _ in range(n):
    word = input()
    words.append(word)
    for i in range(1,len(word)+1):
        dict_alpha[word[i-1]].add(i)
        dict_num[i].add(word[i-1])

for i in range(8,-1,-1):
    if dict_num[i]:
        if len(dict_num[i]) == 1:
            x = dict_num[i]
            print(x)
'''


'''
AB 98 89
BC 87 97

54321
ACDEB
OOGCF
겹치면 뒤에 있는 알파벳 선택
'''