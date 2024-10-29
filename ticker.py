import tkinter as tk
import random
import os
import time

# Datei, die den Text enthält
ticker_file = "tickertext.txt"
last_modified = 0  # Zeitpunkt der letzten Änderung der Datei
current_text = ""  # Aktuell angezeigter Text
timestamp = ""  # Zeitstempel für die letzte Textänderung

# Funktion, um eine zufällige Hintergrundfarbe zu generieren und die Schriftfarbe anzupassen
def random_background_and_text_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    bg_color = f"#{r:02x}{g:02x}{b:02x}"
    
    # Helligkeit berechnen und Textfarbe setzen
    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    text_color = "black" if brightness > 127 else "white"
    
    canvas.config(bg=bg_color)
    canvas.itemconfig(text, fill=text_color)

# Funktion, um den Text aus der Datei zu laden und auf Änderungen zu prüfen
def load_text():
    global last_modified, current_text, timestamp
    if os.path.exists(ticker_file):
        modified_time = os.path.getmtime(ticker_file)
        if modified_time != last_modified:
            last_modified = modified_time
            with open(ticker_file, "r", encoding="utf-8") as f:
                new_text = f.read().strip()
                
            # Wenn der Text sich geändert hat, aktualisiere Text, Hintergrund und Zeitstempel
            if new_text != current_text:
                current_text = new_text
                timestamp = time.strftime("%H:%M:%S - %A, %d.%m.%Y", time.localtime(last_modified))
                update_display_text()  # Text mit neuem Zeitstempel aktualisieren
                random_background_and_text_color()  # Hintergrund und Schriftfarbe anpassen

# Funktion, um den angezeigten Text mit Zeitstempel zu aktualisieren
def update_display_text():
    display_text = f"{timestamp} - {current_text}"
    canvas.itemconfig(text, text=display_text)

# Funktion für den Lauftext
def scroll_text():
    canvas.move(text, -2, 0)
    pos = canvas.coords(text)
    
    # Wenn der Text das Ende erreicht hat, setze ihn zurück
    if pos[0] < -canvas.bbox(text)[2]:
        canvas.move(text, canvas.winfo_width() + canvas.bbox(text)[2], 0)
        
    # Textänderung und Datei prüfen
    load_text()
    
    # Wiederhole den Vorgang alle 20 ms
    root.after(20, scroll_text)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Smooth Scrolling Ticker")

# Canvas-Objekt für den Lauftext mit fester Größe
canvas_width = 4000  # Feste Breite
canvas_height = 100  # Feste Höhe
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Textobjekt hinzufügen
text = canvas.create_text(canvas_width, canvas_height // 2, text="", fill="white", font=("Arial", 28, "bold"), anchor="w")

# Initialen Text laden und Lauftext starten
load_text()
scroll_text()

# Hauptschleife starten
root.mainloop()
