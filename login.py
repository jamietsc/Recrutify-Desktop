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

def loginButton(event=None):
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
            subprocess.run(["python", "create_test.py"])
    else:
        # Falsche Anmeldedaten
        messagebox.showwarning("Fehler", "Falscher Benutzername oder Passwort")
        password_entry.delete(0, END)

    conn.close()


login = ttk.Window(themename="superhero")
login.title("Recrutify | Login")
window_width = 500
window_height = 500
login.resizable(False, False)
login.geometry(f"{window_width}x{window_height}")

# Fenster immer in der Mitte des Bildschirms positionieren
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
login.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


# Recrutify Logo
image = ttk.PhotoImage(file="recrutify.png")

# Titel-Label
image_label = ttk.Label(login, anchor="center", image=image)
image_label.pack(pady=20)

# Frame für das Formular erstellen
form_frame = ttk.Frame(login)
form_frame.pack(pady=10)

# Benutzername Label und Entry (Label über Entry, beide linksbündig)
username_label = ttk.Label(form_frame, text="Benutzername", font=("Helvetica", 10, "bold"))
username_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")  # Links ausrichten
username_entry = ttk.Entry(form_frame, font=("Helvetica", 10), width=40)
username_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Links ausrichten mit dem Label

# Passwort Label und Entry (Label über Entry, beide linksbündig)
password_label = ttk.Label(form_frame, text="Passwort", font=("Helvetica", 10, "bold"))
password_label.grid(row=2, column=0, padx=10, pady=(15, 0), sticky="w")  # Links ausrichten
password_entry = ttk.Entry(form_frame, show="●", font=("Helvetica", 10), width=40)
password_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")  # Links ausrichten mit dem Label

# Checkbutton für "Passwort anzeigen"
show_password = ttk.Checkbutton(
    form_frame,
    text="Passwort anzeigen",
    bootstyle="secondary-round-toggle",
    command=toggle_password
)
show_password.grid(row=4, column=0, padx=10, pady=10, sticky="w")  # Links ausrichten

# Login Button
login_button = ttk.Button(login, text="Login", command=loginButton, width=45, style="primary")
login_button.pack(pady=20)

# Binde die Enter-Taste, um den Button auszulösen
login.bind("<Return>", loginButton)

login.mainloop()
