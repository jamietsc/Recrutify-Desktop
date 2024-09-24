import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3

multiple_choice_number = 0
i = 1
multiple_choice_array = [[]]
entry_array = [[]]

frage_entry = 0



def trennlinie():
    global i
    seperator = ttk.Separator(main, orient=HORIZONTAL)
    seperator.place(x=0, y=40 * i, width=1920, height=40)
    i += 1


def newMultipleChoice():
    global i, multiple_choice_array, multiple_choice_number, frage_entry, antwort_1_entry, antwort_2_entry, antwort_3_entry, antwort_4_entry

    if(multiple_choice_number > 0):
        Text = frage_entry.get()
        Antwort_1 = antwort_1_entry.get()
        Antwort_2 = antwort_2_entry.get()
        Antwort_3 = antwort_3_entry.get()
        Antwort_4 = antwort_4_entry.get()

        # Richtige Antwort basierend auf der Auswahl des Radio-Buttons festlegen
        if v.get() == 1:
            Richtig = Antwort_1
        elif v.get() == 2:
            Richtig = Antwort_2
        elif v.get() == 3:
            Richtig = Antwort_3
        elif v.get() == 4:
            Richtig = Antwort_4
        else:
            Richtig = "Keine Auswahl"

        multiple_choice_array.append([Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig])


    # Label und Eingabefeld für die Frage
    frage_label = tkinter.Label(main, text=f"Frage {multiple_choice_number + 1}:")
    frage_label.place(x=500, y=40 * i)
    frage_entry = tkinter.Entry(relief=RIDGE, width=100)
    frage_entry.place(x=600, y=40 * i)
    i += 1

    # Radiobutton und Eingabefelder für Antworten
    antwort_1_radiobutton = tkinter.Radiobutton(main, text="Antwort 1", variable=v, value=1)
    antwort_1_radiobutton.place(x=500, y=40 * i)
    antwort_1_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_1_entry.place(x=600, y=40 * i)
    i += 1

    antwort_2_radiobutton = tkinter.Radiobutton(main, text="Antwort 2", variable=v, value=2)
    antwort_2_radiobutton.place(x=500, y=40 * i)
    antwort_2_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_2_entry.place(x=600, y=40 * i)
    i += 1

    antwort_3_radiobutton = tkinter.Radiobutton(main, text="Antwort 3", variable=v, value=3)
    antwort_3_radiobutton.place(x=500, y=40 * i)
    antwort_3_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_3_entry.place(x=600, y=40 * i)
    i += 1

    antwort_4_radiobutton = tkinter.Radiobutton(main, text="Antwort 4", variable=v, value=4)
    antwort_4_radiobutton.place(x=500, y=40 * i)
    antwort_4_entry = tkinter.Entry(relief=RIDGE, width=100)
    antwort_4_entry.place(x=600, y=40 * i)
    i += 1

    multiple_choice_number += 1


def datenbankEintrag():
    global multiple_choice_array

    Text = frage_entry.get()
    Antwort_1 = antwort_1_entry.get()
    Antwort_2 = antwort_2_entry.get()
    Antwort_3 = antwort_3_entry.get()
    Antwort_4 = antwort_4_entry.get()

    # Richtige Antwort basierend auf der Auswahl des Radio-Buttons festlegen
    if v.get() == 1:
        Richtig = Antwort_1
    elif v.get() == 2:
        Richtig = Antwort_2
    elif v.get() == 3:
        Richtig = Antwort_3
    elif v.get() == 4:
        Richtig = Antwort_4
    else:
        Richtig = "Keine Auswahl"

    multiple_choice_array.append([Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig])

    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('Recrutify.db')  # Datenbank öffnen oder erstellen
    cursor = conn.cursor()

    # Tabelle "Fragen" erstellen, falls sie noch nicht existiert
    cursor.execute('''CREATE TABLE IF NOT EXISTS Fragen (
                        FID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Text TEXT,
                        Antwort_1 TEXT,
                        Antwort_2 TEXT,
                        Antwort_3 TEXT,
                        Antwort_4 TEXT,
                        Richtig TEXT,
                        TID INT,
                        FOREIGN KEY (TID) REFERENCES Test(TID)
                    )''')

    # SQL-Befehl zum Einfügen der Daten
    sql = '''INSERT INTO Fragen(Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig, TID) 
             VALUES (?,?,?,?,?,?,?)'''
    tid = 1

    # Daten in die Datenbank einfügen
    for i in range(0, len(multiple_choice_array)):
        try:
            # Überprüfe, ob die Daten korrekt sind
            print(f"Füge folgende Daten ein: {multiple_choice_array[i]}")
            cursor.execute(sql, (multiple_choice_array[i][0], multiple_choice_array[i][1], multiple_choice_array[i][2], multiple_choice_array[i][3], multiple_choice_array[i][4], multiple_choice_array[i][5], tid))
            print("Daten erfolgreich eingefügt")
        except sqlite3.Error as e:
            print(f"Fehler beim Einfügen der Daten: {e}")

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

    print("Fragen und Antworten wurden in die Datenbank übertragen.")

def arrayLänge():
    print(len(multiple_choice_array))

def arrayAusgeben():
    for i in range(0, len(multiple_choice_array)):
        print(multiple_choice_array[i][0], multiple_choice_array[i][1], multiple_choice_array[i][2], multiple_choice_array[i][3], multiple_choice_array[i][4], multiple_choice_array[i][5])


# GUI-Setup
main = Tk()
main.title("Recutify")
main.state('zoomed')
main.resizable(False, False)

# Variablen müssen nach dem Erstellen des tkinter-Hauptfensters initialisiert werden
v = IntVar()  # Variable für die Radiobuttons
multiple_choice_array.clear()

menu = Menu(main)
main.config(menu=menu)

# Erstellen der Navigationsleiste
filemenu = Menu()
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neue Datei")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Fertigstellen", command=datenbankEintrag)

bausteinemenu = Menu()
menu.add_cascade(label="Bausteine", menu=bausteinemenu)
bausteinemenu.add_command(label="Multiple Choice", command=newMultipleChoice)
bausteinemenu.add_separator()
bausteinemenu.add_command(label="Trennlinie", command=trennlinie)

helpmenu = Menu()
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Fertigstellen (in Arbeit)")
helpmenu.add_command(label="Bausteine (in Arbeit)")


debugmenu = Menu()
menu.add_cascade(label="Debuggen", menu=debugmenu)
debugmenu.add_command(label="Länge Array", command=arrayLänge)
debugmenu.add_command(label="Datenausgeben", command=arrayAusgeben)

main.mainloop()
