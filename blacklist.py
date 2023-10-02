class people():
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        pass
class man(people):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        

Jojo = man("Dmitrii","Frederi",29)
print(Jojo.name)

grades = {"Python" : [3,7,9,10,9], "Golang" : [8,8,1,7,6]}  

def avg(grade):
    count = 0
    for i,v in grade.items():
        count += (sum(v)/len(v))
    return count/len(grade)
    
print(avg(grades))