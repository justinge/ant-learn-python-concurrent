def ask(name="func"):
    print(name)


#
# my_func = ask
# my_func("func")


class Person:
    def __init__(self):
        print("class")


my_class = Person
# my_class()

obj_list = []
obj_list.append(ask)
obj_list.append(Person)


def print_type(item):
    print(type(item))


for item in obj_list:
    # print(item())
    print_type(item)


# 对象可以作为函数的返回值
def ask(name="func"):
    print(name)


def decorator_func():
    print("dec start")
    return ask


my_ask = decorator_func()
my_ask("tom")
