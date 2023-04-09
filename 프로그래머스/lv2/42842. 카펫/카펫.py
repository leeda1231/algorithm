def solution(brown, yellow):
    for x in range(1,int(yellow**0.5)+1):
        if yellow % x == 0 and 2*x+2*(yellow//x)+4 == brown:
            answer = [yellow//x+2,x+2]
            break
    return answer