class Father:
    def __init__(self,name,age):
        self.father_name=name
        self.father_age=age
        print("constructor is executed")

    def display(self):
        print("my father name is",self.father_name)
        print("my father age is ",self.father_age)
class Son(Father):
        def son_hii(self):
            print("hi i am ram")
            print("i  am 22 years old")
son_obj=Son("mohan",67)
print(son_obj.father_age)

        