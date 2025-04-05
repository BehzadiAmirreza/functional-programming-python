from functools import reduce

dict_list = [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}]

a = reduce(lambda acc, d: {**acc, **d}, dict_list, {})
print(a)