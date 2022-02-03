class Student:
    def say(self):
        print("i am a student")


stu = Student()


def say_teacher():
    print("i am teacher")


stu.say()
stu.say = say_teacher

stu.say()
