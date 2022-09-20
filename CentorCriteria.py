from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import font

win = Tk()
win.title('Centor Criteria')
win.geometry("550x520")


def display_about():
    messagebox.showinfo('About', "*Usually pharyngitis is viral and doesn't require antibiotic treatment. \n \n**The Centor Score predicts which patients will have higher likelihood of streptococcal infections. \n \n***This helps determine which patients to test and lowers overprescription rates of antibiotics.")

menubar = Menu(win)

menubar.add_cascade(label='About', command=display_about)
menubar.add_cascade(label='Exit', command=win.quit)
win.config(menu= menubar)



def display_error():
    msg = messagebox.showerror('Error', 'This criteria is meant for patients with age 3 and above')



def display_input():
    score = var1.get() + var2.get() + var3.get() + var4.get() + var5.get()
    if score in range(0, 2):
        messagebox.showinfo('Result', "No antibiotics or testing")
    elif score == 2:
        messagebox.showinfo('Result', 'Optional rapid strep testing and/or culture')
    elif score == 3:
        messagebox.showinfo('Result', 'Consider rapid strep testing and/or culture')
    elif score >= 4:
        messagebox.showinfo('Result', 'Empiric antibiotic')


# Define empty variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()


# Define a Checkbox
label = Label(win, pady=10, text='Use only in patients with recent onset (=<3days) acute pharyngitis', font='Ariel')
label.pack()
spacer1 = Label(win, text="")
spacer1.pack()
frame2 = LabelFrame(win, relief='sunken', text='Signs & Symptoms', pady=5)
frame2.pack()
t1 = Checkbutton(frame2, pady=3, text="Fever>38°c", font='Calibri', variable=var1, onvalue=1, offvalue=0)
t1.pack(anchor='w')
t2 = Checkbutton(frame2, pady=3, text="Tonsillar Exudate", font='Calibri', variable=var2, onvalue=1, offvalue=0)
t2.pack(anchor='w')
t3 = Checkbutton(frame2, pady=3, text="Absence of Cough", font='Calibri', variable=var3, onvalue=1, offvalue=0)
t3.pack(anchor='w')
t4 = Checkbutton(frame2, pady=3, text="Anterior Cervical LAD", font='Calibri', variable=var4, onvalue=1, offvalue=0)
t4.pack(anchor='w')
spacer1 = Label(win, text="")
spacer1.pack()
frame1= LabelFrame(win, relief='sunken', text='Age Group', pady=5)
frame1.pack()
t8 = Radiobutton(frame1, pady=3, text="Age under 3 years", font='Calibri', variable=var5, value=5, command=display_error)
t8.pack(anchor='w')
t5 = Radiobutton(frame1, pady=3, text="Age 3-14 years", font='Calibri', variable=var5, value=1)
t5.pack(anchor='w')
t6 = Radiobutton(frame1, pady=3, text="Age 15-44 years", font='Calibri', variable=var5, value=0)
t6.pack(anchor='w')
t7 = Radiobutton(frame1, pady=3, text="Age over 44", font='Calibri', variable=var5, value=-1)
t7.pack(anchor='w')
spacer1 = Label(win, text="")
spacer1.pack()
button = tkinter.Button(win, pady=4, bd=10, text='Show results', width=20, bg='White', foreground='black', activebackground='black',
                        activeforeground='white', font='Georgia' , command=display_input)
button.pack()

win.mainloop()
