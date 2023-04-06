from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    ty,tm,td = today.split('.')
    ty,tm,td = int(ty), int(tm), int(td)
    term = defaultdict(int)
    for t in terms:
        x,y = t.split()
        term[x] = int(y)
    for i in range(len(privacies)):
        date,s = privacies[i].split()
        y,m,d = date.split('.')
        y,m,d = int(y),int(m),int(d)
        nm = m + term[s]
        nd = d - 1
        if nd == 0:
            nd = 28
            nm -= 1
        if nm%12 == 0:
            ny = y + nm//12 -1
        else:
            ny = y + nm//12
        nm %= 12
        if nm == 0:
            nm = 12
        if (ny < ty) or (ny == ty and nm < tm) or (ny == ty and nm == tm and nd < td):
            answer.append(i+1)
    return answer