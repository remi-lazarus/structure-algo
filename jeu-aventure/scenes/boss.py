"""
=============================================================
  scenes/boss.py — Le Boss Final : Le Sorcier du Code
=============================================================
"""

import random
from moteur.affichage import afficher_scene, narrer, demander_choix, afficher_separateur
from moteur.joueur import Joueur


# -------------------------------------------------------
# Données du boss
# -------------------------------------------------------
BOSS_NOM = "Sorcier du Code"
BOSS_PV_MAX = 80
BOSS_FORCE = 12


# -------------------------------------------------------
# Questions du sorcier
# -------------------------------------------------------
QUESTIONS_SORCIER = [
    {"question": "Combien font 7 × 8 ?", "reponse": "56"},
    {"question": "Quelle structure répète une action un nombre connu de fois ?", "reponse": "pour"},
    {"question": "Quel mot-clé permet de tester une condition en Python ?", "reponse": "if"},
]


def afficher_combat(joueur: Joueur, boss_pv: int):
    barre = "█" * (boss_pv // 10) + "░" * ((BOSS_PV_MAX - boss_pv) // 10)
    print(f"\n🧙 {BOSS_NOM} | [{barre}] {boss_pv}/{BOSS_PV_MAX}")
    joueur.afficher_statut()


# -------------------------------------------------------
# Phase de dialogue
# -------------------------------------------------------
def phase_dialogue(joueur: Joueur) -> int:
    narrer(f'\n🧙 {BOSS_NOM} : "Réponds à mes questions !"')

    bonnes = 0

    for i, qa in enumerate(QUESTIONS_SORCIER, start=1):
        print(f"Question {i}/3 : {qa['question']}")
        rep = input("> ").strip().lower()

        if rep == qa["reponse"]:
            narrer("✅ Correct !")
            bonnes += 1
        else:
            narrer(f"❌ Faux (réponse : {qa['reponse']})")

    if bonnes == 3:
        narrer("🌟 Bonus +5 force !")
        return 5
    elif bonnes > 0:
        narrer(f"✨ Bonus +{bonnes} force !")
        return bonnes
    else:
        narrer("😤 Aucun bonus.")
        return 0


# -------------------------------------------------------
# SCENE BOSS
# -------------------------------------------------------
def scene_boss(joueur: Joueur):

    afficher_scene("Boss Final")
    narrer(f"\nVous affrontez le {BOSS_NOM}...")

    # Dialogue
    bonus_attaque = phase_dialogue(joueur)

    # Bonus inventaire
    if "Croc de loup" in joueur.inventaire:
        bonus_attaque += 3
    if "Épée rouillée" in joueur.inventaire:
        bonus_attaque += 2

    force = joueur.force + bonus_attaque

    # Difficulté dynamique
    if joueur.victoires >= 2:
        boss_pv = 60
        narrer("😌 Boss affaibli !")
    else:
        boss_pv = BOSS_PV_MAX

    tour = 0
    esquive = False

    afficher_separateur()

    # -------------------------------------------------------
    # BOUCLE COMBAT
    # -------------------------------------------------------
    while boss_pv > 0 and joueur.est_vivant():
        tour += 1
        print(f"\n--- Tour {tour} ---")
        afficher_combat(joueur, boss_pv)

        # Invocation
        if tour % 3 == 0:
            narrer("☠️ Invocation de squelettes !")
            for i in range(2):
                joueur.subir_degats(5)
            continue

        # Salve magique
        if tour % 4 == 0:
            narrer("💥 Salve magique !")
            for i in range(3):
                if not esquive:
                    joueur.subir_degats(random.randint(4, 8))
            esquive = False
            continue

        # Choix joueur
        options = ["Attaquer"]

        if "Potion de soin" in joueur.inventaire:
            options.append("Potion")

        if "Torche magique" in joueur.inventaire:
            options.append("Torche")

        options.append("Défense")

        choix = demander_choix(options)
        action = options[int(choix) - 1]

        # Actions
        if action == "Attaquer":
            degats = random.randint(force - 2, force + 4)
            if random.random() < 0.2:
                degats *= 2
                narrer(f"💥 Critique ! {degats}")
            boss_pv -= degats

        elif action == "Potion":
            joueur.inventaire.remove("Potion de soin")
            joueur.soigner(30)

        elif action == "Torche":
            joueur.inventaire.remove("Torche magique")
            degats = random.randint(20, 35)
            boss_pv -= degats

        else:
            esquive = True

        # Attaque boss
        if boss_pv > 0:
            if boss_pv < BOSS_PV_MAX // 2:
                degats = random.randint(12, 20)
            else:
                degats = random.randint(9, 15)

            if not esquive:
                joueur.subir_degats(degats)

    # -------------------------------------------------------
    # FIN
    # -------------------------------------------------------
    afficher_separateur()

    if joueur.est_vivant():
        narrer("🎉 Victoire !")
        joueur.or_ += 100
        joueur.ramasser("Baguette du Sorcier")
    else:
        narrer("💀 Défaite...")