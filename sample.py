# coding=utf-8

# 打印等边三角形 注意print后面的的","，不能省略，可以起到不换行的作用
print "打印空心等边三角形"
rows = int( raw_input('输入列数：') )
blank = " "
edge = '*'

for i in range(0, rows + 1):
    for j in range(0, rows - i):
        print blank,
        j += 1
    for k in range(0, 2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:#因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print edge,
                else:
                    print blank,
            else:
               print edge,
        else:
            print blank,
        k += 1
    print "\n"
    i += 1