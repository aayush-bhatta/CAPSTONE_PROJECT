from json_file_manager import *

class Teacher:
    def create_file():
        create_teacher_file()
        
    def append_file():
        """
        To enter teacher data.
        """
        append_in_teacher_file()
    
    def validate_teacher(id):
        value=view_contents_of_teacher_file()
        for loop in value:
            for k,v in loop.items():
                if k=="ID" and v== id:
                    return True
        else:return False    
        
        
    def delete_contents_of_teacher_file(id):
        value=view_contents_of_teacher_file()
        for dict in value:
            if dict["ID"]==id:
                value.remove(dict)
                with open ("teacher.json","w") as file:
                    json.dump(value,file,indent=3)
        
    def all_teachers_info():
        """
        Display the contents required for teachers.
        """
        value=view_contents_of_teacher_file()
        for num in value:
            for k,v in num.items():
                if k=="Name":
                    print(f"{k} : {v}")
                if k=="ID":
                    print(f"ID is:{v}")
                if k=="Subject":
                    print(f"{k} : {v}")
                if k=="Email":
                    print(f"{k} : {v}")
            print("\n")   
        
if __name__=="__main__":
    print("From teacher file.")

