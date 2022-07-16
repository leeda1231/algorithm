answer = [[]]
    col = set()
    beam = set()
    for build in build_frame:
        x,y,a,b = build
        
        # 기둥
        if a == 0:
            # 설치
            if b == 1:
                if y == 0 or (x,y) in col or (x,y) in beam:
                    col.update([(x,y),(x,y+1)])
            # 삭제
            else:
                pass
        
        # 보
        else:
            # 설치
            if b == 1:
                if (x,y) in col or ((x,y)
            # 삭제
            else:
                pass
                
    return answer