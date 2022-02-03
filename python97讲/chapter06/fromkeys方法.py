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
