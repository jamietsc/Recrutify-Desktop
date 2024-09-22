import tkinter
from tkinter import *

multiple_choice_number = 1
v = int

def newMultipleChoice():
    i = 1
    frage_label = tkinter.Label(main, text="Frage:")
    frage_label.place(x= 500, y=40 * i)
    frage_entry = tkinter.Entry(relief=RIDGE, width= 100)
    frage_entry.place(x=600, y=40 * i)
    i += 1

    antwort_1_radiobutton = tkinter.Radiobutton(main, text="Antwort 1", variable=v, value=1)
    antwort_1_radiobutton.place(x=500, y=40 * i)
    antwort_1_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_1_entry.place(x=600, y=40 * i)
    i += 1

    antwort_2_radiobutton = tkinter.Radiobutton(main, text="Antwort 2", variable=v, value=2)
    antwort_2_radiobutton.place(x=500, y= 40 * i)
    antwort_2_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_2_entry.place(x=600, y = 40 * i)
    i += 1

    antwort_3_radiobutton = tkinter.Radiobutton(main, text="Antwort 3", variable=v, value=3)
    antwort_3_radiobutton.place(x=500, y= 40 * i)
    antwort_3_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_3_entry.place(x=600, y = 40 * i)
    i += 1

    antwort_4_radiobutton = tkinter.Radiobutton(main, text="Antwort 4", variable=v, value=4)
    antwort_4_radiobutton.place(x=500, y= 40 * i)
    antwort_4_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_4_entry.place(x=600, y = 40 * i)
    i += 1

    Text = str(frage_entry.get())
    Antwort_1 = str(antwort_1_entry.get())
    Antwort_2 = str(antwort_2_entry.get())
    Antwort_3 = str(antwort_3_entry.get())
    Antwort_4 = str(antwort_4_entry.get())

    if(v == 1):
        Richtig = Antwort_1
    elif(v == 2):
        Richtig = Antwort_2
    elif(v == 3):
        Richtig = Antwort_3
    elif(v == 4):
        Richtig = Antwort_4
    else:
        Richtig = "Leer"

    multiple_choice_array = [[Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig]]


#def datenbankEintrag():




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
bausteinemenu.add_command(label="")

helpmenu = Menu()
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Fertigstellen")
helpmenu.add_command(label="Bausteine")

main.mainloop()