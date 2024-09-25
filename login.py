import tkinter
import tkinter.dialog
from tkinter import *
import sqlite3
from tkinter import messagebox
import subprocess

def start():
    global username_entry, password_entry

    username_label = tkinter.Label(login, text="Benutzername: ")
    username_label.place(x=500, y=40)
    password_label = tkinter.Label(login, text="Passwort: ")
    password_label.place(x=500, y=80)

    username_entry = Entry(login)
    username_entry.place(x=600, y=40)
    password_entry = Entry(login, show="*")
    password_entry.place(x=600, y=80)

    login_button = tkinter.Button(login, text="Login", command=loginButton)
    login_button.place(x=600, y=120)
    login.bind("<Return>", loginButton)

def loginButton(event=None):
    global versuche
    versuche = 0

    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('Recrutify.db')  # Datenbank öffnen oder erstellen
    cursor = conn.cursor()

    username_user = username_entry.get()
    password_user = password_entry.get()

    # Tabelle erstellen (falls noch nicht vorhanden)
    cursor.execute('''CREATE TABLE IF NOT EXISTS Unternehmen (
                        UID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name VARCHAR(255) NOT NULL,
                        Benutzername VARCHAR(255) NOT NULL,
                        Passwort VARCHAR(255) NOT NULL,
                        Ansprechpartner VARCHAR(255),
                        is_admin BOOLEAN NOT NULL DEFAULT 0
                    )''')

    # Benutzername und Passwort abfragen
    cursor.execute('''SELECT is_admin FROM Unternehmen WHERE Benutzername = ? AND Passwort = ?''', (username_user, password_user))
    result = cursor.fetchone()

    if result:
        is_admin = result[0]  # Holen des is_admin-Werts

        if is_admin:
            # Wenn der Benutzer ein Admin ist, zur Registrierungsseite weiterleiten
            login.destroy()
            subprocess.run(["python", "register.py"])
        else:
            # Wenn kein Admin, zur Hauptseite weiterleiten
            login.destroy()
            subprocess.run(["python", "main.py"])
    else:
        # Falsche Anmeldedaten
        messagebox.showwarning("Fehler", "Falscher Benutzername oder Passwort")
        password_entry.delete(0, END)

    conn.close()


login = Tk()
login.title("Recrutify | Login")
login.state('zoomed')
login.resizable(False, False)

start()

login.mainloop()