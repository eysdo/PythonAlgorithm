"""
题目：回数是指从左到右和从右到左的数值一样，例如：像12321这样的数，从左边1-2-3-2-1，从右边1-2-3-2-1.
要求：从100到1000的回数个数
思路：反转，列表中的三种反转分别是reversed(),sorted()，切片，而字符串中没有reverse函数，所以使用切片比较方便点。
对比切片后的，并进行判断这里用到了filter起到过滤的作用，后面在统计。
"""
def fn(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False
res = len(list(filter(fn,range(100,1000))))
print(res)