#Student Marks,Percentage amd Grade
name=input("Enter student name:")
n=int(input("Enter number of subject:"))
total=0
for i in range (1,n+1):
    mark=float(input(f"Enter mark for subject{i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="outstanding"
elif percentage>=80:
    grade="A"
    performance="Excellent"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif performance>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
   grade="F"
   performance="Needs improvement"
print("\n---Academic Performance--")
print("Student Name:",name)
print("Total Marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)
      
