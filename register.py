import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox

def start():
    global username_entry, password_entry, unternehmen_entry, ansprechpartner_entry, register_button
    global unternehmen_entry_var, ansprechpartner_entry_var, username_entry_var, password_entry_var

    unternehmen_label = tkinter.Label(register, text="Unternehmen: ")
    unternehmen_label.place(x=500, y=40)
    ansprechpartner_label = tkinter.Label(register, text="Ansprechpartner: ")
    ansprechpartner_label.place(x=500, y=80)
    username_label = tkinter.Label(register, text="Benutzername: ")
    username_label.place(x=500, y=120)
    password_label = tkinter.Label(register, text="Passwort: ")
    password_label.place(x=500, y=160)

    unternehmen_entry_var = StringVar()
    unternehmen_entry = Entry(register, textvariable=unternehmen_entry_var)
    unternehmen_entry.place(x=600, y=40)

    ansprechpartner_entry_var = StringVar()
    ansprechpartner_entry = Entry(register, textvariable=ansprechpartner_entry_var)
    ansprechpartner_entry.place(x=600, y=80)

    username_entry_var = StringVar()
    username_entry = Entry(register, textvariable=username_entry_var)
    username_entry.place(x=600, y=120)

    password_entry_var = StringVar()
    password_entry = Entry(register, textvariable=password_entry_var, show="*")
    password_entry.place(x=600, y=160)

    register_button = tkinter.Button(register, text="Registrieren", command=registerButton, state=DISABLED)
    register_button.place(x=600, y=200)

    # Überwachung der Textänderungen in den Eingabefeldern
    unternehmen_entry_var.trace("w", lambda *args: check_fields())
    ansprechpartner_entry_var.trace("w", lambda *args: check_fields())
    username_entry_var.trace("w", lambda *args: check_fields())
    password_entry_var.trace("w", lambda *args: check_fields())

    register.bind("<Return>", registerButton)

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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Unternehmen (
            UID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(255) NOT NULL,
            Benutzername VARCHAR(255) NOT NULL,
            Passwort VARCHAR(255) NOT NULL,
            Ansprechpartner VARCHAR(255),
            is_admin BOOLEAN NOT NULL DEFAULT 0);
            ''')

    # Daten einfügen
    cursor.execute('''
        INSERT INTO Unternehmen (Name, Benutzername, Passwort, Ansprechpartner) 
        VALUES (?, ?, ?, ?)
    ''', (unternehmen, username, password, ansprechpartner))

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

register = Tk()
register.title("Recrutify | Registrierung")
register.state('zoomed')
register.resizable(False, False)

start()

register.mainloop()
