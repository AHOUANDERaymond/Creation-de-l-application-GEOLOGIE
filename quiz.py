import tkinter as tk
from tkinter import messagebox
import json
import random

# Charger les questions (à créer dans data/questions.json)
def charger_questions():
    try:
        with open("data/questions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def ouvrir_quiz():
    fenetre = tk.Toplevel()
    fenetre.title("Quiz Géologique")
    fenetre.geometry("500x400")

    questions = charger_questions()
    if not questions:
        messagebox.showerror("Erreur", "Aucune question trouvée !")
        return

    # Mélanger les questions
    random.shuffle(questions)
    current_question = 0
    score = 0

    # Affichage de la question
    lbl_question = tk.Label(fenetre, text="", wraplength=400, font=("Helvetica", 12))
    lbl_question.pack(pady=20)

    # Boutons de réponse
    frame_reponses = tk.Frame(fenetre)
    frame_reponses.pack()

    def afficher_question():
        nonlocal current_question
        if current_question < len(questions):
            q = questions[current_question]
            lbl_question.config(text=q["question"])
            for widget in frame_reponses.winfo_children():
                widget.destroy()
            for reponse in q["reponses"]:
                btn = tk.Button(frame_reponses, text=reponse, command=lambda r=reponse: verifier_reponse(r, q["reponse_correcte"]))
                btn.pack(pady=5)
        else:
            messagebox.showinfo("Quiz Terminé", f"Score final : {score}/{len(questions)}")
            fenetre.destroy()

    def verifier_reponse(reponse_choisie, reponse_correcte):
        nonlocal score, current_question
        if reponse_choisie == reponse_correcte:
            score += 1
            messagebox.showinfo("Correct !", "Bonne réponse !")
        else:
            messagebox.showerror("Incorrect", f"La bonne réponse était : {reponse_correcte}")
        current_question += 1
        afficher_question()

    afficher_question()