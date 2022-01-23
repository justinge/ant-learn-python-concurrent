# 如何统计序列中元素出现的频度
list1 = [1, 2, 3, 3, 0, 4]
# 如何找到出现次数最高的3个元素,他们出现的次数是多少?

list2 = ['hello', 'world']

from random import randint

data = [randint(0, 20) for _ in range(30)]

c = dict.fromkeys(data, 0)
print(c)
for x in data:
    c[x] += 1

print(c)

from collections import Counter

c2 = Counter(data)
print(c2)
print(c2.most_common(3))

import re

txt = open('CodingStyle').read()
res_list = txt.split('\W+', txt)
Counter(res_list, 10)
