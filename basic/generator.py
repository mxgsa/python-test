# coding=utf-8

__author__ = 'mengxg'

# 生成一个列表
L=[x*x for x in range(1,8)]
print L

# 生成一个generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g=(x*x for x in  range(1,8))
print g

# generator 可以用g.next()获取每个元素
print g.next();

# 但是基本都是通过for来遍历generator
for x in g :
    print x


# 打印斐波拉契数列的值，但是很难创建一个这样列表
def fib(max):
    a,b,n=0,1,0
    while n<max :
        print b;
        a,b=b,a+b
        n=n+1

fib(6)

# 生成斐波拉契数列的generator，通过yield字段来处理，然后每次获取next的值
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n,a,b=0,0,1
    while n<max :
        yield b
        a,b=b,a+b
        n=n+1

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
g=fib(6)
print g

# 依然可以通过for来遍历出来需要的列表
for x in fib(6):
    print x