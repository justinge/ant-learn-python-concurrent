"""
学生信息系统中数据为固定格式:
(姓名,年龄,性别,邮箱地址)
学生数量很大为了减小储存开销,对每个学生信息用元组表示:
('Jim',16,'jim8721@gmail.com')
....
访问时,我们使用索引(index)访问,大量索引降低程序可读性,如何解决这个问题?
"""
from enum import Enum

studnet = ('Jim', 16, 'jim8721@gmail.com')


class StudentInfo(Enum):
    Name = 0
    Age = 1
    Email = 2


print(StudentInfo.Name.value)
print(studnet[StudentInfo.Name.value])
print(studnet[StudentInfo.Age.value])
print(studnet[StudentInfo.Email.value])

NAME, AGE, SEX, EMAIL = range(4)
print(NAME, AGE, SEX, EMAIL)
# 用name tuple 进行替换

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s2 = Student(name='Jim', age=16, sex='male', email='jim8721@gmail.com')
print(s2)
print(s2.age, s2.name, s2.email)
print(isinstance(s2,tuple))
