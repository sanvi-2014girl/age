from tkinter import *
#screen
window = Tk()
window.title("tkinter GUI")
window.geometry('500x500')
window.configure(bg='pink')
#add widgets
x = Label(text = "Hey welcome to codingal!",bg="#ff0000", fg = "white")
x.pack()
#entry
age = Entry(window,width= 30)
age.pack()

#label
L = Label(window,text="",bg = "blue",fg="white",width = 50)
L.pack()
#btn function
def sayhello():
    num1 = int(age.get())
    
    cal = num1 - 2024
    L.config(text="Result is:"+str(cal))
#btn
b = Button(window, text="click here!",command= sayhello)
b.pack()
window.mainloop()