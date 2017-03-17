# coding=utf-8

__author__ = 'mengxg'


# 自定义函数
'''
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''

# 定义一个根据考试分数判定是 优秀 良好 及格 不及格 输出单个结果
# 输入分数
# 输出 判定结果
def my_single_output(score):
    if score<60:
        return '不及格';
    elif score>=60 and score<75 :
        return '及格'
    elif score>=75 and score<85 :
        return  '良好'
    else :
        return  '优秀'

print '90分的判定结果：' + my_single_output(90);
print '70分的判定结果：' + my_single_output(70);
print '80分的判定结果：' + my_single_output(80);
print '30分的判定结果：' + my_single_output(30);

# 自己输入分数,这里就不做类型错误判断了
score = float(raw_input('请输入考试分数：'));

# int类型输出要进行转换字符串 str()
print str(score) + '分的判定结果：' + my_single_output(score);



# 引入math数学计算库
import math;

# 游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
# 输入当前的坐标，位移，角度(给定默认零度，可以不传值）
# 输出 当前坐标
def my_mulite_output(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = my_mulite_output(200, 200, 60, math.pi / 6)
print x,y
# x,y 输出 251.961524227 170.0

z = my_mulite_output(200, 200, 60, math.pi / 6)
print z;
# z 输出(251.96152422706632, 170.0) 其实还是一个值，就是tuple的值

# 定义一个空函数，就需要用的pass，不然会报错的

def empty():
    pass

empty();

# 可变参数 定义 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
def collect(*args):
    sum=0;
    for n in args:
        sum+=n
    print 'collect:',sum

# 进行调用，可以使用多个方法
collect(1,2,3,4,5)
a=(1,2,3,4,5)
collect(*a)

# 关键字函数定义 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def animal(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

# 进行调用，可以使用多个方法
animal('dog',1,color='red',eat='rich')
kw={'color':'red','eat':'rich'}
animal('dog',1,**kw)