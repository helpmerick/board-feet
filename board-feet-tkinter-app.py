from tkinter import *

window = Tk()
window.title("BFCalc")
window.geometry("525x800")
window.resizable(width=False,height=False)
E1Val = StringVar()
E1_value = StringVar()
E2_value = StringVar()
E3_value = StringVar()

answers = []

def CalculateNum(event):
    LengthVal = float(E1_value.get())
    WidthVal = float(E2_value.get())
    ThicknessVal = float(E3_value.get())

    FinalCalc = LengthVal * WidthVal * ThicknessVal / 144
    FinalCalc = round(FinalCalc,2)
    answers.append(FinalCalc)

    E4.delete(0,"end")
    E4.insert(END,FinalCalc)
    T1.insert(END,f'{FinalCalc}\n')
    Total()
    TotalBoards()

def Total():
    tot = 0
    for num in answers:
        tot += num
   
    E5.delete(0,"end")
    E5.insert(END,round(tot,2))

def ClearVal():
    E1.delete(0,"end")
    E2.delete(0,"end")
    E3.delete(0,"end")
    E4.delete(0,"end")
    E3.insert(0,'1')

def TotalBoards():
    E6.delete(0,"end")
    E6.insert(END,len(answers))

def ClearList():
    T1.delete('1.0',END)
    E5.delete(0,"end")
    E6.delete(0,"end")
    answers.clear()

L1 = Label(text="Board Foot Calculator",font='Helvetica 20 bold underline')
L1.pack()

L2 = Label(text="Input in Inches",font='Helvetica 16 bold underline')
L2.pack(pady=10)

L3 = Label(text="Length",font='Helvetica 14 bold italic')
L3.pack()

E1 = Entry(window,font='Goudy 14 bold',textvariable=E1_value)
E1.pack()

L4 = Label(text="Width",font='Helvetica 14 bold italic')
L4.pack()

E2 = Entry(window,font='Goudy 14 bold',textvariable=E2_value)
E2.pack()

L5 = Label(text="Thickness",font='Helvetica 14 bold italic')
L5.pack()

E3 = Entry(window,font='Goudy 14 bold',textvariable=E3_value)
E3.insert(0,'1')
E3.pack()

B1 = Button(window,text="Calculate",font='Helvetica 14 bold',height=2,width=15)
B1.bind("<Button-1>",CalculateNum)
B1.bind("<KeyPress-Return>",CalculateNum)
B1.pack(pady=40)

L6 = Label(text="Board Feet",font='Helvetica 16 bold italic')
L6.pack()

E4 = Entry(window,font='Goudy 14 bold')
E4.pack()

B2 = Button(window,text="Clear",font='Helvetica 14 bold',height=2,width=10,command=ClearVal)
B2.pack(pady=40)

B3 = Button(window,text="Clear List",font='Helvetica 14 bold',height=2,width=10,command=ClearList)
B3.pack()

L9 = Label(text="Total Boards:",font='Goudy 14 bold')
L9.place(x=50,y=740)

E6 = Entry(window,font='Goudy 16 bold')
E6.place(x=250,y=740)

L7 = Label(text="Coded by Lucio (C) 2020",font='Goudy 12')
L7.pack()

T1 = Text(window,width=10,height=34,font='Goudy 12')
T1.place(x=400,y=50)

E5 = Entry(window,font='Goudy 16 bold')
E5.place(x=250,y=700)

L8 = Label(text="Total Board Feet:",font='Goudy 14 bold')
L8.place(x=50,y=700)

window.mainloop()
