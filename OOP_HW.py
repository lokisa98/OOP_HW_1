

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lectors(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def avg(self,grades):
        self.grades = grades
        count = 0
        for i,v in self.grades.items():
            count += (sum(v)/len(v))
        return round(count/len(self.grades),1)
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашнее задание: {self.avg(self.grades)}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}')


    def __gt__(self,other):
        return self.avg(self.grades) > other.avg(other.grades)
                

     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        pass
        
        
class Lecturer(Mentor):

    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.courses_attached = []
        self.grades = {}
    pass

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}'
                f'Cредняя оценка за лекции: {self.avg(self.grades)}')
    

    def avg(self,grades):
        self.grades = grades
        count = 0
        for i,v in self.grades.items():
            count += (sum(v)/len(v))
        return round(count/len(self.grades),1)
    
    def __gt__(self,other):
        return self.avg(self.grades) > other.avg(other.grades)
                
    
    
class Reviewer(Mentor):

    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')
        
best_student = Student('Dmitrii','Kosachev','male')
my_student = Student('Natalia','Verhoturceva','female')
best_reviewer = Reviewer('Egor','Klochkov')
my_reviewer = Reviewer('Anton','Naif')
best_lecturer = Lecturer('Andrew','Baranov')
my_lecturer = Lecturer('Anastasia','Rud')

best_student.add_courses('Git')
best_student.courses_in_progress += ['Python']
my_student.courses_in_progress += ['Python']
best_lecturer.courses_attached += ['Python']
my_reviewer.courses_attached += ['Python']
my_reviewer.courses_attached += ['Golang']
best_student.courses_in_progress += ['Golang']
my_student.courses_in_progress += ['Golang']
my_reviewer.courses_attached += ['Golang']
best_lecturer.courses_attached += ['Golang']
my_lecturer.courses_attached += ['Python']
my_reviewer.rate_hw(best_student,"Python",10)
my_reviewer.rate_hw(best_student,"Python",6)
my_reviewer.rate_hw(best_student,"Python",7)
my_reviewer.rate_hw(best_student,"Python",6)
my_reviewer.rate_hw(best_student,"Golang",8)
my_reviewer.rate_hw(best_student,"Golang",5)
my_reviewer.rate_hw(best_student,"Golang",6)
my_reviewer.rate_hw(best_student,"Golang",4)
my_reviewer.rate_hw(my_student,"Python",10)
my_reviewer.rate_hw(my_student,"Python",6)
my_reviewer.rate_hw(my_student,"Golang",6)
my_reviewer.rate_hw(my_student,"Golang",4)
my_reviewer.rate_hw(my_student, "Golang",10)
print(best_student.avg(best_student.grades))
print(my_student.avg(my_student.grades))
print(my_student)
print(best_student)
print(my_student > best_student )
print(best_lecturer.courses_attached)
best_student.rate_lectors(best_lecturer,'Python', 10)
best_student.rate_lectors(best_lecturer,'Python', 4)
best_student.rate_lectors(best_lecturer,'Python', 7)
best_student.rate_lectors(best_lecturer,'Python', 8)
best_student.rate_lectors(best_lecturer,'Golang', 5)
best_student.rate_lectors(best_lecturer,'Golang', 3)
best_student.rate_lectors(best_lecturer,'Golang', 8)
best_student.rate_lectors(best_lecturer,'Golang', 10)
best_student.rate_lectors(my_lecturer,'Python', 5)
best_student.rate_lectors(my_lecturer,'Python', 3)
best_student.rate_lectors(my_lecturer,'Python', 2)
best_student.rate_lectors(my_lecturer,'Python', 1)
print(best_lecturer.grades)
print(my_lecturer.grades)   
print(my_lecturer > best_lecturer)
