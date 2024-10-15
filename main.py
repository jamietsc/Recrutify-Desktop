import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import ttkbootstrap as tbk

multiple_choice_number = 0
multiple_choice_array = []

# GUI-Setup
main = Tk()
style = tbk.Style("superhero")
main.title("Recrutify")
main.state('zoomed')
main.resizable(False, False)


# Frame to hold canvas and scrollbar                                         
frame = Frame(main)
frame.pack(fill=BOTH, expand=True)

# Create a canvas
canvas = Canvas(frame)
canvas.pack(side=TOP, fill=BOTH, expand=True)

# Add a scrollbar to the canvas
scrollbar = Scrollbar(frame, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas scroll command
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the content
content_frame = Frame(canvas)

# Add a window (content_frame) inside the canvas, anchored at the top center ("n")
canvas.create_window((canvas.winfo_width() / 2, 0), window=content_frame, anchor="n")

# Update scroll region dynamically when the window size changes
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.create_window((canvas.winfo_width() / 2, 0), window=content_frame, anchor="n")

# Bind the window resize event to the update_scroll_region function
canvas.bind("<Configure>", update_scroll_region)

def trennlinie():
    # Add a separator to content_frame (which is inside the canvas)
    seperator = ttk.Separator(content_frame, orient=HORIZONTAL)
    seperator.pack(fill="x", pady=10)

def exit():
    main.destroy()

class MultipleChoice:
    def __init__(self, master, question_number):
        self.master = master
        self.question_number = question_number
        self.v1 = tkinter.BooleanVar()
        self.v2 = tkinter.BooleanVar()
        self.v3 = tkinter.BooleanVar()
        self.v4 = tkinter.BooleanVar()
        self.create_question()

    def create_question(self):
        # Frame to center the question and answers horizontally
        question_frame = Frame(self.master)
        question_frame.pack(pady=20)

        # Center the whole frame inside content_frame
        question_frame.pack(pady=20, anchor="center")

        # Question label and entry (centered)
        question_label = Label(question_frame, text=f"Frage {self.question_number + 1}:", font=("Helvetica", 10, "bold"))
        question_label.grid(row=0, column=0, padx=10)

        self.question_entry = Entry(question_frame, width=70)
        self.question_entry.grid(row=0, column=1, padx=10)

        # Answer options with checkbuttons (centered)
        self.create_answer_option(question_frame, self.v1, "Antwort 1", 1)
        self.create_answer_option(question_frame, self.v2, "Antwort 2", 2)
        self.create_answer_option(question_frame, self.v3, "Antwort 3", 3)
        self.create_answer_option(question_frame, self.v4, "Antwort 4", 4)

    def create_answer_option(self, frame, var, text, row):
        # Create checkbutton and entry side by side in the same row
        answer_checkbutton = Checkbutton(frame, variable=var)
        answer_checkbutton.grid(row=row, column=0, padx=10)

        answer_entry = Entry(frame, width=70)
        answer_entry.grid(row=row, column=1, padx=10)

        # Store the entry reference
        if text == "Antwort 1":
            self.answer_1_entry = answer_entry
        elif text == "Antwort 2":
            self.answer_2_entry = answer_entry
        elif text == "Antwort 3":
            self.answer_3_entry = answer_entry
        elif text == "Antwort 4":
            self.answer_4_entry = answer_entry

    def get_question_entry(self):
        return self.question_entry.get()
    
    def get_answer_entries(self):
        return [
            self.answer_1_entry.get(),
            self.answer_2_entry.get(),
            self.answer_3_entry.get(),
            self.answer_4_entry.get()
        ]
    
    def get_selected_answer(self):
        return [
            self.v1.get(),
            self.v2.get(),
            self.v3.get(),
            self.v4.get()
        ]

def newMultipleChoice():
    global multiple_choice_number, multiple_choice_array
    
    # Create a new multiple choice question inside content_frame
    mc = MultipleChoice(content_frame, multiple_choice_number)
    multiple_choice_array.append(mc)
    multiple_choice_number += 1
    trennlinie()

    # Update scroll region
    canvas.config(scrollregion=canvas.bbox("all"))


def zeitlimit():
    global dauer  # Zugriff auf die globale Variable, um die Zeit zu speichern
    
    zeit = tbk.Window(themename="superhero")
    zeit.title("Recrutify | Zeit einstellen")
    window_width = 300
    window_height = 150
    zeit.resizable(False, False)
    zeit.geometry(f"{window_width}x{window_height}")

    screen_width = zeit.winfo_screenwidth()
    screen_height = zeit.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    zeit.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    zeit_label = Label(zeit, text="Zeit in Minuten:", font=("Helvetica", 10, "bold"))
    zeit_label.place(x=55, y=55)

    zeit_entry = Entry(zeit, relief=RIDGE, width=10)
    zeit_entry.place(x=160, y=55)

    def buttonClick():
        global dauer  # Zeitwert speichern
        try:
            dauer = int(zeit_entry.get())  # Die Eingabe wird in ein int konvertiert
            datenbankEintrag()
            zeit.destroy()  # Schließt das Fenster nach der Eingabe
            messagebox.showinfo("Erfolgreich","Eingegebene Zeit: " + str(dauer) + " Minuten")  # Debug-Ausgabe
        except ValueError:
            messagebox.showwarning("Fehler","Ungültige Eingabe, bitte eine Zahl eingeben.")  # Falls die Eingabe ungültig ist
        

    zeit_button = Button(zeit, text="OK", width=15, command=buttonClick)
    zeit_button.place(x=100, y=85)

    zeit.mainloop()


def datenbankEintrag():
    global multiple_choice_array

    conn = sqlite3.connect(r'Z:\BachelorOfScience-Informatik\3. Semester\Software_Engeneering\Recutrify_Desktop_Anwendung\Recrutify\Recrutify.db')
    cursor = conn.cursor()

    # Tabelle MultipleChoiceFragen erstellen
    cursor.execute('''CREATE TABLE IF NOT EXISTS MultipleChoiceFragen(
                        FID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Text TEXT,
                        Antwort_1 TEXT,
                        Antwort_2 TEXT,
                        Antwort_3 TEXT,
                        Antwort_4 TEXT,
                        Richtig_1 BOOLEAN,
                        Richtig_2 BOOLEAN,
                        Richtig_3 BOOLEAN,
                        Richtig_4 BOOLEAN,
                        TID INT,
                        FOREIGN KEY (TID) REFERENCES Test(TID)
                    )''')

    # Tabelle Test erstellen
    cursor.execute('''CREATE TABLE IF NOT EXISTS Test(
                        TID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Dauer INTEGER,
                        UID INT,
                        FOREIGN KEY (UID) REFERENCES Unternehmen(UID)
                    )''')

    # TID holen und erhöhen
    cursor.execute('''SELECT MAX(TID) FROM Test''')
    result = cursor.fetchone()
    
    if result[0] is None:
        TID = 1  # Setze TID auf 1, wenn noch keine Tests existieren
    else:
        TID = result[0] + 1  # Erhöhe die TID um 1
    
    """cursor.execute('''SELECT UID FROM Unternehmen WHERE Benutzername = ? AND Passwort = ?''', (login.get_username(), login.get_password()))
    UID = cursor.fetchone()
    if UID is None:
        print("Fehler: Ungültige Login-Daten.")
        return """

    # SQL-Befehl für das Einfügen von Daten in die Tabelle MultipleChoiceFragen
    sql = '''INSERT INTO MultipleChoiceFragen(Text, Antwort_1, Antwort_2, Antwort_3, Antwort_4, Richtig_1, Richtig_2, Richtig_3, Richtig_4, TID) 
             VALUES (?,?,?,?,?,?,?,?,?,?)'''

    # SQL-Befehl für das Einfügen von Daten in die Tabelle Test
    sql1 = '''INSERT INTO Test(TID, Dauer, UID)
              VALUES(?, ?, ?)'''

    for mc in multiple_choice_array:
        try:
            question = mc.get_question_entry()
            answers = mc.get_answer_entries()
            selected_answers = mc.get_selected_answer()  # Liste der richtigen Antworten (Booleans)
            
            # Prüfe, ob alle Felder ausgefüllt sind
            if question.strip() == "" or any(answer.strip() == "" for answer in answers):
                print(f"Fehler: Eine Frage oder Antwort ist leer.")
                continue  # Überspringt diesen Datensatz, wenn leere Felder gefunden werden

            # Führe den SQL-Befehl aus und füge die Frage und Antworten in die Tabelle ein
            cursor.execute(sql, (question, answers[0], answers[1], answers[2], answers[3],
                                 selected_answers[0], selected_answers[1], selected_answers[2], selected_answers[3],
                                 TID))
            cursor.execute(sql1, (TID, dauer, 7))
            print("Daten erfolgreich eingefügt")
        except sqlite3.Error as e:
            print(f"Fehler beim Einfügen der Daten: {e}")

    

    conn.commit()
    conn.close()

    print("Fragen und Antworten wurden in die Datenbank übertragen.")


def arrayLänge():
    print(len(multiple_choice_array))

def arrayAusgeben():
    for mc in multiple_choice_array:
        print(mc.get_question_entry(), mc.get_answer_entries(), mc.get_selected_answer())

def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

menu = Menu(main)
main.config(menu=menu)


filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neue Datei")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Fertigstellen", command=zeitlimit)
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=exit)

bausteinemenu = Menu(menu)
menu.add_cascade(label="Bausteine", menu=bausteinemenu)
bausteinemenu.add_command(label="Single Choice", command=newMultipleChoice)
bausteinemenu.add_separator()
bausteinemenu.add_command(label="Trennlinie", command=trennlinie)

helpmenu = Menu(menu)
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Fertigstellen (in Arbeit)")
helpmenu.add_command(label="Bausteine (in Arbeit)")

debugmenu = Menu(menu)
menu.add_cascade(label="Debuggen", menu=debugmenu)
debugmenu.add_command(label="Länge Array", command=arrayLänge)
debugmenu.add_command(label="Datenausgeben", command=arrayAusgeben)

main.mainloop()
