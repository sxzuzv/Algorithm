# 학생들의 이름과 키를 저장한 두 배열을 사용하여 키가 180cm 이상인 학생들의 이름을 출력
students_name = ["쿠리", "햄햄", "냥냥", "견"]
students_heights = [175, 190, 174, 184]

def get_180_over_indexes(heights):
    result = []
    for i in range(len(students_heights)):
        if (heights[i] > 180):
            result.append(i)
    return result
    
over_indexes = get_180_over_indexes(students_heights)

for i in over_indexes:
    print(students_name[i])