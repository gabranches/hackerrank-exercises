N = int(raw_input())
students = {}
grades = []

for _ in range(0, N):
    name = raw_input()
    students[name] = float(raw_input())
    grades.append(students[name])

grades = list(set(grades))
grades.remove(min(grades))

lowest_grade = min(grades)

ans = sorted([student for student in students if float(students[student]) == lowest_grade])

for x in ans: print x