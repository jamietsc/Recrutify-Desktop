import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3

multiple_choice_number = 1
i = 1

def trennlinie():
    seperator = ttk.Separator(main, orient=HORIZONTAL)
    seperator.place(x=0, y=40*i, width=1920, height=40)
def newMultipleChoice():
    global i
    frage_label = tkinter.Label(main, text="Frage:")
    frage_label.place(x=500, y=40 * i)
    frage_entry = tkinter.Entry(relief=RIDGE, width=100)
    frage_entry.place(x=600, y=40 * i)
    i += 1

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

    def save_data():
        # Hier werden die Daten erst beim Klicken auf den Button gelesen
        Text = frage_entry.get()
        Antwort_1 = antwort_1_entry.get()
        Antwort_2 = antwort_2_entry.get()
        Antwort_3 = antwort_3_entry.get()
        Antwort_4 = antwort_4_entry.get()

        # Prüfen, ob die Daten korrekt abgerufen werden
        print("Frage:", Text)
        print("Antwort 1:", Antwort_1)
        print("Antwort 2:", Antwort_2)
        print("Antwort 3:", Antwort_3)
        print("Antwort 4:", Antwort_4)
        print("Richtige Antwort:", v.get())

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
            Richtig = "Leer"

        print("Richtig:", Richtig)

        # Daten in die Datenbank einfügen
        datenbankEintrag(Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig)
        fertig_button.destroy()

    # "Fertig"-Button erstellen und save_data als command übergeben
    fertig_button = tkinter.Button(main, text="Fertig", command=save_data)
    fertig_button.place(x=500, y=40 * i)

def datenbankEintrag(frage, antwort_1, antwort_2, antwort_3, antwort_4, richtig):
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
    sql = '''INSERT INTO Fragen (Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig, TID)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''

    # Beispiel für TID, muss möglicherweise dynamisch oder aus einem anderen Input kommen
    tid = 1  # Dies sollte an deine Test-ID angepasst werden

    # Daten einfügen
    try:
        cursor.execute(sql, (frage, antwort_1, antwort_2, antwort_3, antwort_4, richtig, tid))
        print("Daten erfolgreich eingefügt")
    except sqlite3.Error as e:
        print(f"Fehler beim Einfügen der Daten: {e}")

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

# GUI-Setup
main = Tk()
main.title("Recutify")
main.state('zoomed')
main.resizable(False, False)

# Variablen müssen nach dem Erstellen des tkinter-Hauptfensters initialisiert werden
v = IntVar()  # Variable für die Radiobuttons

menu = Menu(main)
main.config(menu=menu)

# Erstellen der Navigationsleiste
filemenu = Menu()
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neue Datei")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Fertigstellen")

bausteinemenu = Menu()
menu.add_cascade(label="Bausteine", menu=bausteinemenu)
bausteinemenu.add_command(label="Multiple Choice", command=newMultipleChoice)
bausteinemenu.add_command(label="")
bausteinemenu.add_separator()
bausteinemenu.add_command(label="Trennlinie", command=trennlinie)

helpmenu = Menu()
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Fertigstellen")
helpmenu.add_command(label="Bausteine")

main.mainloop()
