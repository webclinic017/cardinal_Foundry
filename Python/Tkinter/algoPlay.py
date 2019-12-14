from tkinter import *
import tkinter.messagebox


# Settings=======
algoPlay = Tk()
algoPlay.title('KnowThyComplexities')
algoPlay.geometry("500x300")
color = 'gray87'
algoPlay.configure(bg=color)
algoPlay.resizable(width=False, height=False)
# Body ========
v = IntVar()
res = IntVar()

Label(algoPlay, text="Steps", bg=color).place(x=5, y=100)
ip = Entry(algoPlay, width=20, bd=2, insertwidth=2)
ip.place(x=100, y=100)

btn_cal = Button(algoPlay, text="Cal", command=lambda: cal(), highlightbackground=color)
btn_cal.place(x=5, y=150)

Label(algoPlay, text="Result", bg=color).place(x=5, y=200)
result = Entry(algoPlay, textvariable=res).place(x=100, y=200)


label = Label(algoPlay, text=" Make your choice! ", bg=color).place(x=5, y=3)

Radiobutton(algoPlay, text="Factorial Sum", padx=20, variable=v, value=1, bg=color).place(x=5, y=30)
Radiobutton(algoPlay, text="Recursive Sum", padx=20, variable=v, value=2, bg=color).place(x=5, y=50)
Radiobutton(algoPlay, text="Fibonnaci Sum", padx=20, variable=v, value=3, bg=color).place(x=5, y=70)



# Functions ============
def cal():
    ip_int = int(ip.get())
    if v.get() == 1:
        res.set(fact_sum(ip_int))
    elif v.get() == 2:
        res.set(rec_sum(ip_int))
    elif v.get() == 3:
        res.set(fibonnaci_sum(ip_int))
def fact_sum(n):
    if n==0:
        return 1
    else:
        return n * fact_sum(n-1)
def rec_sum(n):
    if n == 0:
        return 0
    else :
        return n + rec_sum(n-1)
def fibonnaci_sum(n):
    if n <= 1:
        return n
    else :
        return fibonnaci_sum(n-1) + fibonnaci_sum(n-2)
# The End ==========
algoPlay.mainloop()
