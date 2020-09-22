# Author: Song Zhirui zjs5301@psu.edu
# Collaborator: Jack Hillman jsh5719@psu.edu
# Collaborator:  Shrey Hillman sxs6588@psu.edu
# Collaborator: Alexandros Condeelis afc5865@psu.edu
# Section:5

Grade1 = input("Enter your course 1 letter grade: ")
if Grade1 == "A":
  Gradepoint1 = 4.0
elif Grade1 == "A-": 
  Gradepoint1 = 3.67
elif Grade1 == "B+":
  Gradepoint1 = 3.33
elif Grade1 == "B":
  Gradepoint1 = 3.0 
elif Grade1 == "B-":
  Gradepoint1 = 2.67
elif Grade1 == "C+":
  Gradepoint1 = 2.33
elif Grade1 == "C":
  Gradepoint1 = 2.0
elif Grade1 == "D":
  Gradepoint1 = 1.0 
else:
  Gradepoint1 = 0.0
Gredit1 = input("Enter your course 1 credit: ")
Gradepoint1 = float(Gradepoint1)
Gredit1 = float(Gredit1)
Grade1 = float((Gradepoint1)*(Gredit1))/ (Gredit1)
print(f"Grade point for course 1 is: {str(Grade1)}")
Grade2 = input("Enter your course 2 letter grade: ")
if Grade2 == "A":
  Gradepoint2 = 4.0
elif Grade2 == "A-": 
  Gradepoint2 = 3.67
elif Grade2 == "B+":
  Gradepoint2 = 3.33
elif Grade2 == "B":
  Gradepoint2 = 3.0 
elif Grade2 == "B-":
  Gradepoint2 = 2.67
elif Grade2 == "C+":
  Gradepoint2 = 2.33
elif Grade2 == "C":
  Gradepoint2 = 2.0
elif Grade2 == "D":
  Gradepoint2 = 1.0 
else:
  Gradepoint2 = 0.0
Gredit2 = input("Enter your course 2 credit: ")
Gradepoint2 = float(Gradepoint2)
Gredit2 = float(Gredit2)
Grade2 = float((Gradepoint2)*(Gredit2))/ (Gredit2)
print(f"Grade point for course 2 is: {str(Grade2)}")
Grade3 = input("Enter your course 3 letter grade: ")
if Grade3 == "A":
  Gradepoint3 = 4.0
elif Grade3 == "A-": 
  Gradepoint3 = 3.67
elif Grade3 == "B+":
  Gradepoint3 = 3.33
elif Grade3 == "B":
  Gradepoint3 = 3.0 
elif Grade3 == "B-":
  Gradepoint3 = 2.67
elif Grade3 == "C+":
  Gradepoint3 = 2.33
elif Grade3 == "C":
  Gradepoint3 = 2.0
elif Grade3 == "D":
  Gradepoint3 = 1.0 
else:
  Gradepoint3 = 0.0
Gredit3 = input("Enter your course 3 credit: ")
Gradepoint3 = float(Gradepoint3)
Gredit3 = float(Gredit3)
Grade3 = float((Gradepoint3)*(Gredit3))/ (Gredit3)
print(f"Grade point for course 3 is: {str(Grade3)}")
GPA = float((Gradepoint1)*(Gredit1) + (Gradepoint2)*(Gredit2) + (Gradepoint3) * (Gredit3))/((Gredit1) + (Gredit2) + (Gredit3))
print(f"Your GPA is: {str(GPA)}")