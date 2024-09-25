import tkinter
import tkinter.dialog
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

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

def loginButton():
    global versuche
    versuche = 0
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('Recrutify.db')  # Datenbank öffnen oder erstellen
    cursor = conn.cursor()

    username_user = username_entry.get()
    password_user = password_entry.get()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Unternehmen (
                        UID INT PRIMARY KEY,
                        Name VARCHAR(255) NOT NULL,
                        Benutzername VARCHAR (255) NOT NULL,
                        Passwort VARCHAR (255) NOT NULL,
                        Ansprechpartner VARCHAR(255)
                    )''')

    cursor.execute('''SELECT * FROM Unternehmen WHERE Benutzername = ? AND Passwort = ?''', (username_user, password_user))
    result = cursor.fetchone()

    if result:
        print("success")
    else:
        versuche += 1
        if versuche >= 3:
            messagebox.showerror("Fehler", "Melde dich an den Administrator")
        else:
            messagebox.showwarning("Fehler", "Falscher Benutzername oder Passwort")

    conn.close()


login = Tk()
login.title("Recrutify | Login")
login.state('zoomed')
login.resizable(False, False)

start()

login.mainloop()