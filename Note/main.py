# #1  打印
a = 10  # 数据交换
b = 20
a,b = b,a
print('Hello World')
print(a,b)
#   注释
'''
    三个单引号
'''
"""
    三个双引号
"""
# 变量规范 #3

ab = 'aaa'
res = type(ab)
print(ab,res)
# 大字符串
ab = '''   很长
'''
print(ab)
# #4 数字类型
a = 0x10
b = b'001100011' #type
f = 5+6j    #复数
bo = True # bool类型
print(a,b, type(b),f,type(f))

#  #5 列表
varlist = [1,2,3,4]
print(varlist,type(varlist))
varlist = ['a',1,'pai',3.14]
print(varlist[2],varlist[-1])
varlist = ['a',1,'pai',3.14,[3,4,5]]    #二级列表，二维列表，多维列表
print(varlist[3],type(varlist[3]))
print(varlist[4],type(varlist[4]),varlist[4][1],type(varlist[4][1]))
# 元组 tuple
var = (1,2,3,'a','b')
var_1 = ('abv',)
var_2 = 1,2,3,'ab'
print(var,type(var),var_1,type(var_1), var_2,type(var_2))

# #6 Dict 字典
vard = {'title':'<<鬼谷子>>', 'author':'鬼谷子','price':'29.99'}
print(vard,type(vard))
print(vard['title'])
# 键重复覆盖
vard = {'a':1,'b':2,'a':3}
print(vard,type(vard))

# #7 set
vars = {1,2,3,'a','b',1}
vars_1 = set('123456')
vars_2 = set()

print(vars,type(vars),vars_1,type(vars_1),vars_2,type(vars_2))

# 添加元素
a = {1,2,3,'a'}
a.add('b')
# 重复的无法添加
a.add('a')
print(a,type(a))
a.discard('a')
print(a,type(a))
# 检测是否存在
print('a' in a)
print(1 in a)
# 集合运算

a = {1,2,3,'a','b'}
b = {1,'a',22,33}
print(a & b) #交集
print(a - b) #差集 a 集合有，b集合没有
print(a | b) #并集 放在一起，并且去重
print(a ^ b) # 对称差集  重复的去掉