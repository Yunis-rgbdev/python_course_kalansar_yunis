subs = int(input("Enter the number of subjects: "))
grades = []

for i in range(subs):
    grade = int(input("subject's grade: "))
    grades.append(grade)
    
    
print(grades)    
avg = sum(grades) / subs
print(avg)
