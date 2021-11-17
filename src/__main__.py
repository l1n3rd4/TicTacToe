from randomComputerPlayer import RandomComputerPlayer
from ticTacToe import TicTacToe
from humanPlayer import HumanPlayer
from gameController import GameController

if __name__ == "__main__":
    x_player = RandomComputerPlayer("X")
    o_player = HumanPlayer("O")
    tic = TicTacToe()
    GameController.play(tic, x_player, o_player, print_game=True)