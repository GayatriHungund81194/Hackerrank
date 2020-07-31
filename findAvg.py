n = int(input())
student_marks = {}
for i in range(n):
    name = raw_input().split(" ",1)
    if name[0] not in student_marks:
        student_marks[name[0]] = name[1]
nm = raw_input()
if nm in student_marks:
    mks = student_marks[nm].split(" ")
    total = 0
    for i in range(len(mks)):
        total +=float(mks[i])
    num = len(mks)
    avg = total/num
    print(avg)