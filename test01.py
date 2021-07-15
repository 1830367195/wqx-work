#print('hello pycharm')

"""变量
a=1
print(a)
a,b = 1,2
print(b)
"""

"""数字
int_a = 1
float_b = 2.1
complex_c = 2j
print(type(complex_c))
"""

"""字符串
a = 'string'
print(a)
"""

"""连接字符串:+变量之间的连接，空格不能用于变量之间的连接
a = "aaaa都"
b = "bbb不"
print (a+b)
print ("aaa12" "bbb佛跳")
"""

"""引用
a = 'aaaa'
b = 'bbb啊'
c = f'ccc{a}'
d = 'ccc{}'
e = 'eee{x}{y}'

print(c)
print(d.format(a))
*print(e.format(x=a,y=b))
"""

"""列表
list_a = [1,2,"a","b","c"]

print(list_a)
print(list_a[0])
print(list_a[-1])
print(list_a[0:3])
"""

"""分支语句（1）
a = 1
if (a == 0):
    print("a=0")
else:
    print("a!=0")
"""

"""(2)多重分支
a = 6
if (a<0):
    print("a<0")
elif (0<a<=5):
    print("0<a<5")
else:
    print("a>5")
"""

"""(3)嵌套分支
a = 3
if a>0:
    if a>2:
        print("a>2")
    else:
        print("0<a<2")
else:
    print("a<0")
"""
"""
x=2
if x <= 1:
    if x < -1:
        print(5*x+3)
    else:
        print(x+2)
else:
    print(3*x-5)
"""


"""课堂实战1___【礼物】
#定义全局变量
have_gift = False
#print(id(have_gift))

#发礼物
def send_gift():

    #局部变量
    have_gift = True
    gift_status = have_gift
    print(f"礼物状态{gift_status}")

    #打印内存地址
    print(id(gift_status))

if __name__ == '__main__':  #写入入库函数
#调用函数
   send_gift()
   # print(id(have_gift))
#
# 
"""

"""【猜数字】
出一个1-100的随机数
给出大一点、小一点、猜对了的提示



以下代码需修改
a=90
for i in range(101):
    if a>i:
        print("大一点")
    elif a<i:
        print("小一点")
    else:
        print("猜对了！")
    continue
print(i)
print(a)
"""

"""
list=[1,2,3]
#print(list.append(0))
list.append(0)
print(list)
list.insert(0,9)
print(list)
list.remove(2)
print(list)
list.pop(1)
y = list.pop(1)
print(list)
print(y)

list.sort()
print(list)

list2 = [1,3,4,5,2]
list2.reverse()
print(list2)



list_square=[]
for i in range(4):
    list_square.append(i**2)
print(list_square)

"""

i=2
j=3
a=i+j

0715edit
0715-3 edit

dev


















