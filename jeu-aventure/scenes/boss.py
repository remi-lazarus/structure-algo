"""
=============================================================
  scenes/boss.py — Le Boss Final : Le Sorcier du Code
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
    """Combat final contre le Sorcier du Code."""

    afficher_scene("La Tour du Sorcier — Boss Final")

    narrer("\nAu sommet de la tour, une silhouette vous attend.")
    narrer(f"C'est lui : le {BOSS_NOM} !")
    narrer('"Tu as survécu jusqu\'ici... Impressionnant. Mais ça s\'arrête là !"')

    # -------------------------------------------------------
    # 🧠 Phase de dialogue (quiz)
    # -------------------------------------------------------
    narrer("\n🧠 Le sorcier vous teste avant le combat...")

    questions = [
        ("Combien font 2 + 2 ?", "4"),
        ("Mot-clé pour une boucle en Python ?", "for"),
        ("Valeur de True and False ?", "false")
    ]

    bonnes_reponses = 0

    for question, reponse in questions:
        print(question)
        user = input("> ")
        if user.strip().lower() == reponse.lower():
            narrer("✔️ Correct !")
            bonnes_reponses += 1
        else:
            narrer("❌ Faux...")

    bonus_attaque = 0
    if bonnes_reponses >= 2:
        narrer("✨ Le sorcier est impressionné... Vous gagnez +5 en force !")
        bonus_attaque += 5

    # -------------------------------------------------------
    # Bonus inventaire
    # -------------------------------------------------------
    if "Croc de loup" in joueur.inventaire:
        bonus_attaque += 3
        narrer("🐺 Le Croc de loup vous donne +3 en force !")

    if "Épée rouillée" in joueur.inventaire:
        bonus_attaque += 2
        narrer("⚔️ L'Épée rouillée vous donne +2 en force !")

    force_effective = joueur.force + bonus_attaque

    # -------------------------------------------------------
    # ⚖️ Difficulté dynamique
    # -------------------------------------------------------
    if joueur.victoires >= 2:
        narrer("😌 Vous êtes expérimenté : le sorcier est affaibli.")
        boss_pv = int(BOSS_PV_MAX * 0.75)
    else:
        boss_pv = BOSS_PV_MAX

    tour = 0
    esquive_active = False

    afficher_separateur()
    narrer("⚔️ COMBAT FINAL !\n")

    # -------------------------------------------------------
    # Boucle principale
    # -------------------------------------------------------
    while boss_pv > 0 and joueur.est_vivant():
        tour += 1
        print(f"  ─── Tour {tour} ───")
        afficher_combat(joueur, boss_pv, BOSS_NOM)

        # -------------------------------------------------------
        # ☠️ Invocation (tous les 3 tours)
        # -------------------------------------------------------
        if tour % 3 == 0:
            narrer(f"\n☠️ Le {BOSS_NOM} invoque des squelettes !")

            for i in range(1, 3):
                if joueur.est_vivant():
                    narrer(f"  Squelette {i}/2 attaque ! (-5 PV)")
                    joueur.subir_degats(5)

            continue

        # -------------------------------------------------------
        # 💥 Salve magique (tous les 4 tours)
        # -------------------------------------------------------
        if tour % 4 == 0:
            narrer(f"\n💥 Le {BOSS_NOM} lance une SALVE DE SORTS !")

            for i in range(1, 4):
                if joueur.est_vivant():
                    degat_sort = random.randint(4, 8)

                    if esquive_active:
                        narrer(f"  Sort {i}/3 esquivé !")
                    else:
                        joueur.subir_degats(degat_sort)
                        narrer(f"  Sort {i}/3 touche !")

            esquive_active = False
            continue

        # -------------------------------------------------------
        # Actions joueur
        # -------------------------------------------------------
        print("Que faites-vous ?")
        options = ["Attaquer (épée)"]

        if "Potion de soin" in joueur.inventaire:
            options.append("Utiliser une Potion de soin")

        if "Torche magique" in joueur.inventaire:
            options.append("Utiliser la Torche magique")

        options.append("Se protéger")

        choix = demander_choix(options)
        action = options[int(choix) - 1]

        # -------------------------------------------------------
        # Traitement des actions
        # -------------------------------------------------------
        if action == "Attaquer (épée)":
            critique = random.random() < 0.2
            degats = random.randint(force_effective - 2, force_effective + 4)

            if critique:
                degats *= 2
                narrer(f"\n💥 COUP CRITIQUE ! {degats} dégâts !")
            else:
                narrer(f"\n⚔️ Vous infligez {degats} dégâts.")

            boss_pv = max(0, boss_pv - degats)

        elif action == "Utiliser une Potion de soin":
            joueur.inventaire.remove("Potion de soin")
            joueur.soigner(30)

        elif action == "Utiliser la Torche magique":
            joueur.inventaire.remove("Torche magique")
            degats = random.randint(20, 35)
            narrer(f"\n🔥 La torche brûle le sorcier ! ({degats} dégâts)")
            boss_pv = max(0, boss_pv - degats)

        else:
            narrer("\n🛡️ Vous vous préparez à esquiver !")
            esquive_active = True

        # -------------------------------------------------------
        # Contre-attaque du boss
        # -------------------------------------------------------
        if boss_pv > 0:
            if boss_pv < BOSS_PV_MAX // 2:
                narrer(f"⚠️ Le {BOSS_NOM} entre en RAGE !")
                degats_boss = random.randint(BOSS_FORCE, BOSS_FORCE + 8)
            else:
                degats_boss = random.randint(BOSS_FORCE - 3, BOSS_FORCE + 3)

            if not esquive_active:
                if random.random() < 0.1:
                    narrer("😵 Le sorcier rate son attaque !")
                else:
                    joueur.subir_degats(degats_boss)

    # -------------------------------------------------------
    # Fin du combat
    # -------------------------------------------------------
    afficher_separateur()

    if joueur.est_vivant():
        narrer(f"\n✨ Le {BOSS_NOM} est vaincu !")
        narrer("La tour s'effondre... Vous avez gagné !")

        joueur.or_ += 100
        joueur.ramasser("Baguette du Sorcier")

        narrer("💰 +100 or")
        narrer("🪄 Vous obtenez la Baguette du Sorcier !")

    else:
        narrer(f"\n💀 Le {BOSS_NOM} vous a vaincu...")
        #je ne sais pas ..