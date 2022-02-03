a = 1
b = "abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))


class Student:
    pass


stu = Student()
print(type(stu))

print(type(Student))
print(int.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))

a1 = "b"
a2 = "bb"
a3 = a1 + "b"
a4 = "b" + "b"

print(a2 == a3, id(a2) == id(a3), a2 is a3,id(a2),id(a3))
