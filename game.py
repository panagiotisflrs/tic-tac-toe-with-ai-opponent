import time
from player import *

class Tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #   if spot == ' '
        #       moves.append(i)
        #return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
        #it is the same with: return len(self.available_moves())

    #If valid move then make the move.
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter

            #i need to check if someone has won.
            if self.possible_winner(square,letter):
                self.winner = letter
            return True # A move was made. If a move wasn't made then its False.
        return False # Every square was filled or there hasn't been an input yet or invalid input.

    def possible_winner(self, square, letter):
        #row winning condition.
        # // it means divide by 3 and then round down.
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True

        #column winning condition.
        # % it means the left over of the division. Aka the remainder
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # diagonal winning condition.
        if square % 2 == 0:
            diagonal1= [self.board[i] for i in [0,4,8]]
            diagonal2= [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagonal1):
                return True
            if all(spot == letter for spot in diagonal2):
                return True

        #if there is no winning condition.
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'x'

    while game.empty_squares():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'o' if letter == 'x' else 'x'

            time.sleep(0.7)

    if print_game:
        print('It\'s a tie.')

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = GeniusComputerPlayer('o')
    t = Tictactoe()
    play(t, x_player, o_player, print_game = True)