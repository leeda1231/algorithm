from itertools import permutations

def solution(numbers):
    answer = 0
    nums = []
    for i in range(len(numbers)):
        for j in permutations(numbers,i+1):
            nums.append(int(''.join(j)))
    num_lst = list(set(nums))
    
    for num in num_lst:
        if num != 0 and num != 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                answer += 1        
    return answer