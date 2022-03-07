import tkinter as tk

window = tk.Tk()

window.minsize(650,400)
window.maxsize(650,400)
window.geometry("550x300")
window.title("Hangman")

arme = tk.PhotoImage(file="Assets/Arme.gif")
beine = tk.PhotoImage(file="Assets/Beine.gif")
kopf = tk.PhotoImage(file="Assets/Kopf.gif")
koerper = tk.PhotoImage(file="Assets/Körper.gif")
pfahl = tk.PhotoImage(file="Assets/Pfahl.gif")
seil = tk.PhotoImage(file="Assets/Seil.gif")

#Überschrift
lbl_ueb = tk.Label(window, text="Hangman", font=("Comic Sans MS", 30, "bold underline"))
#Button zum Starten des Spiels
btn_play = tk.Button(window, text="Spielen", font=("Comic Sans MS", 20, "bold"))



#grid
lbl_ueb.grid(row=0, column=0,padx=(240,0), pady=(5,0))
btn_play.grid(row=1, column=0, padx=(240,0), pady=(100, 0))

window.mainloop()
