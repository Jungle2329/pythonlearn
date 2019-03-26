from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    # 初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # 按钮
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton1 = Button(self, command=self.fword, text='点我你试试啊？')
        # 输入框
        self.nameInput = Entry(self)
        self.ageInput = Entry(self)
        self.createWidgets()

    # 创建
    def createWidgets(self):
        self.pack()
        self.nameInput.pack()
        self.ageInput.pack()
        self.alertButton.pack()
        # self.alertButton1.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        age = self.ageInput.get()
        messagebox.showinfo('Message', 'Hello, %s age=%s' % (name, age))

    def fword(self):
        messagebox.showerror('dd0', '123')


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
