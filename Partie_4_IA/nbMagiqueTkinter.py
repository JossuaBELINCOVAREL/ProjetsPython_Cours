# Ici, on s'essaie à l'IA en générant avec GPT et modifiant au fur et à mesure...

import random
import tkinter as tk

# Définir le nombre de vies et le nombre maximal comme des constantes
NOMBRE_DE_VIES = 3
NOMBRE_MAXIMAL = 20

class JeuNombreMagique:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Nombre Magique")

        self.initialiser_jeu()

    def initialiser_jeu(self):
        # Réinitialiser les variables
        self.nombre_magique = random.randint(1, NOMBRE_MAXIMAL)
        self.vies = NOMBRE_DE_VIES

        # Effacer les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()

        # Interface utilisateur
        self.label = tk.Label(self.root, text="Bienvenue dans le jeu du Nombre Magique !\nDevinez le nombre entre 1 et {}.".format(NOMBRE_MAXIMAL))
        self.label.pack(pady=10)

        self.message = tk.Label(self.root, text="Il vous reste {} vies.".format(self.vies))
        self.message.pack(pady=5)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=5)

        # Créer des boutons pour chaque nombre possible, sur plusieurs lignes
        for i in range(1, NOMBRE_MAXIMAL + 1):
            bouton = tk.Button(self.buttons_frame, text=str(i), command=lambda i=i: self.verifier_supposition(i))
            bouton.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)

        self.restart_button = None

    def verifier_supposition(self, guess):
        # Désactiver le bouton cliqué
        for widget in self.buttons_frame.winfo_children():
            if widget.cget("text") == str(guess):
                widget.config(state=tk.DISABLED)

        if guess == self.nombre_magique:
            self.message.config(text="Félicitations! Vous avez deviné le nombre magique.", fg="green")
            for widget in self.buttons_frame.winfo_children():
                widget.config(state=tk.DISABLED)
            self.afficher_bouton_relancer()
        else:
            self.vies -= 1
            if self.vies > 0:
                if guess < self.nombre_magique:
                    self.message.config(text="Trop bas! Essayez un nombre plus grand. Il vous reste {} vies.".format(self.vies), fg="orange")
                else:
                    self.message.config(text="Trop haut! Essayez un nombre plus petit. Il vous reste {} vies.".format(self.vies), fg="orange")
            else:
                self.message.config(text="Désolé, vous n'avez plus de vies. Le nombre magique était {}.".format(self.nombre_magique), fg="red")
                for widget in self.buttons_frame.winfo_children():
                    widget.config(state=tk.DISABLED)
                self.afficher_bouton_relancer()

    def afficher_bouton_relancer(self):
        self.restart_button = tk.Button(self.root, text="Relancer le jeu", command=self.initialiser_jeu)
        self.restart_button.pack(pady=10)

# Créer l'application Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    jeu = JeuNombreMagique(root)
    root.mainloop()
