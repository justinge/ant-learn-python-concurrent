from random import randint, sample
from functools import reduce

print(sample('abcdefg', randint(3, 6)))
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s4 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1, s2, s3, s4)
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print(res)

# 利用集合set的交集操作
# step1:使用字典viewkeys()方法，得到一个字典keys的集合
# step2:使用map函数,得到所有字典keys的集合
# step3:使用reduce函数,取出所有字典的keys的集合的交集
print(dict.keys(s1))
print(dict.keys(s2))
print(dict.keys(s3))
print(dict.keys(s1) & dict.keys(s2) & dict.keys(s3))
# 对于确定的轮次,以上方法就满足了, 对于 n轮那
print(list(map(dict.keys, [s1, s2, s3])))

print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))
