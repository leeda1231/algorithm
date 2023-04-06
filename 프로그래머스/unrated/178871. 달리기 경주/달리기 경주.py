def solution(players, callings):
    dic = dict()
    for i in range(len(players)):
        dic[players[i]] = i
    for c in callings:
        x = dic[c]
        a,b = players[x-1], players[x]
        dic[a], dic[b] = x,x-1
        players[x-1], players[x] = b,a
    return players