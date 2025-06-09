import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Nouveaux imports
from chatbot import ouvrir_chatbot
from quiz import ouvrir_quiz
from identification import ouvrir_identification

# Configuration de la fenêtre
root = tk.Tk()
root.title("GÉOLOGIE - Explorer la Terre avec l'IA")
root.geometry("500x500")

# Charger l'image de fond (remplace "geologue_bg.jpg" par ton fichier)
try:
    bg_image = Image.open("geologue_bg.jpg")
    bg_image = bg_image.resize((500, 500), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except FileNotFoundError:
    root.configure(bg="#f0f8ff")  # Fallback si l'image est manquante

# Cadre principal semi-transparent
main_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)

# Style moderne
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", 
                font=("Arial", 12), 
                padding=10, 
                background="#4a6fa5", 
                foreground="white")
style.map("TButton", background=[("active", "#3a5a80")])

# Bannière
banniere = tk.Label(
    main_frame, 
    text="GÉOLOGIE", 
    font=("Arial", 28, "bold"), 
    fg="#2c3e50", 
    bg="white"
)
banniere.pack(pady=20)

# Slogan
slogan = tk.Label(
    main_frame, 
    text="La géologie intelligente, pour tout explorer.", 
    font=("Arial", 10, "italic"), 
    fg="#7f8c8d", 
    bg="white"
)
slogan.pack(pady=5)

# Cadre pour les boutons
frame_boutons = tk.Frame(main_frame, bg="white")
frame_boutons.pack(pady=20)

# Boutons
btn_chatbot = ttk.Button(
    frame_boutons, 
    text="🤖 Chatbot Éducatif", 
    command=ouvrir_chatbot,
    style="TButton"
)
btn_chatbot.pack(pady=10, fill=tk.X)

btn_quiz = ttk.Button(
    frame_boutons, 
    text="📝 Quiz Géologique", 
    command=ouvrir_quiz,
    style="TButton"
)
btn_quiz.pack(pady=10, fill=tk.X)

btn_roche = ttk.Button(
    frame_boutons, 
    text="🪨 Identifier une Roche", 
    command=ouvrir_identification,
    style="TButton"
)
btn_roche.pack(pady=10, fill=tk.X)

root.mainloop()