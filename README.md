## 🕹️ Jeu de Nim — Variante Simple et Marienbad

Ce projet est une implémentation en Python du célèbre **jeu de Nim**, dans sa **version simple** (Une seule pile) et sa version **Marienbad** (Plusieurs piles d’allumettes). Il propose **deux modes de jeu** :

- 👤 Joueur contre joueur

- 🤖 Joueur contre bot

### 📦 Fonctionnalités
- **Choix du mode de jeu** : contre un autre joueur ou contre l’ordinateur

- **Saisie des noms** des joueurs

- **Choix du joueur qui commence**

- **Affichage** du nombre d’allumettes restantes

- **Détection automatique du gagnant** selon la règle : celui qui prend la dernière allumette perd

- **Stratégie optimale du bot** : joue pour laisser un multiple de 5 à l’adversaire

### 🚀 Pour lancer le jeu :

Assurez-vous d’avoir **Python 3 installé**, puis exécutez :

    python nim_games.py

### 🧱 Structure du code
- **main()** : point d’entrée
- **game_menu()** : menu principal du jeu et choix de mode de jeu
- **ask_player_name()** : fonction pour entrer le nom du joueur
- **who_starts()** : choix du joueur qui commence la partie
- **ask_move()** : demande du tour du joueur
- **play_turn()** : logique d'un tour (mode standard)
- **marienbad_play_turn()** : logique d'un tour (mode marienbad)
- **announce_move()** : affichage visuel du tour
- **bot_strat** : stratégie du bot pour le mode standard
- **standard_game_vs_bot()** : logique d'une partie d'un joueur contre le bot (mode standard)
- **standard_game_vs_player()** : logique partie joueur contre joueur (mode standard)
- **marienbad_bot_strategy()** : la 'stratégie' du bot (mode marienbad)
- **marienbad_player_vs_bot()** : logique de jeu vs bot (mode marienbad)
- **marienbad_player_vs_player()**: logique de jeu player vs player (mode marienbad)
- **announce_winner()** : affichage du gagnant et du perdant

### 🧠 Règles du jeu (Standard)
- Il y a un **nombre fixe d’allumettes** (par défaut : 21).

- Chaque joueur peut **prendre** entre **1 et 4 allumettes par tour**.

- Le **joueur qui prend la dernière allumette perd la partie.**

### 🤖 Stratégie du bot (Standard)

Le bot applique une **stratégie mathématique** :

- Lorsqu’il **commence**, il essaie de **laisser un multiple de 5** à l’adversaire.

- Ensuite, il répond **toujours par 5 - k**, où k est le nombre d’allumettes prises par le joueur.

### 🧠 Règles du jeu (Marienbad)
- Il y a un **nombre fixe d’allumettes** sur plusieurs piles (par défaut : 1, 3, 5, 7).

- Chaque joueur peut **prendre** entre **1 et 4 allumettes par tour** suivant la pile choisi.

- Le **joueur qui prend la dernière allumette perd la partie.**

### 🤖 Stratégie du bot (Marienbad)

Le bot n'a **pas réellement de stratégie**, ses **coups sont aléatoires**.
