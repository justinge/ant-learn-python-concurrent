from chapter04.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year


class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday


if __name__ == '__main__':
    user = User(Date(1990, 2, 1))
    student = Student(Date(1999, 1, 1))
    # print(user._User__birthday)
    # print(user.get_age())
    print(student.__dict__)
    print(user.__dict__)
    print(student.__dict__['_Student__birthday'])
    print(user.__dict__['_User__birthday'])