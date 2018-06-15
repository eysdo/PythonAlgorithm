"""
题目：一行代码实现对列表中的偶数位置的元素进行加4后对整个列表求和？
要求：一行代码实现
"""
from functools import reduce
a = [11,22,33,44,55]
#print(reduce(lambda x, y: x+y, [(x+4*((a.index(x)+1)%2)) for x in a]))
print(sum([y+4 if x%2==0 else y for x,y in enumerate(a)]))