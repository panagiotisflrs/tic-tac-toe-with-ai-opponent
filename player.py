import math
import random


class Player:
    def __init__(self,letter):
        self.letter = letter
        pass

    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #Its my turn and i havent done anything but just look at the window.
        valid_square = False
        val = None
        #Now i am ready to play. So i have to choose a valid square.
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Please try again.')

        return val

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #In the beginning the computer will choose randomly a spot to play.
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())

        else:
            #using the minimax algorithm to win.
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, stage_of_the_game, player):
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'

        if stage_of_the_game.winner == other_player:
            # we need to return position and score because without the score the minimax algorithm wont work.
            return {'position': None,
                    'score': 1 * (stage_of_the_game.num_empty_squares() + 1) if other_player == max_player
                     else -1 * (stage_of_the_game.num_empty_squares() + 1)}

        # no more empty squares.
        elif not stage_of_the_game.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best_score = {'position': None, 'score': -math.inf} # each score should maximize
        else:
            best_score = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in stage_of_the_game.available_moves():
            # make a move/try a spot.
            stage_of_the_game.make_move(possible_move, player)

            # recurse using minimax to simulate a game after making the move.
            sim_score = self.minimax(stage_of_the_game, other_player)
            # now we alternate players

            #undo the move.
            stage_of_the_game.board[possible_move] = ' '
            stage_of_the_game.winner = None
            #we need the command below because it will mess our game due to the recursion.
            sim_score['position'] = possible_move

            #update the dictionaries if necessary
            if player == max_player: #we maximize for us.
                if  sim_score['score'] > best_score['score']:
                    best_score= sim_score
            else: #we minimize for the other player.
                if sim_score['score'] < best_score['score']:
                    best_score= sim_score

        return best_score