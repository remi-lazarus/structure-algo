# ⚔️ La Quête du Code — Projet Git · 1ère CIEL

> Jeu d'aventure textuel développé collaborativement avec Git.

---

## 🎮 Lancer le jeu

```bash
python main.py
```

---

## 📁 Structure du projet

```
jeu-aventure/
├── main.py              # Point d'entrée — NE PAS MODIFIER sans accord
├── moteur/
│   ├── joueur.py        # Classe Joueur (PV, inventaire, or…)
│   └── affichage.py     # Fonctions d'affichage et de narration
├── scenes/
│   ├── intro.py         # Scène 1 : Le Réveil         → Élève 1
│   ├── foret.py         # Scène 2 : La Forêt Maudite  → Élève 2
│   ├── caverne.py       # Scène 3 : La Caverne        → Élève 3
│   └── boss.py          # Scène 4 : Boss Final        → Élève 4
└── README.md            # Ce fichier
```

---

## 🌿 Workflow Git du projet

### 1. Cloner le dépôt (une seule fois)
```bash
git clone <url-du-depot>
cd jeu-aventure
```

### 2. Créer sa branche de travail
Chaque élève travaille sur **sa propre branche** :
```bash
git checkout -b scene/intro      # Élève 1
git checkout -b scene/foret      # Élève 2
git checkout -b scene/caverne    # Élève 3
git checkout -b scene/boss       # Élève 4
```

### 3. Travailler, sauvegarder, envoyer
```bash
# Après chaque modification significative :
git add scenes/ma_scene.py
git commit -m "feat: description de ce que j'ai fait"
git push origin scene/ma_scene
```

### 4. Intégrer son travail (fait en groupe)
```bash
git checkout main
git merge scene/intro
git merge scene/foret
# En cas de conflit → résoudre, puis git add + git commit
```

---

## 🧠 Structures algorithmiques utilisées

| Fichier | Structure | Où ? |
|---------|-----------|------|
| `main.py` | Séquentielle | Enchaînement des scènes |
| `main.py` | Alternative | Choix forêt / caverne |
| `main.py` | TANT QUE | Validation du choix |
| `scenes/foret.py` | Alternative | Actions en combat |
| `scenes/foret.py` | TANT QUE | Boucle de combat |
| `scenes/caverne.py` | POUR | Exploration des salles |
| `scenes/caverne.py` | TANT QUE | Désamorçage du piège |
| `scenes/boss.py` | Toutes | Combat final complet |

---

## 📋 Conventions de commit

Utiliser des **préfixes clairs** dans vos messages de commit :

| Préfixe | Usage |
|---------|-------|
| `feat:` | Nouvelle fonctionnalité |
| `fix:` | Correction d'un bug |
| `style:` | Mise en forme, texte narratif |
| `docs:` | Modification du README |
| `refactor:` | Réécriture de code existant |

**Exemples :**
```
feat: ajout de l'énigme dans la scène intro
fix: correction boucle infinie dans foret.py
style: amélioration des textes narratifs
```

---

## 👥 Équipe

| Rôle | Branche | Fichier |
|------|---------|---------|
| Élève 1 | `scene/intro` | `scenes/intro.py` |
| Élève 2 | `scene/foret` | `scenes/foret.py` |
| Élève 3 | `scene/caverne` | `scenes/caverne.py` |
| Élève 4 | `scene/boss` | `scenes/boss.py` |

---

*Projet réalisé en 1ère CIEL — Algorithmique & Git*
