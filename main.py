import tkinter
from tkinter import *

place_var = 0

def newMultipleChoice():
    i = 0
    frage_label = tkinter.Label(main, text="Frage:")
    frage_label.place(x= 500, y=40 * i)
    frage_entry = tkinter.Entry(relief=RIDGE, width= 100)
    frage_entry.place(x=600, y=40 * i)
    i += 1

    antwort_1_label = tkinter.Label(main, text="Antwort 1")
    antwort_1_label.place(x=500, y=40 * i)
    antwort_1_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_1_entry.place(x=600, y=40 * i)
    i += 1

    antwort_2_label = tkinter.Label(main, text="Antwort 2")
    antwort_2_label.place(x=500, y= 40 * i)
    antwort_2_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_2_entry.place(x=600, y = 40 * i)
    i += 1

    antwort_3_label = tkinter.Label(main, text="Antwort 3")
    antwort_3_label.place(x=500, y= 40 * i)
    antwort_3_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_3_entry.place(x=600, y = 40 * i)
    i += 1

    antwort_4_label = tkinter.Label(main, text="Antwort 4")
    antwort_4_label.place(x=500, y= 40 * i)
    antwort_4_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_4_entry.place(x=600, y = 40 * i)
    i += 1








main = Tk()
main.title("Recutify")
main.state('zoomed')
main.resizable(False, False)

menu = Menu(main)
main.config(menu=menu)

#Erstellen der Navigationsleiste
filemenu = Menu()
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neue Datei")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Fertigstellen")

bausteinemenu = Menu()
menu.add_cascade(label="Bausteine", menu=bausteinemenu)
bausteinemenu.add_command(label="Multiple Choice", command=newMultipleChoice)

helpmenu = Menu()
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Fertigstellen")
helpmenu.add_command(label="Bausteine")

main.mainloop()