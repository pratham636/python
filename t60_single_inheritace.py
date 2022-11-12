class  student:
    def __init__ (self,aname,asection):
        self.name=aname
        self.section=asection
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leavos=newleaves
    def print(self):
        return f"Name is {self.name}. section is {self.section}"
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def myfun(string):
        print("This is good "+ string)
class man(student):
    def printd(self):
        return self.name
harry=student("Harry",1) 
karan=man("Karan",480)      
print(karan.printd())