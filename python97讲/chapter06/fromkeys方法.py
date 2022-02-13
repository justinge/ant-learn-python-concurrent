new_list = ["bobby1", "bobby2"]
new_dict1 = dict.fromkeys(new_list, {"company": "imooc"})
print(new_dict1)

# get 方法可以再查询为空时,指定返回值,不为空时,返回原字典中的值

a = {
    "bobby1": {"company": "imooc"},
    "bobby2": {"company": "imooc2"}
}
print(a.get("bobbbb", {}))
print(a.get('bobby1', {}))

for key, value in a.items():
    print(key, value)

# 4setdefault方法查询值，如果查不到key对应的值，则添加设置的值到原来的字典中去
print(a.setdefault("booooo", 1))
print(a)

a = {
    "bobby1": {"company": "imooc"},
    "bobby2": {"company": "imooc2"}
}
new_list = ["bobby1", "bobby2"]
print("---------------!!!!------------")
new_dict0 = a.fromkeys(new_list, {"company": "imooc"})
print(new_dict0)
print(new_dict0.update((("bobby", "imooc"),)))
print(new_dict0)


# 不建议继承list和dict
class Mydict(dict):
    def __setitem__(self, key, value):
        print("----------")
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)

from collections import UserDict


class Mydict(UserDict):
    def __setitem__(self, key, value):
        print("----------")
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)

from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["bobby"]

print(my_dict)

s = set("abcdeee")
print(s)
s = set(["a", "b", "c", "d", "e"])
print(s)

s = frozenset("abcde")
print(s)

# 向set添加数据
another_set = set("cef")
re_set = s.difference(another_set)
print(re_set)
re_set = s - another_set
print(re_set)
re_set = s & another_set
print(re_set)
re_set = s | another_set
print(re_set)
