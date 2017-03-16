# coding=utf-8

print '---------map()函数实例---------'
# map()函数接收两个参数，一个是函数，一个是序列，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
def my_map(x):
    return x*x;

print map(my_map,[1,2,3,4,5,6,7,8,9])

# 输出 [1, 4, 9, 16, 25, 36, 49, 64, 81]

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 输出 ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print '---------reduce()函数实例---------'
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def my_reduce(x,y):
    return  x+y;

print reduce(my_reduce,[1,2,3,4,5,6]);

# 输出 21

# reduce把序列[1, 3, 5, 7, 9]变换成整数13579
def my_reduce2(x,y):
    return x*10+y;

print reduce(my_reduce2,[1,3,5,7,9])
# 输出 13579

# 实例 把['adam', 'LISA', 'barT']，转换成标准格式首字符大写：['Adam', 'Lisa', 'Bart']
def change_form(x):
    return str.capitalize(x);
print map(change_form,['adam', 'LISA', 'barT'])
# 输出 ['Adam', 'Lisa', 'Bart']

print '---------filter()函数实例---------'

# filter函数 在一个list中，删掉奇数，只保留偶数
def my_filter(x):
    return x%2==0

print filter(my_filter,[1,2,3,4,5,6,7,8])
# 输出 [2, 4, 6, 8]


# 获取1-100当中的素数
def my_filter2(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print filter(my_filter2,[x for x in range(1, 101)])

# 输出 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print '---------sorted()函数实例---------'

# 对列表进行正序排列
print sorted([100,3,2,45,23,55])
# 输出 [2, 3, 23, 45, 55, 100]


# sorted 只能正序排序，倒序的话就得重新写reversed_cmp函数了
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    else:
        return 0

print sorted([100,3,2,45,23,55],reversed_cmp)
# 输出 [100, 55, 45, 23, 3, 2]

print '---------返回函数实例---------'

# 正常的求和方法
def ret_sum(*args):
    num=0
    for n in args:
        num=num+n
    return num

print ret_sum(*(1,2,3,4,5))
# 输出结果 15

# 返回函数求和实例
def ret_sum_fun(*args):
    def f():
        num=0
        for n in args:
            num= num+ n
        return num
    return f
f=ret_sum_fun(*(1,2,3,4,5))
print f
# 输出 <function f at 0x000000000265DE48>
print f()
# 输出 15

print '---------装饰器---------'
# 函数对象可以被赋值给变量
def now():
    print '2017-03-16'

f=now
f()
# 输出 2017-03-16

print 'now.__name__:',now.__name__
# 输出结果 now.__name__: now
print 'f.__name__:',f.__name__
# 输出结果 f.__name__: now

# 定义一个装饰器，在执行函数之前打印开始执行，执行完之后打印执行完成
# functools 之后会讲到，暂时记住就ok
import functools
def log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args , **kw):
            print 'begin %s %s():' % (text,func.__name__)
            f=func(*args , **kw)
            print 'end %s %s():' % (text, func.__name__)
            return f
        return wrapper
    return decorator

# 在执行方法之前
@log('exec')
def log_now():
    print '2017-03-16'

@log()
def log_now2():
    print '2017-03-16 2'

log_now()
# 输出 begin exec log_now():
# 2017-03-16
# end exec log_now()
log_now2()
# 输出 begin  log_now2():
# 2017-03-16 2
# end  log_now2():


