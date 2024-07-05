from json_file_manager import *
if __name__=="__main__":
    print("From the student file.")
    
class Student:
    def create_file():
        create_student_file()
        
    def append_file():
        """
        Data in a file.
        """
        append_in_student_file()
        
    def all_students_info():
        """
        Display contents required for teachers.
        """
        value=view_contents_of_student_file()
        for num in value:
            for k,v in num.items():
                if k=="Name":
                    print(f"{k} : {v}")
                if k=="Marks":
                    print("Marks are:")
                    for marks in v:
                        print (marks)
                if k=="Roll":
                    print(f"{k} : {v}")
            print("\n")   
            
    def highest_and_lowest_marks_class():
        a=100
        b=0
        value=view_contents_of_student_file()
        for num in value:
            for k,v in num.items():
                if k=="Marks":
                    for marks in v:
                        if marks>b:
                           b=marks
                        if marks<a:
                           a=marks
        print(f"The highest marks is {b} and lowest marks is {a} in the entered data.")                
                        
    def pass_and_fail_students():
        """
        Pass/fail returning boolean value.
        """
        pm=0
        value=view_contents_of_student_file()
        for loop in value:
            for key,value in loop.items():
                if key=="Name":
                    print(f"Result of {value} is:")
                if key=="Marks":
                    for marks in value:
                        if marks<32:
                            pm=0
                            print("Fail")
                            break
                        else:
                            pm=marks
                    if pm>=32:
                        print("Pass")   
    
    def single_student_rank(roll):
        dict={}
        a=10
        value=view_contents_of_student_file()
        for num in value:
            for k,v in num.items():
                if k=="Roll" and v== roll:
                    dict=num
                    for key,value in dict.items():
                        print(f"{key}:{value}")
                        if key=="Marks":
                            for mark in value:
                                if mark<32:
                                    a=0
                                    break
                                else:
                                    total=sum(dict["Marks"])
                                    percentage=(total/500)*100
        if a==0:
            print("You have failed so percentage is not calculated.")                                              
        else:
            print(f"The percentage is::{round(percentage,6)}%")
            if percentage>=80:
                print("Grade A")
            elif percentage>=75:
                print("Grade B")
            elif percentage>=60:
                print("Grade C")
            elif percentage>=50:
                print("Grade D")
            elif percentage>=40:
                print("Grade E")
            else:
                print("Grade F")              
    
    def delete_contents_of_student_file(roll):
        value=view_contents_of_student_file()
        for dict in value:
            if dict["Roll"]==roll:
                value.remove(dict)
                with open ("student.json","w") as file:
                    json.dump(value,file,indent=3)
        


