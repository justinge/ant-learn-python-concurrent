from random import randint

# 过滤掉列表[] 中的复数 表达式 > filete > 循环
data = [randint(-10, 10) for _ in range(10)]
print(data)
print(list(filter(lambda x: x >= 0, data)))

print([x for x in data if x >= 0])

res = []
for x in data:
    if x >= 0:
        res.append(x)
print(res)

# 筛出字典中的值,字典解析
clases = {x: randint(60, 100) for x in range(1, 20)}
print(clases)
# 根据值过滤出来分数高于90的值， 字典解析
res = {k: v for k, v in clases.items() if v > 90}
print(res)

s = set(data)
res1 = {x for x in s if x % 3 == 0}
print(res1)
