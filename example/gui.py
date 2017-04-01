#!/usr/bin/env python
# -*- coding: utf-8 -*-

'使用python进行图形界面编程'

__author__ = 'mengxg'

'''
本文要点：
1、使用Tkinter进行GUI编程
'''


from Tkinter import *
import tkMessageBox


# 简单的实例可以这样写

# 使用Tkinter进行GUI编程
def tkinter_demo():
    # 创建一个主窗口
    root=Tk()
    # 设置主窗口的初始大小
    root.geometry('300x300')
    # 创建容器，负责安排其他部件的位置
    frame=Frame(root)
    frame.pack()
    # 创建一个输入框
    helloText=Entry(root)
    helloText.pack()
    # 按钮点击事件
    def ok_click():
        txt = helloText.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % txt)
    w=Label(root, text='Hello, world!')
    w.pack()
    # 创建一个按钮
    button=Button(root ,text= 'OK',command = ok_click)
    button.pack()
    # 进入主事件循环
    root.mainloop()

import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "My Frame", size = (300, 300))
		panel = wx.Panel(self, -1)
		panel.Bind(wx.EVT_MOTION, self.OnMove)
		wx.StaticText(panel, -1, "Pos:", pos = (10, 12))
		self.posCtrl = wx.TextCtrl(panel, -1, "", pos = (40, 10))

	def OnMove(self, event):
		pos = event.GetPosition()
		self.posCtrl.SetValue("%s, %s" %(pos.x, pos.y))
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show(True)
	app.MainLoop()





# 大的一些项目可以这样来写，封装到一个类里面
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.helloText=Entry(self)
        self.helloText.pack()
        self.quitButton = Button(self, text='Get Text', command=self.ok)
        self.quitButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
    def ok(self):
        txt=self.helloText.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % txt)


app=Application()
app.master.title='hello world'
app.mainloop()
