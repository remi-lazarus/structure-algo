"""
=============================================================
  moteur/joueur.py — Classe Joueur
=============================================================
  Contient toutes les données et actions liées au joueur.
  Fichier partagé : modifier avec précaution !
=============================================================
"""


class Joueur:
    """Représente le personnage du joueur."""

    def __init__(self, nom: str, pv_max: int = 100):
        self.nom = nom
        self.pv_max = pv_max
        self.pv = pv_max          # Points de vie actuels
        self.force = 10           # Dégâts infligés par attaque
        self.inventaire = []      # Liste des objets collectés
        self.or_ = 0              # Pièces d'or
        self.victoires = 0        # Nombre de combats gagnés

    # -------------------------------------------------------
    # Méthodes utilitaires
    # -------------------------------------------------------

    def est_vivant(self) -> bool:
        """Retourne True si le joueur a encore des PV."""
        return self.pv > 0

    def subir_degats(self, degats: int):
        """Réduit les PV du joueur (minimum 0)."""
        self.pv = max(0, self.pv - degats)
        print(f"  💔 {self.nom} subit {degats} dégâts. PV restants : {self.pv}/{self.pv_max}")

    def soigner(self, soin: int):
        """Augmente les PV sans dépasser le maximum."""
        avant = self.pv
        self.pv = min(self.pv_max, self.pv + soin)
        print(f"  💊 {self.nom} récupère {self.pv - avant} PV. PV : {self.pv}/{self.pv_max}")

    def ramasser(self, objet: str):
        """Ajoute un objet à l'inventaire."""
        self.inventaire.append(objet)
        print(f"  🎒 {self.nom} ramasse : {objet}")

    def afficher_statut(self):
        """Affiche un résumé de l'état du joueur."""
        barre = "█" * (self.pv // 10) + "░" * ((self.pv_max - self.pv) // 10)
        print(f"\n  ⚔️  {self.nom} | PV [{barre}] {self.pv}/{self.pv_max}")
        if self.inventaire:
            print(f"  🎒 Inventaire : {', '.join(self.inventaire)}")
        if self.or_ > 0:
            print(f"  💰 Or : {self.or_} pièces")

    # -------------------------------------------------------
    # À COMPLÉTER PAR LES ÉLÈVES
    # -------------------------------------------------------
    # TODO : ajouter une méthode attaquer(ennemi)
    # TODO : ajouter une méthode utiliser_potion()
    # TODO : ajouter une méthode afficher_inventaire()
