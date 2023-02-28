for tc in range(10):
    n = int(input())
    boxes = list(map(int,input().split()))
    for _ in range(n):
        max_v = max(boxes)
        max_idx = boxes.index(max_v)
        min_v = min(boxes)
        min_idx = boxes.index(min_v)
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    ans = max(boxes) - min(boxes)
    print(f'#{tc+1} {ans}')