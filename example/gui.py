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

'''
简单的实例可以这样写

root=Tk()
frame=Frame(root, width=512, height=512)
frame.pack()
w=Label(root, text='Hello, world!')
w.pack()
root.mainloop()
'''


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