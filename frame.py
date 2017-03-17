from Tkinter import *

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
        #tkMessageBox.showinfo('Message', 'Hello, %s' % txt)




app=Application()
app.master.title='hello world'
app.mainloop()