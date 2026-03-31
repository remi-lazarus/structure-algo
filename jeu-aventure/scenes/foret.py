"""
=============================================================
  scenes/foret.py — La Forêt Maudite
=============================================================
  RESPONSABLE : Élève 2 (à compléter)

  Objectif pédagogique :
    → Pratiquer la STRUCTURE ALTERNATIVE (SI…ALORS…SINON)
    → Deuxième commit Git sur la branche : scene/foret

  Commandes Git pour cette scène :
    git checkout -b scene/foret
    git add scenes/foret.py
    git commit -m "feat: ajout scène forêt"
    git push origin scene/foret
=============================================================
"""

import random
from moteur.affichage import afficher_scene, narrer, demander_choix, afficher_separateur
from moteur.joueur import Joueur


def scene_foret(joueur: Joueur):
    """
    Scène de la Forêt : rencontre avec un loup et une énigme.

    Structure algorithmique utilisée : ALTERNATIVE
    Chaque choix mène à un résultat différent (SI…ALORS…SINON).
    """
    afficher_scene("La Forêt Maudite")

    narrer("\nLe sentier s'enfonce dans une forêt sombre.")
    narrer("Les branches craquent. Quelque chose vous observe...\n")

    # -------------------------------------------------------
    # COMBAT contre le loup
    # Structure : TANT QUE le loup est vivant ET joueur vivant
    # -------------------------------------------------------
    loup_pv = 30
    loup_force = 8

    narrer("Un LOUP GÉANT DE CACA surgit des buissons !\n")
    print(f"  🐺 Loup Géant — PV : {loup_pv}")

    # --- Boucle de combat (structure répétitive TANT QUE) ---
    while loup_pv > 0 and joueur.est_vivant():
        joueur.afficher_statut()
        print()
        print("Que faites-vous ?")
        choix = demander_choix([
            "Attaquer avec votre épée",
            "Utiliser une potion (si vous en avez)",
            "Tenter de fuir",
            "Déposer le caca"
        ])

        # --- Structure alternative : action selon le choix ---
        if choix == "1":
            # Attaque avec variation aléatoire
            degats = random.randint(joueur.force - 3, joueur.force + 5)
            loup_pv -= degats
            loup_pv = max(0, loup_pv)
            print(f"\n  ⚔️  Vous frappez le loup pour {degats} dégâts ! (PV loup : {loup_pv})")

            # Le loup contre-attaque si encore vivant
            if loup_pv > 0:
                degats_loup = random.randint(loup_force - 2, loup_force + 2)
                joueur.subir_degats(degats_loup)

        elif choix == "2":
            # Structure alternative : a-t-on une potion ?
            if "Potion de soin" in joueur.inventaire:
                joueur.inventaire.remove("Potion de soin")
                joueur.soigner(30)
                print("  (La potion est utilisée.)")
            else:
                print("\n  ⚠️  Vous n'avez pas de potion !")
                # Le loup en profite pour attaquer
                degats_loup = random.randint(loup_force, loup_force + 4)
                print("  Le loup en profite pour vous mordre !")
                joueur.subir_degats(degats_loup)

        elif choix == "3":  # Fuir
            narrer("\nVous tentez de fuir... Le loup vous rattrape !")
            joueur.subir_degats(15)
            narrer("Vous réussissez finalement à vous échapper, mais blessé.")
            return  # On quitte la scène sans victoire
        
        elif choix == "4":
            # Structure alternative : a-ton-envie de faire caca ?
                joueur.CACA += 1
                print("\n(Le caca est déposé.)")
                print("le loup est préoccupé par le caca")
                narrer("Vous arrivez à vous enfuir sans prendre de dégât")
                joueur.afficher_statut()
                return # Quitte la scène en aillant fait caca
        
        
    # --- Résultat du combat ---
    afficher_separateur()
    if joueur.est_vivant():
        narrer("🎉 Vous avez vaincu le Loup Géant !")
        joueur.victoires += 1
        joueur.ramasser("Croc de loup")
        joueur.or_ += 20
        narrer(f"Vous récupérez {20} pièces d'or sur sa carcasse.")
    else:
        narrer("💀 Le loup vous a eu...")
        return

    # -------------------------------------------------------
    # 🎯 MISSION ÉLÈVE 2 — À COMPLÉTER :
    # -------------------------------------------------------
    # 1. Ajouter une énigme après le combat
    #    → Afficher une devinette avec narrer()
    #    → Proposer 3 réponses avec demander_choix()
    #    → SI bonne réponse → objet magique dans inventaire
    #    → SINON → perte de 10 PV
    #
    # 2. Ajouter un marchand ambulant :
    #    → SI joueur.or_ >= 15 → proposer d'acheter une potion
    #    → SINON → "Vous n'avez pas assez d'or..."
    # -------------------------------------------------------
