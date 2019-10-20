marks= input("enter the marks")
marks= int(marks)

if marks >=80 :
    grade="a+"
elif marks>=70:
    grade="a"
elif marks >=60:
    grade="b"
else:
    grade="F"

print("your grade is",grade)