from student import *
from teacher import *
from json_file_manager import *

print("Welcome to student data management program: \n1. Student\n2. Teacher ")
role = input("Please select your role: ")


if role == "1":
    print("Welcome to Students portal")
    std1 = Student
    t1 = Teacher
    roll = int(input("Enter Rollno. to view details: "))
    std1.single_student_rank(roll)

elif role == "2":
    print("Welcome to Teachers portal")
    t2 = Teacher
    std2 = Student
    print(f"Enter Teachers ID to verify as a Teacher: ")
    teacherid = int(input("Teacher ID: "))
    y_n = t2.validate_teacher(teacherid)
    if y_n == True:
        print("You are logged in as a Teacher")
        option = int(input("Press 1 for Students data manipulation.\nPress 2 for Teachers data manipulation.\n"))
        if option == 1:
            option1 = int(input("Enter your decision for Students data manipulation :\n1. Create a file. \n2. Append students data. \n3. Delete Students data. \n4. Display all Students details. \n5. Highest and lowest marks in class. \n6. View pass/fail details. \n7. View percentage and details of a specified student.\n"))
            
            if option1 == 1:
                std2.create_file()
                
            elif option1 == 2:
                std2.append_file()
                
            elif option1 == 3:
                eroll = int(input("Enter the roll no of student whose data you want to delete."))
                std2.delete_contents_of_student_file(eroll)
                print("Successfully deleted from students file.")
                
            elif option1 == 4:
                std2.all_students_info()
            
            elif option1 == 5:
                std2.highest_and_lowest_marks_class()
            
            elif option1 == 6:
                std2.pass_and_fail_students()
            
            elif option1 == 7:
                proll=int(input("Enter the roll no of student whose details you want to view."))
                std2.single_student_rank(proll)
            
            else:
                print("Enter valid information.")
        
        elif option == 2:
            option2 = int(input("Enter your decision for Teachers data manipulation: \n1. Add data in teacher file. \n2. Delete data from teacher file. \n3. Display details of teacher.\n"))
            if option2 == 1:
                t2.append_file()
            
            elif option2 == 2:
                idt = int(input("Enter the Teacher ID to delete data."))
                t2.delete_contents_of_teacher_file(idt)
                print("Successfully deleted data from teacher file.")
            
            elif option2 == 3:
                t2.all_teachers_info()
                
            else:
                print(f"Enter a valid option.")
                
    else:
        print("INVALID Teachers ID !!!")
     

    


