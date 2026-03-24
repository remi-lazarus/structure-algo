"""
=============================================================
  JEU D'AVENTURE TEXTUEL — Projet Git · 1ère CIEL
=============================================================
  Fichier principal : point d'entrée du jeu.
  NE PAS MODIFIER ce fichier sans accord du groupe !
  Toute modification → nouvelle branche + pull request.
=============================================================
"""

from moteur.joueur import Joueur
from moteur.affichage import afficher_titre, afficher_separateur
from scenes.intro import scene_intro
from scenes.foret import scene_foret
from scenes.caverne import scene_caverne
from scenes.boss import scene_boss


def main():
    afficher_titre()

    # --- Création du joueur (structure séquentielle) ---
    print("Avant de commencer, comment t'appelles-tu, aventurier ?")
    nom = input("> ").strip() or "Inconnu"
    joueur = Joueur(nom)

    print(f"\nBienvenue, {joueur.nom} ! Que l'aventure commence...\n")
    afficher_separateur()

    # --- Enchaînement des scènes (structure séquentielle) ---
    scene_intro(joueur)

    # --- Structure alternative : choix de chemin ---
    if joueur.est_vivant():
        print("\nDevant vous, deux chemins s'offrent à vous :")
        print("  [1] Prendre le sentier de la Forêt")
        print("  [2] Descendre vers la Caverne")

        choix = ""
        # --- Structure répétitive : validation de saisie ---
        while choix not in ["1", "2"]:
            choix = input("> ").strip()
            if choix not in ["1", "2"]:
                print("Choisissez 1 ou 2.")

        if choix == "1":
            scene_foret(joueur)
        else:
            scene_caverne(joueur)

    # --- Boss final ---
    if joueur.est_vivant():
        scene_boss(joueur)

    # --- Fin du jeu ---
    afficher_separateur()
    if joueur.est_vivant():
        print(f"🏆 Félicitations {joueur.nom} ! Vous avez terminé l'aventure !")
        print(f"   Points de vie restants : {joueur.pv} / {joueur.pv_max}")
        print(f"   Inventaire final : {joueur.inventaire if joueur.inventaire else 'vide'}")
    else:
        print(f"💀 {joueur.nom} est tombé... L'aventure s'arrête ici.")
        print("   Retentez votre chance !")


if __name__ == "__main__":
    main()
