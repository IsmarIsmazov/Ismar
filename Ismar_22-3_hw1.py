class Person:
    def __init__(self, fullname, age: int, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"fullname - {self.fullname} age - {self.age} is_married {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def average(self):
        print(f'average marks: {round(sum(self.marks.values()) / len(self.marks), 1)}')


class Teacher(Person):
    salary = 17000

    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    def sum_salary(self):
        if self.experience > 3:
            new_salary = round(self.salary + ((self.salary / 100 * 5) * (self.experience - 3)))
            print(new_salary)


def create_students():
    student1 = Student("Arbudu Imran", 16, "no", {
        "bio": 3,
        "phy": 3,
        "geo": 5})
    student2 = Student("Ismazov Ismar", 17, "no", {
        "bio": 5,
        "phy": 3,
        "geo": 5})
    student3 = Student("Bebeza Abdumalik", 19, "yes", {
        "bio": 3,
        "phy": 4,
        "geo": 4})
    result = [student1, student2, student3]

    return result


data = create_students()

for i in data:
    i.introduce_myself()
    print(i.marks)
    i.average()
