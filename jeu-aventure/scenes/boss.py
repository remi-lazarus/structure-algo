"""
=============================================================
  scenes/boss.py — Le Boss Final : Le Sorcier du Code
=============================================================
  RESPONSABLE : Élève 4 (à compléter)

  Objectif pédagogique :
    → Mobiliser TOUTES les structures algorithmiques
    → Commit final sur la branche : scene/boss

  Commandes Git pour cette scène :
    git checkout -b scene/boss
    git add scenes/boss.py
    git commit -m "feat: ajout boss final"
    git push origin scene/boss
=============================================================
"""

import random
from moteur.affichage import afficher_scene, narrer, demander_choix, afficher_separateur
from moteur.joueur import Joueur


# -------------------------------------------------------
# Données du boss (constantes)
# -------------------------------------------------------
BOSS_NOM = "Sorcier du Code"
BOSS_PV_MAX = 80
BOSS_FORCE = 12


def afficher_combat(joueur: Joueur, boss_pv: int, boss_nom: str):
    """Affiche l'état du combat en cours."""
    barre_boss = "█" * (boss_pv // 10) + "░" * ((BOSS_PV_MAX - boss_pv) // 10)
    print(f"\n  🧙 {boss_nom} | PV [{barre_boss}] {boss_pv}/{BOSS_PV_MAX}")
    joueur.afficher_statut()
    print()


def scene_boss(joueur: Joueur):
    """
    Boss final : combat contre le Sorcier du Code.

    Mobilise TOUTES les structures :
      - Séquentielle : narration et préparation
      - Alternative  : choix d'actions et effets spéciaux
      - TANT QUE     : boucle de combat principale
      - POUR         : phases de sorts (attaques multiples)
    """
    afficher_scene("La Tour du Sorcier — Boss Final")

    narrer("\nAu sommet de la tour, une silhouette vous attend.")
    narrer(f"C'est lui : le {BOSS_NOM} !")
    narrer('"Tu as survécu jusqu\'ici... Impressionnant. Mais ça s\'arrête là !"\n')

    # --- Préparation : bonus selon l'inventaire ---
    bonus_attaque = 0
    if "Croc de loup" in joueur.inventaire:
        bonus_attaque += 3
        narrer("🐺 Le Croc de loup vous donne +3 en force !")
    if "Épée rouillée" in joueur.inventaire:
        bonus_attaque += 2
        narrer("⚔️  L'Épée rouillée vous donne +2 en force !")

    force_effective = joueur.force + bonus_attaque

    # --- Variables du boss ---
    boss_pv = BOSS_PV_MAX
    tour = 0
    esquive_active = False

    afficher_separateur()
    narrer("⚔️  COMBAT FINAL !\n")

    # -------------------------------------------------------
    # Boucle de combat — Structure TANT QUE … FAIRE
    # On continue tant que les deux adversaires sont en vie
    # -------------------------------------------------------
    while boss_pv > 0 and joueur.est_vivant():
        tour += 1
        print(f"  ─── Tour {tour} ───")
        afficher_combat(joueur, boss_pv, BOSS_NOM)

        # --- Tour spécial : le sorcier lance une salve ---
        # Structure POUR : il frappe 3 fois consécutives
        if tour % 4 == 0:
            narrer(f"\n💥 Le {BOSS_NOM} lance une SALVE DE SORTS !")
            # --- POUR i allant de 1 à 3 FAIRE ---
            for i in range(1, 4):
                if joueur.est_vivant():
                    degat_sort = random.randint(4, 8)
                    if esquive_active:
                        narrer(f"  Sort {i}/3 : esquivé grâce à votre bouclier !")
                    else:
                        joueur.subir_degats(degat_sort)
                        narrer(f"  Sort {i}/3 touche !")
            esquive_active = False
            continue  # Pas d'action joueur ce tour

        # --- Actions du joueur ---
        print("Que faites-vous ?")
        options = ["Attaquer (épée)"]

        # Options conditionnelles selon l'inventaire
        if "Potion de soin" in joueur.inventaire:
            options.append("Utiliser une Potion de soin")
        if "Torche magique" in joueur.inventaire:
            options.append("Utiliser la Torche magique (brûle le sorcier)")
        options.append("Se protéger (bouclier pour le prochain sort)")

        choix = demander_choix(options)
        action = options[int(choix) - 1]

        # --- Structure alternative : traitement de l'action ---
        if action == "Attaquer (épée)":
            critique = random.random() < 0.2  # 20% de chance de coup critique
            degats = random.randint(force_effective - 2, force_effective + 4)
            if critique:
                degats *= 2
                narrer(f"\n  💥 COUP CRITIQUE ! {degats} dégâts !")
            else:
                narrer(f"\n  ⚔️  Vous frappez pour {degats} dégâts.")
            boss_pv = max(0, boss_pv - degats)

        elif action == "Utiliser une Potion de soin":
            joueur.inventaire.remove("Potion de soin")
            joueur.soigner(30)

        elif "Torche magique" in action:
            joueur.inventaire.remove("Torche magique")
            degats_feu = random.randint(20, 35)
            narrer(f"\n  🔥 La Torche brûle le sorcier pour {degats_feu} dégâts !")
            boss_pv = max(0, boss_pv - degats_feu)

        else:  # Se protéger
            narrer("\n  🛡️  Vous levez votre bouclier. Prochain sort esquivé !")
            esquive_active = True

        # --- Contre-attaque du boss (si encore en vie) ---
        if boss_pv > 0:
            # Le boss devient plus fort si ses PV sont bas
            if boss_pv < BOSS_PV_MAX // 2:
                narrer(f"  ⚠️  Le {BOSS_NOM} entre en RAGE !")
                degats_boss = random.randint(BOSS_FORCE, BOSS_FORCE + 8)
            else:
                degats_boss = random.randint(BOSS_FORCE - 3, BOSS_FORCE + 3)

            if not esquive_active:
                joueur.subir_degats(degats_boss)

    # -------------------------------------------------------
    # Fin du combat
    # -------------------------------------------------------
    afficher_separateur()
    if joueur.est_vivant():
        narrer(f"\n✨ Le {BOSS_NOM} s'effondre dans un dernier cri !")
        narrer('"Impossible... vaincu par un simple élève de première..."')
        narrer("\nLa tour tremble. Vous avez sauvé le royaume !")
        joueur.or_ += 100
        joueur.ramasser("Baguette du Sorcier")
        narrer(f"\n💰 Vous récupérez 100 pièces d'or et la Baguette du Sorcier !")
    else:
        narrer(f"\n💀 Le {BOSS_NOM} ricane : \"Trop facile...\"")

    # -------------------------------------------------------
    # 🎯 MISSION ÉLÈVE 4 — À COMPLÉTER :
    # -------------------------------------------------------
    # 1. Ajouter une phase de dialogue avant le combat :
    #    → 3 questions du sorcier, SI bonnes réponses → bonus
    #
    # 2. Ajouter un sort "Invocation" :
    #    → Le sorcier invoque 2 squelettes (POUR i de 1 à 2)
    #    → Chaque squelette inflige 5 dégâts
    #
    # 3. Ajouter un système de niveaux de difficulté :
    #    → SI joueur.victoires >= 2 → boss plus facile (PV réduits)
    #    → SINON → boss standard
    # -------------------------------------------------------
