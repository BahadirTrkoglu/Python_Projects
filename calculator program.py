#calculator program

from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text
    try:
      total = str(eval(equation_text))

      equation_label.set(total)
      equation_text= total
    except ZeroDivisionError:
        equation_label.set("aritmethic error")

        equation_text = ""

    except SyntaxError:
        equation_label.set("SyntaxError")

        equation_text = ""

def clear():
   global equation_text

   equation_label.set("")
   equation_text = ""

def bahadir():
    global equation_text
    equation_text = "Bahadır made this program:)"
    equation_label.set(equation_text)

window=Tk()
window.title("Calculator program")
window.geometry("450x624")

equation_text =""

equation_label = StringVar()

label = Label(window, textvariable = equation_label, font=('consolas',20), bg="black",fg="#22f259", width=29,height=3)
label.pack()


frame  = Frame(window)
frame.pack()

button1= Button(frame, text=1, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(1))
button1.grid(row=0,column=0)


button2= Button(frame, text=2, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(2))
button2.grid(row=0,column=1)

button3= Button(frame, text=3, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(3))
button3.grid(row=0,column=2)

button4= Button(frame, text=4, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(4))
button4.grid(row=1,column=0)

button5= Button(frame, text=5, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(5))
button5.grid(row=1,column=1)

button6= Button(frame, text=6, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(6))
button6.grid(row=1,column=2)

button7= Button(frame, text=7, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(7))
button7.grid(row=2,column=0)

button8= Button(frame, text=8, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(8))
button8.grid(row=2,column=1)


button9= Button(frame, text=9, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(9))
button9.grid(row=2,column=2)

button0= Button(frame, text=0, height=4 , width=9, font=35,bg="#aeb1b8",fg="black",
                command=lambda : button_press(0))
button0.grid(row=3,column=0)

plus= Button(frame, text='+', height=4 , width=9, font=35,bg="gray",fg="white",
                command=lambda : button_press('+'))
plus.grid(row=0,column=3)

minus= Button(frame, text='-', height=4 , width=9, font=35,bg="gray",fg="white",
                command=lambda : button_press('-'))
minus.grid(row=1,column=3)

multipy= Button(frame, text='*', height=4 , width=9, font=35,bg="gray",fg="white",
                command=lambda : button_press('*'))
multipy.grid(row=2,column=3)

devide= Button(frame, text='/', height=4 , width=9, font=35,bg="gray",fg="white",
                command=lambda : button_press('/'))
devide.grid(row=3,column=3)

equal= Button(frame, text='=', height=4 , width=9, font=35,bg="gray",fg="white",
                command=equals)
equal.grid(row=3, column=2)

decimal= Button(frame, text='.', height=4 , width=9, font=35,bg="gray",fg="white",
                command=lambda : button_press('.'))
decimal.grid(row=3,column=1)

clear = Button(frame, text='clear', height=4 , width=9, font=35,bg="gray",fg="white",
                command=clear)
clear.grid(row=4,column=0)

bahadir = Button(frame, text='Respect', height=4 , width=9, font=35,bg="gray",fg="white",
                command=bahadir)
bahadir.grid(row=4,column=1)

window.mainloop()