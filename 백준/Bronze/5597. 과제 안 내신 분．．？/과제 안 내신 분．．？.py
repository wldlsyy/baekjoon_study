students = [x for x in range(1, 31)]

for _ in range(28):
    student = int(input())
    if student in students:
        students.remove(student)

for s in students:
    print(s)