#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
def game_vs_bot(player,n_matches):
    actual_player = player
    second_player = "Computer"
    victory = False
    last_player_move = None  # Pour stocker le dernier coup du joueur

    while not victory:
        if actual_player == player:
            print(f"It is {actual_player}'s turn.")

            # Validation loop
            valid = False
            while not valid:
                try:
                    action = int(input('How many matches would you like to take? (1-4) '))
                    if 1 <= action <= 4:
                        valid = True
                    else:
                        print("Please choose a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            print(f'You have taken {action} matches')
            n_matches -= action
            last_player_move = action  # Mémoriser le coup du joueur
            print(f'The actual number of matches is {n_matches}\n')

        else:
            print(f"It is {second_player}'s turn.")
            if last_player_move is not None:
                bot_move = 5 - last_player_move
            else:
                # Si le bot commence, il joue un coup aléatoire ou optimal
                bot_move = min(4, n_matches % 5 if n_matches % 5 != 0 else 1)

            # S'assurer que le coup est valide
            bot_move = max(1, min(bot_move, min(4, n_matches)))
            print(f'The bot has taken {bot_move} matches')
            n_matches -= bot_move
            print(f'The actual number of matches is {n_matches}\n')

        if n_matches <= 0:
            victory = True
            loser = actual_player
            winner = second_player if actual_player == player else player
            print('=======================================================')
            print(f"    {winner} has won! {loser} took the last match and lost.")
            print('=======================================================')
        else:
            actual_player = second_player if actual_player == player else player


def game_player_vs_player(n_matches, start_player, second_player):
    """
    The function asks the player who is playing which number of
    matches does he want to take, then it goes to the second player.
    The function keeps track of the number of matches played and
    when it goes to 0 the actual player win the game.

    :param n_matches: the original  number of matches.
    :param start_player: the player who start the game.
    :param second_player: the second player.
    :return:
    """
    actual_player = start_player
    victory = False
    while not victory:
        print(f"It is {actual_player}'s turn.")

        # Validation loop
        valid = False
        while not valid:
            try:
                action = int(input('How many matches would you like to take? (1-4) '))
                if 1 <= action <= 4:
                    valid = True
                else:
                    print("Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f'You have taken {action} matches')
        n_matches -= action
        print(f'The actual number of matches is {n_matches}\n')

        if n_matches <= 0:
            victory = True
            loser = actual_player
            winner = second_player if actual_player == start_player else start_player
            print('=======================================================')
            print(f"{   winner} has won! {loser} took the last match and lost.")
            print('=======================================================')
        else:
            actual_player = second_player if actual_player == start_player else start_player


def who_starts(player1, player2):
    """
    This function takes in input the players and ask
    who is starting, then return the player accordingly.
    :param player1: the first player
    :param player2: the second player
    :return: the player that will start in the game.
    """
    user_choice = input("Who start the game? player 1 or 2? ")
    if user_choice == '1':
        return player1
    else:
        return player2


def ask_player_name(n):
    """
    The ask_player_name function asks the player's name and return it.
    :param n: the number of the player.
    :return: the name of the player.
    """
    player_name = input("Player name: ").strip().lower().capitalize()
    print(f"Player {n}: {player_name}")
    return player_name


def main():
    """
    The main function of the game.
    We add the number of matches.
    Asks for players names.
    Then we determine who start the game.
    And finally we start the game.
    :return: the logic of the game.
    """
    number_of_matches = 21
    player_or_bot = input('Do you want to play against a (b)ot or a second (p)layer?').strip().lower()
    player_one = ask_player_name(1)
    if player_or_bot == 'b':
        game_vs_bot(player_one, number_of_matches)
    else:
        player_two = ask_player_name(2)
        starting_player = who_starts(player_one, player_two)
        second_player = player_two if starting_player == player_one else player_one
        game_player_vs_player(number_of_matches, starting_player, second_player)

if __name__ == '__main__':
    main()