# -----hello World------------
print 'Hello World!';

print '---------split---------------';


# -----测试字符串-------------
str = 'Hello World!';
 
print str;           # 输出完整字符串
print str[0];        # 输出字符串中的第一个字符
print str[2:5];      # 输出字符串中第三个至第五个之间的字符串
print str[2:];       # 输出从第三个字符开始的字符串
print str * 2;       # 输出字符串两次
print str + "TEST";  # 输出连接的字符串

print '---------split---------------';

# -----测试LIST-------------
list = [ 'mxgsa', 1111 , 2.23, 'shuaige', 70.2 ];
tinylist = [1111, 'mxgsa'];
print list;               # 输出完整列表
print list[0];            # 输出列表的第一个元素
print list[1:3];          # 输出第二个至第三个的元素 
print list[2:];           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2;       # 输出列表两次
print list + tinylist;    # 打印组合的列表

del list[2];			  # 删除数组元素
print len(list);          # 输出列表长度
print 'mxgsa' in list;    # 元素是否存在于列表中
print list[1:];			  # 从第二个元素开始截取列表
print max(list);		  # 输出列表中最大值
print min(list);		  # 输出列表中最小值


print '---------split---------------';

# -----测试Tuple-------------

tuple = ( 'mxgsa', 1111 , 2.23, 'shuaige', 70.2 );
tinytuple=( 1111, 'mxgsa' );
print tuple;               # 输出完整元组
print tuple[0];            # 输出元组的第一个元素
print tuple[1:3];          # 输出第二个至第三个的元素 
print tuple[2:];           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2;       # 输出元组两次
print tuple + tinytuple;   # 打印组合的元组

print '---------split---------------';

# -----测试赋值-------------

list[2]='mxgsa';		   # 更改list第二个元素
print list;

#tuple[2]='mxgsa';		   # 更改Tuple第二个元素
#print tuple;

print '---------split---------------';

# -----测试dict-------------

dict = {};
dict['one'] = "This is mxgsa";
dict[2] = "This is mxgsa two";
 
tinydict = {'name': 'mxgsa','code':6734, 'dept': 'sales'};
 
 
print dict['one'];          # 输出键为'one' 的值
print dict[2];              # 输出键为 2 的值
print tinydict;             # 输出完整的字典
print tinydict.keys();      # 输出所有键
print tinydict.values();    # 输出所有值

print '---------split---------------';


