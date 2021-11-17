import time

class GameController:
    @staticmethod
    def play(game, x_player, o_player, print_game=True):
        if print_game:
            game.print_board()

        letter = 'X'
        while game.empty_squares():
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
            if game.make_move(square, letter):

                if print_game:
                    print(letter + ' makes a move to square {}'.format(square))
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter  # ends the loop and exits the game
                letter = 'O' if letter == 'X' else 'X'  # switches player

            time.sleep(1)

        if print_game:
            print('It\'s a tie!')