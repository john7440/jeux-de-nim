#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
"""
Jeux  de Nim (variante simple et de Marienbad)
"""
def game_menu():
    print("\n=== Welcome to the Matchstick Game ===")
    print("🕹️ Choose your game mode:")
    print("  (s) Standard vs Player👤")
    print("  (b) Standard vs Bot 🤖")
    print("  (m) Marienbad vs Player👤")
    print("  (mb) Marienbad vs Bot 🤖")
    mode = input("\nWhich mode do you want to play?  ").strip().lower()

    # Standard mode
    if mode in ['s', 'b']:
        print("\n=== Welcome to the Standard Mode ===")
        number_of_matches = 21
        player1 = ask_player_name(1)

        # Against a bot
        if mode == 'b':
            print("   ===👤 Player Vs Bot 🤖 ===")
            starting_player = who_starts(player1, "Computer")
            standard_game_vs_bot(starting_player, number_of_matches)

        # Against another player (or yourself, why not)
        else:
            print("   ===👤 Player Vs Player 👤 ===")
            player2 = ask_player_name(2)
            starting_player = who_starts(player1, player2)
            second_player = player2 if starting_player == player1 else player1
            standard_player_vs_player(number_of_matches, starting_player, second_player)

    # The marienbad mode
    elif mode == 'm':
        print("\n=== Welcome to the Marienbad Mode ===")
        print("   ===👤 Player Vs Player 👤 ===")
        player1 = ask_player_name(1)
        player2 = ask_player_name(2)
        starting_player = who_starts(player1, player2)
        second_player = player2 if starting_player == player1 else player1
        marienbad_player_vs_player(starting_player, second_player)

    elif mode == 'mb':
        print("\n=== Welcome to the Marienbad Mode ===")
        print("   ===👤 Player Vs Bot 🤖 ===")
        player1 = ask_player_name(1)
        starting_player = who_starts(player1, "Computer 🤖")
        marienbad_player_vs_bot(starting_player, player1, "Computer 🤖")

    # The user don't want to cooperate mode
    else:
        print("Invalid choice. Please restart and choose a valid mode.")


def marienbad_bot_strategy(piles):
    """
    This is the 'strategy' of the bot for the marienbad mode,
    it just does random choices each times (so its totally non-optimal)
    :param piles: the actual status of the piles.
    :return: the updated piles.
    """
    piles_not_empty = [i for i, pile in enumerate(piles) if pile > 0]
    bot_pile_choice = random.choice(piles_not_empty)
    bot_matches_choice = random.randint(1, piles[bot_pile_choice])
    print(f"Computer has taken {bot_matches_choice} matches from the {bot_pile_choice} pile.")
    piles[bot_pile_choice] -= bot_matches_choice
    return piles


def marienbad_player_vs_bot(starting_player, player1, bot_name = "Computer 🤖"):
    """
    This function handles the logiq for a marienbad game player vs bot.
    It just checks the actual status of the piles each turn and
    switch 'players' till there's a winner (no more matches lefts).
    :param starting_player: starting player.
    :param player1: the player 1.
    :param bot_name: the bot.
    :return: calls the announce_winner function when anyone wins.
    """
    piles = [1, 3, 5 ,7]
    actual_player = starting_player

    while any(pile > 0 for pile in piles):
        print(f"\nCurrent piles: {piles}")
        if actual_player == player1:
            piles = marienbad_play_turn(player1, piles)
        else:
            piles = marienbad_bot_strategy(piles)

        if all(pile == 0 for pile in piles):
            winner = bot_name if actual_player == player1 else player1
            announce_winner(actual_player, winner)
            break
        else:
            actual_player = bot_name if actual_player == player1 else player1


def marienbad_play_turn(player, piles):
    """
    This function handles a single turn for a player in Marienbad.
    It show prompts for row and number of matches to remove,
    check if they are valid and return the updated piles.
    :param player: the actual player
    :param piles: the actual status of piles
    :return: the new status of piles
    """
    while True:
        try:
            print(f"\nCurrent piles: {piles}")
            row = int(input(f"{player}, choose the pile (1-{len(piles)}): ")) -1
            if row < 0 or row >= len(piles) or piles[row] == 0:
                print("\nThat is not a valid row. Please try again.")
                continue
            count = int(input(f"{player}, how many matches do you want to remove from {row+1}: "))
            if 1 <= count <= piles[row]:
                piles[row] -= count
                print(f"{player} removed {count} from row {row + 1}.")
                return piles
            else:
                print("\nInvalid number of matches. Please try again.")
        except ValueError:
            print("Invalid input. Try again.")


def marienbad_player_vs_player(player1, player2):
    """
    This function simulate the marienbad game logic between two players.
    :param player1: player 1
    :param player2: player 2
    :return: None
    """
    piles = [1, 3, 5, 7]
    actual_player = player1

    while any(pile >0 for pile in piles):
        piles = marienbad_play_turn(actual_player, piles)

        if all(pile == 0 for pile in piles):
            winner = player2 if actual_player == player1 else player1
            announce_winner(actual_player, winner)
            break
        else:
            actual_player = player2 if actual_player == player1 else player1


def standard_game_vs_bot(starting_player, n_matches):
    """
    This function is the logic of the standard game against a bot.
    :param starting_player: the player or bot
    :param n_matches: the original number of matches
    :return:
    """
    human_player = starting_player if starting_player != "Computer" else "Player"
    bot = "Computer 🤖"
    actual_player = starting_player
    last_player_move = None

    while n_matches > 0:
        if actual_player == human_player:
            n_matches, last_player_move = play_turn(human_player, n_matches)
        else:
            print(f"{bot}'s turn.")
            move = bot_strat(n_matches, last_player_move)
            n_matches -= move
            last_player_move = move
            announce_move(bot, move, n_matches)

        if n_matches <= 0:
            winner = bot if actual_player == human_player else human_player
            announce_winner(actual_player, winner)
        else:
            actual_player = bot if actual_player == human_player else human_player


def standard_player_vs_player(n_matches,player1, player2):
    """
    This function is the logic of the standard game between two players.
    :param n_matches: the original number of matches
    :param player1: player 1
    :param player2: player 2
    :return:
    """
    actual_player = player1
    while n_matches > 0:
        n_matches, _ = play_turn(actual_player, n_matches)
        if n_matches <= 0:
            winner = player2 if actual_player == player1 else player1
            announce_winner(actual_player, winner)
        else:
            actual_player = player2 if actual_player == player1 else player1


def who_starts(player1, player2):
    """
    This function ask who is starting,
    then return the player accordingly.
    :param player1: the first player
    :param player2: the second player
    :return: the player that will start in the game.
    """
    choice = input("Who starts the game? player 1 or 2? ").strip()
    return player1 if choice == '1' else player2


def ask_player_name(n):
    """
    The ask_player_name function asks the player's name and return it.
    :param n: the number of the player.
    :return: the name of the player.
    """
    player_name = input(f"Player {n} name: ").strip().capitalize()
    print(f"Player {n}: {player_name}")
    return player_name


def ask_move(player):
    """
    The ask_move function asks the player's move,
    check if its valid and return it.
    :param player: the player
    :return: the validated move
    """
    while True:
        try:
            move = int(input(f"{player}, how many matches would you like to take? (1-4) "))
            if 1 <= move <= 4:
                return move
            print("Please choose a number between 1 and 4. ")
        except ValueError:
            print("Invalid input. Please enter a number. ")


def announce_move(player, move, remaining):
    """
    This function print out the move and the remaining matches.
    :param player: the actual player
    :param move: the move that was played
    :param remaining: the number of matches remaining
    :return: 2 f strings accordingly
    """
    print(f"{player} has taken {move} matches.")
    print(f"Remaining matches: {remaining}\n")


def announce_winner(loser, winner):
    """
    This function announces the winner of the game with a simple f string
    :param loser: the person (or bot) who loosed the game
    :param winner: the winner of the game
    :return: print an f string accordingly to the result
    """
    print('=======================================================')
    print(f"    {winner} has won! {loser} took the last match and lost.")
    print('=======================================================')


def play_turn(player, n_matches):
    """
    This function ask the player about his move, and return it.
    :param player: the actual player
    :param n_matches: the number of matches
    :return: the new number of matches and the move
    """
    move = ask_move(player)
    n_matches -= move
    announce_move(player, move, n_matches)
    return n_matches, move


def bot_strat(n_matches, last_player_move):
    """
    This function simulate the bot strategy.
    :param n_matches: the number of matches
    :param last_player_move: the last player move
    :return: an 'optimal' move according to the strategy.
    """
    if last_player_move is not None:
        move = 5 - last_player_move
    else:
        move = n_matches % 5 or 1
    return max(1, min(move, min(4, n_matches)))


def main():
    """
    The main function of the game.
    It calls the game menu.
    """
    game_menu()


if __name__ == '__main__':
    main()