"""
=============================================================
  scenes/caverne.py — La Caverne des Échos
=============================================================
  RESPONSABLE : Élève 3 (à compléter)

  Objectif pédagogique :
    → Pratiquer les BOUCLES : POUR et TANT QUE
    → Troisième commit Git sur la branche : scene/caverne

  Commandes Git pour cette scène :
    git checkout -b scene/caverne
    git add scenes/caverne.py
    git commit -m "feat: ajout scène caverne"
    git push origin scene/caverne
=============================================================
"""

import random
from moteur.affichage import afficher_scene, narrer, demander_choix, afficher_separateur
from moteur.joueur import Joueur


def scene_caverne(joueur: Joueur):
    """
    Scène de la Caverne : pièges, coffres et un troll endormi.

    Structures algorithmiques utilisées :
      - POUR … FAIRE   → explorer les salles de la caverne
      - TANT QUE … FAIRE → désamorcer un piège
    """
    afficher_scene("La Caverne des Échos")

    narrer("\nVous descendez un escalier de pierre humide.")
    narrer("La caverne s'étend sur plusieurs salles...\n")

    # -------------------------------------------------------
    # Exploration des salles — Structure POUR … FAIRE
    # On parcourt 3 salles numérotées dans l'ordre
    # -------------------------------------------------------
    salles = ["Salle des Champignons", "Salle du Trésor", "Salle du Troll"]
    objets_possibles = ["Torche magique", "Épée rouillée", "Carte du donjon"]

    # --- POUR chaque salle FAIRE ---
    for numero, nom_salle in enumerate(salles, 1):
        afficher_separateur()
        narrer(f"Salle {numero}/3 : {nom_salle}")

        # Événement aléatoire dans chaque salle
        evenement = random.randint(1, 3)

        if evenement == 1:
            # Trouver un objet
            objet = objets_possibles[numero - 1]
            narrer(f"\nVous trouvez quelque chose par terre...")
            print("Ramassez-vous l'objet ?")
            choix = demander_choix(["Oui, je le prends", "Non, trop risqué"])
            if choix == "1":
                joueur.ramasser(objet)

        elif evenement == 2:
            # Piège — Structure TANT QUE : désamorcer en trouvant le bon code
            narrer("\n⚠️  Un piège à pression ! Vous devez entrer le bon code.")
            narrer("Le code est un chiffre entre 1 et 5.\n")

            code_secret = random.randint(1, 5)
            tentatives = 0
            max_tentatives = 3
            desamorce = False

            # --- TANT QUE tentatives restantes ET piège actif ---
            while tentatives < max_tentatives and not desamorce:
                tentatives += 1
                print(f"  Tentative {tentatives}/{max_tentatives}")
                try:
                    essai = int(input("  Code > ").strip())
                    if essai == code_secret:
                        narrer("  ✅ Bon code ! Le piège est désamorcé.")
                        desamorce = True
                    elif essai < code_secret:
                        print("  📉 Trop petit...")
                    else:
                        print("  📈 Trop grand...")
                except ValueError:
                    print("  ⚠️  Entrez un chiffre valide.")

            # --- Structure alternative : résultat ---
            if not desamorce:
                narrer(f"\n  Le piège se déclenche ! Code secret : {code_secret}")
                joueur.subir_degats(20)
            else:
                joueur.or_ += 10
                narrer("  Vous trouvez 10 pièces d'or derrière le panneau !")

        else:
            # Rien de particulier
            narrer("\nLa salle est vide. Vous avancez prudemment.")

        joueur.afficher_statut()

    # -------------------------------------------------------
    # Boss de la caverne : le Troll endormi
    # -------------------------------------------------------
    afficher_separateur()
    narrer("Dans la dernière salle, un TROLL est profondément endormi.")
    print("\nQue faites-vous ?")
    choix = demander_choix([
        "Passer discrètement sans le réveiller",
        "L'attaquer pendant qu'il dort",
        "Lui voler son trésor puis fuir"
    ])

    if choix == "1":
        narrer("\nVous retenez votre souffle et passez sans un bruit. Ouf !")
    elif choix == "2":
        narrer("\nAttaque surprise ! Vous infligez de lourds dégâts.")
        narrer("Le troll furieux riposte !")
        joueur.subir_degats(25)
        joueur.victoires += 1
        joueur.or_ += 30
        narrer("Victoire ! Vous récupérez 30 pièces d'or.")
    else:
        narrer("\nVous saisissez le trésor... mais le troll se réveille !")
        joueur.subir_degats(15)
        joueur.or_ += 15
        narrer("Vous fuyez avec 15 pièces d'or !")

    # -------------------------------------------------------
    # 🎯 MISSION ÉLÈVE 3 — À COMPLÉTER :
    # -------------------------------------------------------
    # 1. Ajouter une 4ème salle "Salle des Cristaux"
    #    → Utiliser une boucle POUR pour collecter des cristaux
    #    → POUR i allant de 1 à 3 : proposer de ramasser cristal_i
    #
    # 2. Modifier le piège : ajouter un indice après chaque
    #    mauvaise tentative (chaud/froid)
    #
    # 3. Ajouter une condition sur l'inventaire :
    #    → SI "Torche magique" dans inventaire → bonus exploration
    # -------------------------------------------------------
