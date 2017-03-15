# coding=utf-8

f=lambda x,y,z:x+y+z;
print f(1,2,3);

#输出 6

f=lambda x,y,z:x+y+10+z
print f(1,2,3)

# 输出 16

# 算出n的阶乘
def factorial(n):
    f=reduce(lambda x,y:x*y,range(1,n+1))
    print f
factorial(4)
# 输出 24


# lambda表达式也可以用在def函数中。
def add(x):
    return lambda y:x+y

f=add(3)
print f(2)
# 输出 5

# 可以把def直接写成lambda形式
f=lambda x:lambda y:x+y
a=f(1)
print a(2)

# 输出 3




