import tkinter as tk

def scroll_text():
    # Bewege den Text nach links
    canvas.move(text, -2, 0)  # Geschwindigkeit ist hier -2 (je kleiner, desto langsamer)
    pos = canvas.coords(text)
    
    # Wenn der Text das Ende erreicht hat, setze ihn zurück
    if pos[0] < -canvas.bbox(text)[2]:
        canvas.move(text, canvas.winfo_width() + canvas.bbox(text)[2], 0)
        
    # Wiederhole den Vorgang alle 20 ms für einen smoothen Lauftext
    root.after(20, scroll_text)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Smooth Scrolling Text")

# Canvas-Objekt für den Lauftext erstellen
canvas = tk.Canvas(root, width=1500, height=100, bg="white")
canvas.pack()

# Text hinzufügen (passt hier die Nachricht an)
message = "Dies ist ein Beispiel für einen smoothen Lauftext, wie ein Newsticker im Fernsehen!"
text = canvas.create_text(canvas.winfo_width(), 50, text=message, fill="black", font=("Arial", 24, "bold"), anchor="w")

# Starte den Lauftext
scroll_text()

# Hauptschleife starten
root.mainloop()
