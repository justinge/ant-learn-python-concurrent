res1 = sorted([9, 1, 2, 3])
print(res1)
from random import randint

res2 = {x: randint(60, 100) for x in 'xyzabc'}
print(res2)
res3 = sorted(res2)
print(res3)
# 利用zip将字典数据转化成元组
print(sorted(zip(res2.values(), res2.keys())))
# 利用sorted 的key
print(res2.items())
print(sorted(res2.items()))
print(sorted(res2.items(), key=lambda x: x[1]))
