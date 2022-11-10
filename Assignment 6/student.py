# oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

import random


class Student:
    def __init__(self, name: str, student_id: int, year: str, major: str, gpa: float):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.gpa = gpa

    def is_honors(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def free_lunch(self):
        winning_id = random.randint(1, 1000)
        if self.student_id == winning_id:
            return "Winner! " + self.name + " gets a free lunch!"
        else:
            return "Loser!"


def main():
    # create three students and check if they get free lunch and if they qualify for honors
    student1 = Student("Nick", 1, "f", "Computer Science", 4.0)
    print(student1.is_honors(), student1.free_lunch())

    student2 = Student("Valentina", 4, "f", "Business", 4.0)
    print(student2.is_honors(), student2.free_lunch())

    student3 = Student("Blob", 999, "s", "Rock Studies", 0.1)
    print(student3.is_honors(), student3.free_lunch())


main()
