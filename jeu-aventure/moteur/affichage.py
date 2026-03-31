"""
=============================================================
  moteur/affichage.py — Fonctions d'affichage
=============================================================
  Centralise tout ce qui concerne l'affichage dans le terminal.
=============================================================
"""

import time


def afficher_titre():
    """Affiche le titre du jeu au démarrage."""
    print("\n" + "═" * 55)
    print("  ⚔️   L A   Q U Ê T E   D U   C O D E   ⚔️  ")
    print("      Jeu d'aventure textuel · 1ère CIEL")
    print("═" * 55 + "\n")


def afficher_separateur():
    """Affiche une ligne de séparation."""
    print("\n" + "─" * 55 + "\n")


def afficher_scene(titre: str):
    """Affiche l'en-tête d'une nouvelle scène."""
    print("\n" + "━" * 55)
    print(f"  📍 {titre.upper()}")
    print("━" * 55)


def narrer(texte: str, delai: float = 0.03):
    """
    Affiche un texte caractère par caractère pour un effet
    narratif. Utilise une boucle POUR.

    Structure algorithmique : POUR … FAIRE
    """
    # --- POUR chaque caractère du texte FAIRE ---
    for caractere in texte:
        print(caractere, end="", flush=True)
        time.sleep(delai)
    print()  # Retour à la ligne


def demander_choix(options: list) -> str:
    """
    Affiche des options numérotées et retourne le choix valide.

    Structure algorithmique : TANT QUE … FAIRE
    (on répète la demande tant que la saisie est invalide)
    """
    valides = [str(i + 1) for i in range(len(options))]

    # Affichage des options (structure séquentielle)
    for i, option in enumerate(options, 1):
        print(f"  [{i}] {option}")

    # Validation de la saisie (structure répétitive TANT QUE)
    choix = ""
    while choix not in valides:
        choix = input("\n  Votre choix > ").strip()
        if choix not in valides:
            print(f"  ⚠️  Entrez un nombre entre 1 et {len(options)}.")

    return choix


def afficher_carte():
    """
    Affiche une carte ASCII du donjon.

    Structure algorithmique : Affichage structuré avec chaînes de caractères
    """
    print("\n" + "╔" + "═" * 53 + "╗")
    print("║" + " " * 15 + "📜 CARTE DU DONJON 📜" + " " * 16 + "║")
    print("╠" + "═" * 53 + "╣")
    print("║                                                     ║")
    print("║           ENTRÉE DU DONJON                          ║")
    print("║               🚪                                     ║")
    print("║               │                                     ║")
    print("║            ═══╳═══                                  ║")
    print("║               │                                     ║")
    print("║     ┌─────────┼─────────┐                           ║")
    print("║     │         │         │                           ║")
    print("║  🍄 │  SALLE  │  SALLE  │  ⚔️  SALLE              ║")
    print("║     │   DES   │   DU    │        DU                ║")
    print("║     │ CHAMPI- │ TRÉSOR  │       TROLL              ║")
    print("║     │  GNONS  │    💎   │        👹                ║")
    print("║     │         │         │                           ║")
    print("║     └────┬────┴────┬────┘                           ║")
    print("║          │         │                                ║")
    print("║          └────╳────┘                                ║")
    print("║               │                                     ║")
    print("║                                                     ║")
    print("║  🔑 Légende : 👹 Boss    💎 Trésor    🔥 Danger    ║")
    print("║                                                     ║")
    print("╚" + "═" * 53 + "╝\n")


# -------------------------------------------------------
# À COMPLÉTER PAR LES ÉLÈVES
# -------------------------------------------------------
# TODO : ajouter une fonction afficher_combat(joueur, ennemi)
