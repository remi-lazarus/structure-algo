"""
=============================================================
  scenes/intro.py — Scène d'introduction
=============================================================
  RESPONSABLE : Élève 1 (à compléter)

  Objectif pédagogique :
    → Pratiquer la STRUCTURE SÉQUENTIELLE
    → Premier commit Git sur la branche : scene/intro

  Commandes Git pour cette scène :
    git checkout -b scene/intro
    git add scenes/intro.py
    git commit -m "feat: ajout scène intro"
    git push origin scene/intro
=============================================================
"""

from moteur.affichage import afficher_scene, narrer, demander_choix
from moteur.joueur import Joueur


def scene_intro(joueur: Joueur):
    """
    Scène d'introduction : le joueur se réveille dans une forêt.

    Structure algorithmique utilisée : SÉQUENTIELLE
    Les actions s'enchaînent dans l'ordre, sans condition.
    """
    afficher_scene("Le réveil")

    # --- Narration séquentielle ---
    narrer(f"\nVous ouvrez les yeux. Vous êtes {joueur.nom}, un aventurier égaré.")
    narrer("Autour de vous : des arbres immenses, une brume épaisse.")
    narrer("Un vieux sac est posé à vos pieds.\n")

    # --- Choix : fouiller ou non le sac ---
    print("Que faites-vous ?")
    choix = demander_choix([
        "Fouiller le sac",
        "Ignorer le sac et avancer"
    ])

    # --- Structure alternative : conséquence du choix ---
    if choix == "1":
        narrer("\nVous ouvrez le sac et trouvez une potion de soin !")
        joueur.ramasser("Potion de soin")
        joueur.or_ += 5
        narrer("Vous trouvez aussi 5 pièces d'or.")
    else:
        narrer("\nVous laissez le sac et avancez prudemment.")
        narrer("Dommage... il contenait peut-être quelque chose d'utile.")

    joueur.afficher_statut()

    # -------------------------------------------------------
    # 🎯 MISSION ÉLÈVE 1 — À COMPLÉTER :
    # -------------------------------------------------------
    # 1. Ajouter une deuxième scène narrative (narrer(...))
    # 2. Proposer un autre objet à ramasser
    # 3. Ajouter une énigme simple avec demander_choix()
    #    → Si bonne réponse : bonus de PV (joueur.soigner(10))
    #    → Si mauvaise réponse : perte de PV (joueur.subir_degats(5))
    # -------------------------------------------------------


narrer("fouiller le donjon")