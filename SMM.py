student_name=input("Enter your name:")
print('''1:"CSE-DS",
2:"CSE(AI&DS)",
3:"CSE-A",
4:"CSE-B",
5:"CSE-C",
6:"EEE",
7:"CSE(AL&ML)"
''')
choose={
1:"CSE-DS",
2:"CSE(AI&DS)",
3:"CSE-A",
4:"CSE-B",
5:"CSE-C",
6:"EEE",
7:"CSE(AL&ML)"
}
while True:
   course=int(input("choose an option:"))
   if course==1:
    print("okay")
   elif course==2:
    print("okay")
   elif course==3:
    print("okay")
   elif course==4:
    print("okay")
   elif course==5:
    print("okay")
   elif course==6:
    print("okay")                
   elif course==7:
    print("okay")
   else:
    print("Please enter the correct course name")
    continue
   break
student_course = choose[course]
print(student_course)
while True:
 student_Hallno = int(input("Enter your Rollno: "))
 with open("student_details.txt", "r") as file:
  data = file.read()
 if f"'Hallticket.no': {student_Hallno}" in data:
  print("Roll number already exists")
  continue
 if 1 <= student_Hallno <= 50:
  print("okay")
 break
else:
 print("invalid roll")
while True:
    try:
        Maths = int(input("Enter your maths marks: "))
        break

    except ValueError:
        print("Please enter your marks")
        continue

while True:
    try:
        Python= int(input("Enter your python marks: "))
        break

    except ValueError:
        print("Please enter your marks")
        continue

while True:
    try:
        Java = int(input("Enter your java marks: "))
        break

    except ValueError:
        print("Please enter your marks")
        continue

student_detail={
    "name":student_name,
    "course":student_course,
    "Hallticket.no":student_Hallno
}
print(student_detail)
if Python<=35 or Java<=35 or Maths<=35 :
    print("Fail")
    status="Failed"
    print(status)

elif  Python<=40 or Java<=40 or Maths<=40 :
    print("D")
    status="pass"
    print(status)

elif Python<=50 or Java<=50 or Maths<=50 :
    print("C")
    status="pass"
    print(status)
    

elif Python<=60 or Java<=60 or Maths<=60:
    print("C+")
    status="pass"
    print(status)
    
elif Python<=70 or Java<=70 or Maths<70:
    print("B")
    status="pass"
    print(status)
    
elif Python<=80 or Java<=80 or Maths<=80:
    print("B+")
    status="pass"
    print(status)

elif Python<=90 or Java<=90 or Maths<=90:
    print("A")
    status="pass"
    print(status)
    
elif Python<=100 or Java<=100 or Maths<=100:
    print("A+")
    status="pass"
    print(status)


def calculate_total(Maths,Python,Java):
    total=Maths+Python+Java
    return total
result = calculate_total(Maths, Python, Java)

print("Total marks:", result)
percentage=result/3
print(f"percentage:{percentage:.2f}")

with open("student_details.txt","a")as file:
     file.write("student_detail\n")
     file.write(str(student_detail) + "\n")
     file.write("Python:" + str(Python) +"\n")
     file.write("java:"+ str(Java) +"\n")
     file.write("Maths"+str(Maths) +"\n")
     file.write("totalMarks"+str(result)+"\n")
     file.write(f"Percentage: {percentage:.2f}\n")

