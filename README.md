### 🕹️ Jeu de Nim — Variante Simple (et Marienbad à venir)

Ce projet est une implémentation en Python du célèbre jeu de Nim, dans sa version simple (une seule pile d’allumettes). Il propose deux modes de jeu :

- 👤 Joueur contre joueur

- 🤖 Joueur contre bot (avec stratégie optimale)

📦 Fonctionnalités
- Choix du mode de jeu : contre un autre joueur ou contre l’ordinateur

- Saisie des noms des joueurs

- Choix du joueur qui commence

- Affichage du nombre d’allumettes restantes

- Détection automatique du gagnant selon la règle : celui qui prend la dernière allumette perd

- Stratégie optimale du bot : joue pour laisser un multiple de 5 à l’adversaire

🚀 Lancer le jeu :

Assurez-vous d’avoir Python 3 installé, puis exécutez :

python nim_game.py

🧠 Règles du jeu
- Il y a un nombre fixe d’allumettes (par défaut : 21).

- Chaque joueur peut prendre entre 1 et 4 allumettes par tour.

- Le joueur qui prend la dernière allumette perd la partie.

🤖 Stratégie du bot

Le bot applique une stratégie mathématique :

- Lorsqu’il commence, il essaie de laisser un multiple de 5 à l’adversaire.

- Ensuite, il répond toujours par 5 - k, où k est le nombre d’allumettes prises par le joueur.

🛠️ À venir

- Version Marienbad (plusieurs piles)