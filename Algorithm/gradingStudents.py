import sys

def solve(grades):
    # Complete this function
    result = []
    for grade in grades:
        if grade % 5 >= 3:
            new_grade = grade - grade % 5 + 5
        else:
            new_grade = grade

        if new_grade < 38:
            result.append(grade)
        else:
            result.append(new_grade)
    return result


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))