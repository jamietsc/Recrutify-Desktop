import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def MultipleChoice():
    # Variable zum Speichern der Auswahl, initialisiert auf False
    correct_answer_1 = tk.BooleanVar(value=False)
    correct_answer_2 = tk.BooleanVar(value=False)
    correct_answer_3 = tk.BooleanVar(value=False)
    correct_answer_4 = tk.BooleanVar(value=False)

    # Frage-Label
    question_label = ttk.Label(create, text="Bitte geben Sie die Frage ein:")
    question_label.pack(pady=10)

    # Eingabefeld für die Frage
    question_entry = ttk.Entry(create, width=100)
    question_entry.pack(pady=5)

    # Rahmen für die Antworten
    answer_frame = ttk.Frame(create)
    answer_frame.pack(pady=10)

    # Antwort 1
    antwort1_label = ttk.Label(answer_frame, text="Antwort 1", font=("Helvetica", 10, "bold"))
    antwort1_label.grid(row=0, column=1, padx=10, pady=(5, 0), sticky="w")

    antwort1_entry_var = tk.StringVar()
    antwort1_entry = ttk.Entry(answer_frame, textvariable=antwort1_entry_var, width=40)
    antwort1_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Checkbox für Antwort 1
    checkbox1 = ttk.Checkbutton(answer_frame, variable=correct_answer_1)
    checkbox1.grid(row=1, column=0, padx=10, pady=5)

    # Antwort 2
    antwort2_label = ttk.Label(answer_frame, text="Antwort 2", font=("Helvetica", 10, "bold"))
    antwort2_label.grid(row=2, column=1, padx=10, pady=(5, 0), sticky="w")

    antwort2_entry_var = tk.StringVar()
    antwort2_entry = ttk.Entry(answer_frame, textvariable=antwort2_entry_var, width=40)
    antwort2_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # Checkbox für Antwort 2
    checkbox2 = ttk.Checkbutton(answer_frame, variable=correct_answer_2)
    checkbox2.grid(row=3, column=0, padx=10, pady=5)

    # Antwort 3
    antwort3_label = ttk.Label(answer_frame, text="Antwort 3", font=("Helvetica", 10, "bold"))
    antwort3_label.grid(row=4, column=1, padx=10, pady=(5, 0), sticky="w")

    antwort3_entry_var = tk.StringVar()
    antwort3_entry = ttk.Entry(answer_frame, textvariable=antwort3_entry_var, width=40)
    antwort3_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    # Checkbox für Antwort 3
    checkbox3 = ttk.Checkbutton(answer_frame, variable=correct_answer_3)
    checkbox3.grid(row=5, column=0, padx=10, pady=5)

    # Antwort 4
    antwort4_label = ttk.Label(answer_frame, text="Antwort 4", font=("Helvetica", 10, "bold"))
    antwort4_label.grid(row=6, column=1, padx=10, pady=(5, 0), sticky="w")

    antwort4_entry_var = tk.StringVar()
    antwort4_entry = ttk.Entry(answer_frame, textvariable=antwort4_entry_var, width=40)
    antwort4_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    # Checkbox für Antwort 4
    checkbox4 = ttk.Checkbutton(answer_frame, variable=correct_answer_4)
    checkbox4.grid(row=7, column=0, padx=10, pady=5)

create = ttk.Window(themename="superhero")
create.title("Recrutify")
create.state('zoomed')  # Vollbildmodus aktivieren
create.resizable(False, False)

menu = tk.Menu(create)
create.config(menu=menu)

# Erstellen der Navigationsleiste
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neue Datei")
filemenu.add_command(label="Speichern")
filemenu.add_command(label="Fertigstellen")
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=exit)

bausteinemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Fragen hinzufügen", menu=bausteinemenu)
bausteinemenu.add_command(label="Single Choice", command=MultipleChoice)
bausteinemenu.add_command(label="Multiple Choice")
bausteinemenu.add_separator()
bausteinemenu.add_command(label="Neuer Abschnitt")

helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Hilfe", menu=helpmenu)
helpmenu.add_command(label="Fertigstellen (in Arbeit)")
helpmenu.add_command(label="Bausteine (in Arbeit)")

create.mainloop()