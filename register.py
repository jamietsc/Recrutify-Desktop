import tkinter
import tkinter.dialog
from tkinter import *
import sqlite3
from tkinter import messagebox, Frame, Label
import subprocess
import ttkbootstrap as ttk

def toggle_password():
    if password_entry.cget('show') == '●':
        password_entry.config(show='')
    else:
        password_entry.config(show='●')

def check_fields():
    # Aktivieren des Buttons, wenn alle Felder ausgefüllt sind
    if (unternehmen_entry_var.get() and ansprechpartner_entry_var.get() and
            username_entry_var.get() and password_entry_var.get()):
        register_button.config(state=NORMAL)
    else:
        register_button.config(state=DISABLED)

def registerButton(event=None):
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('Recrutify.db')  # Datenbank öffnen oder erstellen
    cursor = conn.cursor()

    unternehmen = unternehmen_entry_var.get()
    ansprechpartner = ansprechpartner_entry_var.get()
    username = username_entry_var.get()
    password = password_entry_var.get()

    # Tabelle erstellen (falls noch nicht vorhanden)
    cursor.execute('''CREATE TABLE IF NOT EXISTS Unternehmen (
                        UID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name VARCHAR(255) NOT NULL,
                        Benutzername VARCHAR(255) NOT NULL,
                        Passwort VARCHAR(255) NOT NULL,
                        Ansprechpartner VARCHAR(255),
                        is_admin BOOLEAN NOT NULL DEFAULT 0)''')

    # Daten einfügen
    cursor.execute('''INSERT INTO Unternehmen (Name, Benutzername, Passwort, Ansprechpartner) 
                      VALUES (?, ?, ?, ?)''', (unternehmen, username, password, ansprechpartner))

    # Änderungen in die Datenbank schreiben
    conn.commit()

    # Erfolgsmeldung anzeigen
    messagebox.showinfo("Erfolg", "Unternehmen wurde erfolgreich registriert")

    # Felder leeren
    unternehmen_entry.delete(0, END)
    ansprechpartner_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # Datenbankverbindung schließen
    conn.close()

register = ttk.Window(themename="superhero")
register.title("Recrutify | Registrierung")
register.state('zoomed')  # Vollbildmodus aktivieren
register.resizable(False, False)

image = ttk.PhotoImage(file="recrutify.png")

# Recrutify-Logo
image_label = ttk.Label(register, anchor="center", image=image)
image_label.pack(pady=20)

# Titel-Label
title_label = ttk.Label(register, anchor="center", text="Registrierung neuer Unternehmen", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Frame für das Formular erstellen
form_frame = ttk.Frame(register)
form_frame.pack(pady=10)

# Unternehmen
unternehmen_label = ttk.Label(form_frame, text="Unternehmen", font=("Helvetica", 10, "bold"))
unternehmen_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")

unternehmen_entry_var = StringVar()
unternehmen_entry = ttk.Entry(form_frame, textvariable=unternehmen_entry_var, width=40)
unternehmen_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Korrektur: hier ist das Entry in Row 1

# Ansprechpartner
ansprechpartner_label = ttk.Label(form_frame, text="Ansprechpartner", font=("Helvetica", 10, "bold"))
ansprechpartner_label.grid(row=2, column=0, padx=10, pady=(5, 0), sticky="w")

ansprechpartner_entry_var = StringVar()
ansprechpartner_entry = ttk.Entry(form_frame, textvariable=ansprechpartner_entry_var, width=40)
ansprechpartner_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Benutzername
username_label = ttk.Label(form_frame, text="Benutzername", font=("Helvetica", 10, "bold"))
username_label.grid(row=4, column=0, padx=10, pady=(5, 0), sticky="w")

username_entry_var = StringVar()
username_entry = ttk.Entry(form_frame, textvariable=username_entry_var, width=40)
username_entry.grid(row=5, column=0, padx=10, pady=5, sticky="w")

# Passwort
password_label = ttk.Label(form_frame, text="Passwort", font=("Helvetica", 10, "bold"))
password_label.grid(row=6, column=0, padx=10, pady=(5, 0), sticky="w")

password_entry_var = StringVar()
password_entry = ttk.Entry(form_frame, textvariable=password_entry_var, show="●", width=40)
password_entry.grid(row=7, column=0, padx=10, pady=5, sticky="w")

# Registrieren-Button
register_button = ttk.Button(form_frame, text="Registrieren", command=registerButton, state=DISABLED, style="primary", width=38)
register_button.grid(row=9, column=0, padx=10, pady=(20, 10), sticky="w")

# Checkbutton für "Passwort anzeigen"
show_password = ttk.Checkbutton(
    form_frame,
    text="Passwort anzeigen",
    bootstyle="secondary-round-toggle",
    command=toggle_password
)
show_password.grid(row=8, column=0, padx=10, pady=10, sticky="w")  # Links ausrichten

# Überwachung der Textänderungen in den Eingabefeldern
unternehmen_entry_var.trace("w", lambda *args: check_fields())
ansprechpartner_entry_var.trace("w", lambda *args: check_fields())
username_entry_var.trace("w", lambda *args: check_fields())
password_entry_var.trace("w", lambda *args: check_fields())

register.bind("<Return>", registerButton)

register.mainloop()
