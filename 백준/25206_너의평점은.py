# (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
total = 0
val = 0
grade = {'A+':4.5, 'A0':4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for _ in range(20):
    x,y,z = input().split()
    if z == 'P':
        continue
    total += float(y)
    val += float(y)*grade[z]
print(val/total)