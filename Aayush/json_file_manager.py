import json
from data_check import *
json_data_student=[]
json_data_teacher=[]
def create_student_file():
        namestd=input("Enter the Name of student.")
        rollstd=int(input("Enter the Rollno of the student."))
        addressstd=input("Enter the Address of the student.")
        marksstd=[]
        for i in range(0,5,1):
            value=float(input("Enter the Marks of the student."))
            marksstd.append(value)
        phonestd=int(input("Enter the Phone number of the student."))
        number_check(phonestd)
        emailstd=input("Enter the Email of the student.")
        email_validation(emailstd)
        json_data_student.append({
            "Name":namestd,
                "Address":addressstd,
                "Email":emailstd,
                "Marks":marksstd,
                "Roll":rollstd,
                "Phone":phonestd 
            
        })
        
        with open("student.json","w") as file:
            json.dump(json_data_student,file,indent=3)
            print("Successfully added data in file.\n")
    
def append_in_student_file():
    n=int(input("Enter the number of data you want to insert."))
    for i in range(0,n,1):
        namestd=input("Enter the Name of student.")
        rollstd=int(input("Enter the Rollno of the student."))
        addressstd=input("Enter the Address of the student.")
        phonestd=int(input("Enter the Phone number of the student."))
        number_check(phonestd)
        emailstd=input("Enter the Email of the student.")
        email_validation(emailstd)
        marksstd=[]
        for i in range(0,5,1):
            value=float(input("Enter the Marks of the student."))
            marksstd.append(value)
        
        with open("student.json","r") as file:
            json_data_student=json.load(file)
        json_data_student.append({
            "Name":namestd,
                "Address":addressstd,
                "Email":emailstd,
                "Marks":marksstd,
                "Roll":rollstd,
                "Phone":phonestd 
            
        })
        with open("student.json","w") as file:
            json.dump(json_data_student,file,indent=3)
            print("Successfully written data in file.\n")
    
def view_contents_of_student_file():
    with open("student.json","r") as file:
        content=json.load(file)
        return(content)

def create_teacher_file():
        nametea=input("Enter the Name of teacher.")
        subjecttea=input("Enter the Subject of the teacher.")
        addresstea=input("Enter the Address of the teacher.")
        phonetea=int(input("Enter the Phone no of the teacher."))
        number_check(phonetea)
        emailtea=input("Enter the Email of the teacher.")
        email_validation(emailtea)
        idtea=int(input("Enter the ID number of teacher."))
        json_data_teacher.append({
                "Name":nametea,
                "Address":addresstea,
                "Email":emailtea,
                "Subject":subjecttea,
                "ID":idtea,
                "Phone":phonetea
            
        })
        
        with open("teacher.json","w") as file:
            json.dump(json_data_teacher,file,indent=3)
            print("Successfully added data in file.\n")
            
def append_in_teacher_file():
    n=int(input("Enter the no of data you want to insert."))
    for i in range(0,n,1):
        nametea=input("Enter the Name of teacher.")
        subjecttea=input("Enter the Subject of the teacher.")
        addresstea=input("Enter the Address of the teacher.")
        phonetea=int(input("Enter the Phone number of the teacher."))
        number_check(phonetea)
        emailtea=input("Enter the Email of the teacher.")
        email_validation(emailtea)
        idtea=int(input("Enter the ID no of teacher."))
        with open("teacher.json","r") as file:
            json_data_teacher=json.load(file)
        json_data_teacher.append({
                "Name":nametea,
                "Address":addresstea,
                "Email":emailtea,
                "Subject":subjecttea,
                "ID":idtea,
                "Phone":phonetea
            
        }) 
        with open("teacher.json","w") as file:
            json.dump(json_data_teacher,file,indent=3)
            print("Successfully added data in file.\n")
    
    

def view_contents_of_teacher_file():
    with open("teacher.json","r") as file:
        content=json.load(file)
        return(content)

if __name__=="__main__":
    print("From the json manager file.")
