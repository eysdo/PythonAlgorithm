'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级......它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳发。
要求：一行代码完成
提示：使用lambda方法
思路：
如果楼梯数已为0，则表明只有这一种跳法，也就是没有下一步的跳法了；若不为0，则设这一步会跳1、2、3~n阶，然后将跳完这一步的下一步跳法的跳法相加，返回结果。
'''
f = lambda n: n if n <2 else 2 * f(n-1)

n = 3
print(f(n))