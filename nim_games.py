#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
def ask_player_play(n_matches, start_player, second_player):
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
            print('======================================================')
            print(f"       The player {actual_player} has won! Congratulations!")
            print('======================================================')
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
    user_choice = input("Who started the game? player 1 or 2? ")
    if user_choice == '1':
        return player1
    else:
        return player2


def ask_player_name(n):
    """
    The ask_player function asks the player's name and return it.
    :param n: the n player's name
    :return: the player's name
    """
    player_name = input("Player name: ").strip()
    print(f"Player {n}: {player_name}")
    return player_name


def main():
    number_of_matches = 21
    player_one = ask_player_name(1)
    player_two = ask_player_name(2)
    starting_player = who_starts(player_one, player_two)
    second_player = player_two if starting_player == player_one else player_one
    ask_player_play(number_of_matches, starting_player, second_player)

if __name__ == '__main__':
    main()