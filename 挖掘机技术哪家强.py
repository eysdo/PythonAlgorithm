"""
为了用事实说明挖掘机技术到底哪家强，PAT组织了一场挖掘机技能大赛。现请你根据比赛结果统计出技术最强的那个学校。
点击查看源网页
输入格式：
输入在第1行给出不超过105的正整数N，即参赛人数。随后N行，每行给出一位参赛者的信息和成绩，包括其所代表的学校的编号（从1开始连续编号）、及其比赛成绩（百分制），中间以空格分隔。
输出格式：
在一行中给出总得分最高的学校的编号、及其总分，中间以空格分隔。题目保证答案唯一，没有并列。
输入样例：
6
3 65
2 80
1 100
2 70
3 40
3 0
输出样例：
2 150
"""
info = {}                       #定义一个字典，key是学校，value是分数
n = int(input())                #参赛人数
while n:
    a, b = input().split()      #a是学校ID，b是分数
    b = int(b)
    if a in info:
        info[a] += b
    else:
        info[a] = b
    n -= 1                      #参数人数剩余输入-1
max_score = -1                  #初始化学校最高得分
max_score_id = ''               #初始化得分最高的学校ID
for k in info:
    if info[k] > max_score:
        max_score_id = k
        max_score = info[k]
print('%s %d'%(max_score_id,max_score)) 