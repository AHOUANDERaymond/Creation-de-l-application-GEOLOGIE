import tkinter as tk
from tkinter import scrolledtext

def ouvrir_chatbot():
    fenetre = tk.Toplevel()
    fenetre.title("Chatbot Géologique")
    fenetre.geometry("600x400")

    # Zone de discussion
    chat_area = scrolledtext.ScrolledText(fenetre, wrap=tk.WORD, width=70, height=20)
    chat_area.pack(pady=10)

    # Entrée utilisateur
    entry = tk.Entry(fenetre, width=60)
    entry.pack(pady=5)

    # Bouton Envoyer
    def envoyer_question():
        question = entry.get()
        if question:
            chat_area.insert(tk.END, f"Vous: {question}\n")
            reponse = repondre(question)
            chat_area.insert(tk.END, f"Bot: {reponse}\n")
            entry.delete(0, tk.END)

    btn_envoyer = tk.Button(fenetre, text="Envoyer", command=envoyer_question)
    btn_envoyer.pack(pady=5)

# Réponses prédéfinies (à enrichir)
def repondre(question):
    question = question.lower()
    if "roche" in question:
        return "Les roches sont classées en trois types : ignées, sédimentaires et métamorphiques."
    elif "volcan" in question:
        return "Un volcan est une ouverture dans la croûte terrestre qui libère de la lave, des gaz et des cendres."
    else:
        return "Je suis un chatbot éducatif sur la géologie. Posez-moi des questions sur les roches, les minéraux ou les volcans !"