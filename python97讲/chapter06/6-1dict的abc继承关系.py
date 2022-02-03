from collections.abc import Mapping, MutableMapping

# dict 属于mapping类型
a = dict()
print(isinstance(a, MutableMapping))
print(isinstance(a, Mapping))
