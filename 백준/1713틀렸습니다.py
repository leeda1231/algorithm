n = int(input())
r = int(input())
id_lst = list(map(int,input().split()))
id_cnt = [0]*101
frame_lst = []
frame_set = set()

for id in id_lst:
    # 비어있는 사진틀 존재
    if len(frame_lst) < n:
        id_cnt[id] += 1
        if id in frame_set:
            for i in range(len(frame_lst)):
                if frame_lst[i][0] == id:
                    frame_lst[i][1] += 1
            continue
        frame_lst.append([id,id_cnt[id]])
        frame_set.add(id)
        continue
    # 비어있는 사진 존재x
    if id in frame_set:
        id_cnt[id] += 1
        for i in range(len(frame_lst)):
            if frame_lst[i][0] == id:
                frame_lst[i][1] += 1
        continue
    frame_lst.sort(key=lambda x:x[1])
    a,b = frame_lst.pop(0)
    id_cnt[a] = 0
    id_cnt[id] += 1
    frame_lst.append([id,id_cnt[id]])
    frame_set.add(id)
    frame_set.remove(a)

ans = []
for i in frame_lst:
    ans.append(i[0])
ans.sort()
print(*ans)
