from fltk import *

# Voici un squelette de programme pour le tp1, qu'il vous faudra
# compléter.

# Vous pouvez bien entendu ajouter des fonctions supplémentaires
# ou modifier les paramètres des fonctions définies ici.


# Question 2
def trace_poly(couleur, x, y):
    ...

# Question 4
def dessine_boutons(boutons):
    ...

def detecte_bouton(bouton, x, y):
    ...

def cree_boutons(couleurs):
    ...

# Fonction principale
def main():
    cree_fenetre(800, 600)
    
    couleur = 'black'

    while True:
        ev = donne_ev()
        if ev is not None:
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                trace_poly(couleur, x, y)
            elif tev == 'ClicDroit':
                # à remplir lors de la question 3
                ...
            elif tev == 'Touche' and touche(ev) == 'q':
                # la touche 'q' ferme le programme
                ferme_fenetre()
                exit()

# Ce qui est exécuté lorsque l'on fait "python3 poly.py"
if __name__ == "__main__":
    main()
