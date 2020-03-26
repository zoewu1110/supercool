class Student:
    def __init__(self,new_gender,new_major,new_id):
        self.gender=new_gender
        self.major=new_major
        self.id=new_id

    def joinClass(self):
        pass

    def quitClass(self):
        pass

    def set_gender(self,new_gender):
        if new_gender=='m'or new_gender=='F':
            self.gender=new_gender
        else:
            print("again")

student1=Student("m",'IEM',"B10721003")
# print(student1.gender)
student1.gender='F'
print(student1.gender)