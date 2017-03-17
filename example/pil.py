#!/usr/bin/env python
# -*- coding: utf-8 -*-

'生成随机验证码图片'

__author__='mengxg'

# 从PIL导入Image,ImageDraw,ImageFont,ImageFilter
# Image 类是 PIL 库中一个非常重要的类，通过这个类来创建实例可以有直接载入图像文件，读取处理过的图像和通过抓取的方法得到的图像
# ImageDraw ImageDraw模块提供了图像对象的简单2D绘制。用户可以使用这个模块创建新的图像，注释或润饰已存在图像，为web应用实时产生各种图形。
# ImageFont 创建字体对象给ImageDraw中的text函数使用。
# ImageFilter模块提供了滤镜相关定义；这些滤波器主要用于Image类的filter()方法。
from PIL import Image,ImageDraw,ImageFont,ImageFilter
# 引入随机函数
import random

# 生成随机字符串
def rndChar():
    return chr(random.randint(65,90))

# 生成随机的颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#生成文字的随机颜色
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 图片的宽度
width=60*4
# 图片的高度
height=60
# 生成空白图片对象
image=Image.new('RGB',(width,height),(255,255,255))
# 设置图片文字的字体
font=ImageFont.truetype('C:\\WINDOWS\\Fonts\\SIMYOU.TTF',36)
# 创建一个可用来对image进行操作的对象
draw=ImageDraw.Draw(image)

#对图片背景进行颜色填充
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
# 随机生成字符画到图片上
for t in range(4):
    draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())
# 对图片进行模糊处理
image=image.filter(ImageFilter.BLUR)
# 保存图片到当前目录
image.save('code.jpg','jpeg')