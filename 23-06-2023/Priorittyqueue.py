stu_grade = []
stu_grade.append((1,"Pranay"))
stu_grade.append((4,"Sriram"))
stu_grade.sort(reverse=True)
print("Yes")
print(stu_grade)
stu_grade.append((3,"Teja"))
stu_grade.append((2,"Akshay"))
stu_grade.sort(reverse=True)
print("Priority wise sorted")
print(stu_grade)

print("Original Queue")
while stu_grade:
    print(stu_grade.pop())

