import tkinter as tk
from tkinter import filedialog, messagebox
import json

# Charger la base de données des roches (à créer dans data/roches.json)
def charger_roches():
    try:
        with open("data/roches.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def ouvrir_identification():
    fenetre = tk.Toplevel()
    fenetre.title("Identifier une Roche")
    fenetre.geometry("500x400")

    # Champ de description
    lbl_description = tk.Label(fenetre, text="Décris la roche (couleur, texture, etc.) :")
    lbl_description.pack(pady=10)

    entry_description = tk.Entry(fenetre, width=50)
    entry_description.pack(pady=5)

    # Bouton d'analyse
    def analyser_description():
        description = entry_description.get().lower()
        roches = charger_roches()
        if not roches:
            messagebox.showerror("Erreur", "Base de données des roches introuvable !")
            return

        resultats = []
        for roche in roches:
            if any(mot_cle in description for mot_cle in roche["mots_cles"]):
                resultats.append(roche["nom"])

        if resultats:
            messagebox.showinfo("Résultats", f"Roches possibles : {', '.join(resultats)}")
        else:
            messagebox.showinfo("Aucun résultat", "Aucune roche ne correspond à cette description.")

    btn_analyser = tk.Button(fenetre, text="Analyser", command=analyser_description)
    btn_analyser.pack(pady=10)

    # Bouton d'upload d'image (simulé)
    btn_image = tk.Button(fenetre, text="📷 Uploader une image (simulation)", command=lambda: messagebox.showinfo("Fonctionnalité future", "L'analyse d'image sera ajoutée plus tard !"))
    btn_image.pack(pady=10)