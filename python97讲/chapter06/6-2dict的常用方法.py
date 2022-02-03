a = {
    'bobby1': {"company": "imooc"},
    'bobby2': {'company': 'imooc2'},
}
# print(a)
# a.clear()
# print(a)
# copy, 返回浅拷贝


# copy, 返回浅拷贝
new_dict = a.copy()
new_dict["bobby1"]["company"] = "imooc3"

import copy

new_dict = copy.deepcopy(a)

new_dict["bobby1"]["company"] = "imooc3"

bbb = 1
