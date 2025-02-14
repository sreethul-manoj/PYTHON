# class Emp:
# #     id=100
# #     name="sreethul"
# #     def display(self):
# #         print(self.id,self.name)
# # obj=Emp()
# # obj.display()



# class Emp:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
#     def display(self):
#         print(self.name,self.id,self.age)
# obj=Emp("sreethul",100,24)
# obj1=Emp("sanjay",101,30)
# obj.display()
# obj1.display()



# class student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=student("sreethul",100,101)
# print(getattr(s,"name"))
# setattr(s,"age",23)
# print(getattr(s,"age"))
# print (hasattr(s,"id"))
# delattr(s,"age")
# print(getattr(s,"age")) #del then its error


class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_available = True
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"you have borroed '{self.title}'")
        else:
            print(f"the {self.title} is unavailable")
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"you have returned '{self.title}'")
        else:
            print(f"it's not returned '{self.title}")
    def display(self):
        if self.is_available:
            status = "Available"   
        else:
            status = "Not available"
        print(f"title:{self.title},author:{self.author},status:{status}")
        
object=Book("story","sreethul")
object.borrow()
object.display()
object.return_book()
object.display()
        





        

