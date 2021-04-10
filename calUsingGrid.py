from tkinter import *
class SimpleCal:
    def __init__(self):
        self.container = Tk()
        self.container.iconbitmap("hapus.ico")
        self.screenFm = Frame(self.container)
        self.screenFm.pack()
        self.answer = StringVar()
        self.screen =Entry(self.screenFm, textvariable=self.answer, width =14, font=('arial',20), state="disable",disabledbackground="white" )
        self.screen.pack()
        self.buttonFm = Frame(self.container)
        self.buttonFm.pack()
        Button(self.buttonFm,text="1", width = 5, command=lambda: self.getValues('1')).grid(row =0, column =0, padx=5, pady=5)
        Button(self.buttonFm,text="2", width = 5, command=lambda: self.getValues('2')).grid(row =0, column =1, padx=5, pady=5)
        Button(self.buttonFm,text="3", width = 5, command=lambda: self.getValues('3')).grid(row =0, column =2, padx=5, pady=5)
        Button(self.buttonFm,text="+", width = 5, command=lambda: self.operate('+')).grid(row =0, column =3, padx=5, pady=5)
        Button(self.buttonFm,text="4", width = 5, command=lambda: self.getValues('4')).grid(row =1, column =0, padx=5, pady=5)
        Button(self.buttonFm,text="5", width = 5, command=lambda: self.getValues('5')).grid(row =1, column =1, padx=5, pady=5)
        Button(self.buttonFm,text="6", width = 5, command=lambda: self.getValues('6')).grid(row =1, column =2, padx=5, pady=5)
        Button(self.buttonFm,text="-", width = 5, command=lambda: self.operate('-')).grid(row =1, column =3, padx=5, pady=5)
        Button(self.buttonFm,text="7", width = 5, command=lambda: self.getValues('7')).grid(row =2, column =0, padx=5, pady=5)
        Button(self.buttonFm,text="8", width = 5, command=lambda: self.getValues('8')).grid(row =2, column =1, padx=5, pady=5)
        Button(self.buttonFm,text="9", width = 5, command=lambda: self.getValues('9')).grid(row =2, column =2, padx=5, pady=5)
        Button(self.buttonFm,text="X", width = 5, command=lambda: self.operate('*')).grid(row =2, column =3, padx=5, pady=5)
        Button(self.buttonFm,text="0", width = 5, command=lambda: self.getValues('0')).grid(row =3, column =0, padx=5, pady=5)
        Button(self.buttonFm,text=".", width = 5, command=lambda: self.getValues('.')).grid(row =3, column =1, padx=5, pady=5)
        Button(self.buttonFm,text="C", width = 5, command= self.clear).grid(row =3, column =2, padx=5, pady=5)
        Button(self.buttonFm,text="/", width = 5, command=lambda: self.operate('/')).grid(row =3, column =3, padx=5, pady=5)
        Button(self.buttonFm,text="=", width = 5, command=self.calculate).grid(row =4, column =0, columnspan=2, padx=5, pady=5)
        self.but = Button(self.buttonFm, text="OFF", width =5, command =self.offon)
        self.but.grid(row=4, column=3, columnspan=2, padx=5, pady=5)
        self.state = "off"
        self.answer.set(0)
        self.result = 0
        # self.screen.get()
        self.container.mainloop()

    def getValues(self, value):
        if self.screen.get()  != " ":
            if self.screen.get() =="0" or self.result ==1:
                self.answer.set(value)
            else:
                self.answer.set(self.screen.get() + value)
                self.result = 0

    def operate(self, op):
        if self.screen.get() != " ":
            self.operate = op
            self.fval = float(self.screen.get())
            self.answer.set(0)    
    def clear(self):
       if self.screen.get() != " ":
           self.answer.set(0)

    def calculate(self):
        if self.screen.get() != " ":
            self.sval = float(self.screen.get())
            if self.operate == "+":
                self.answer.set(self.fval + self.sval)
                self.result = 1
            elif self.operate =="-":
                self.answer.set(self.fval - self.sval)
                self.result = 1
            elif self.operate =="*":
                self.answer.set(self.fval * self.sval)
                self.result = 1
            elif self.operate =="/":
                self.answer.set(self.fval / self.sval)
                self.result = 1

    def offon(self):
        if self.state =="on":
            self.answer.set(0)
            self.state = "off"
            self.but.configure(text="OFF")
        else:
            self.answer.set(" ")
            self.state = "on"
            self.but.configure(text ="ON")
bm = SimpleCal()



