class TicTacToe:
    TICTACTOE_SIZE = 3

    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [[' ' for _ in range(TicTacToe.TICTACTOE_SIZE)] \
                     for _ in range(TicTacToe.TICTACTOE_SIZE)]

    def print_board(self):
        for i in range(TicTacToe.TICTACTOE_SIZE):
            print(self.board[i])

    def get_avalaible_moves(self):
        list = []

        for i in range(TicTacToe.TICTACTOE_SIZE):
            for j in range(TicTacToe.TICTACTOE_SIZE):
                if self.board[i][j] == ' ':
                    list.append(f"{i},{j}")

        return list

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        len(self.get_avalaible_moves())

    def make_move(self, row_position, column_position, letter):
        if self.boarld[row_position, column_position] == ' ':
            self.board[row_position, column_position]

            if self.winner(row_position, column_position, letter):
                self.current_winner = letter
            return True
        return False


    def winner(self, row, column, letter):

        # linhas são iguais ? 
        line_check = self.has_equal_rows(self, column, letter)
        # colunas são iguais ?
        column_check = self.has_equal_columns(self, row, letter)
        # diagonais são iguais ? 
        diagonal_check = self.has_equal_diagonals(self, row, letter)
        
        return (diagonal_check | column_check | line_check)

    def has_equal_rows(self, column, letter):
        count = 0

        for i in range(TicTacToe.TICTACTOE_SIZE):
            if self.board[i][column] == letter:
                count += 1

        return (count == 2)

    def has_equal_columns(self, row, letter):
        count = 0

        for i in range(TicTacToe.TICTACTOE_SIZE):
            if self.board[row][i] == letter:
                count += 1

        return (count == 2)

    def has_equal_diagonals(self,letter):
        pass

    def __del__(self):
        return (True)

        