grade = [0, 0, 0, 0]

# A로 가는 사람이 2명 이상 나올 때 > 위급상황 'E'를 마지막에 출력
for _ in range(3):
    symptom, temp = input().split()
    fever = float(temp) >= 37

    if symptom == 'Y':
        idx = 0 if fever else 2
    else:
        idx = 1 if fever else 3

    grade[idx] += 1

if grade[0] >= 2:
    grade.append('E')

print(*grade)