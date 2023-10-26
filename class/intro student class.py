class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.all_attendence = {}

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
    def get_average(self):
        total_score = 0
        for i in self.grades:
            total_score = total_score + i.score
        return(int(total_score / len(self.grades)))

    def update_attendence(self,attendence):
        if type(attendence) is Attendence:
            self.all_attendence[attendence.date] = attendence.att_status

class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return (self.score >= minimum_passing)


class Attendence:
    def __init__(self,date,att_status):
        self.date = date
        self.att_status = att_status


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(90))
pieter.add_grade(Grade(78))

pieter.name = "tony"

pieter.update_attendence(Attendence("10/2", False))
pieter.update_attendence(Attendence("10/3", True))
pieter.update_attendence(Attendence("10/5", False))

print(pieter.all_attendence)

pieter.all_attendence = {"9/7":True}

print(pieter.get_average())
print(pieter.all_attendence)
print(pieter.name)
