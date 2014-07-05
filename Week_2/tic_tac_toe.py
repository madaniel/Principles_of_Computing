"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.
       
def next_random_move(board):
    """
    Returns the next move on empty squere
    """
    if board.check_win() == None:
        return random.choice( board.get_empty_squares() )
    else:
        return False
    
def mc_trial(board, player):
    """
    The function should play a game starting with the given player by making random moves, alternating between players.
    The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.
    In other words, the function should modify the board input.
    """
    # player is the starter
    next_move = next_random_move(board)
    
    while next_move:
        board.move(next_move[0],next_move[1],player)
        next_move = next_random_move(board)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    This function takes a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly, it does not return anything,
    If you won the game, each square that matches your player should get a positive score (MCMATCH)
    and each square that matches the other player should get a negative score (-MCOTHER).
    Conversely, if you lost the game, each square that matches your player should get a negative score (-MCMATCH)
    and and each square that matches the other player should get a positive score (MCOTHER).
    All empty squares should get a score of 0.
    """
    dim = board.get_dim()
    machine = player
    user = provided.switch_player(player)
    
    if board.check_win() == provided.DRAW:
        #for row in range( dim ):
        #    for col in range( dim ):
        #        scores[row][col] = 0
        return
        
    if board.check_win() == machine:
        for row in range( dim ):
            for col in range( dim ):
                status = board.square(row ,col)
                
                if status == machine:
                    scores[row][col] += MCMATCH
                elif status == user:
                    scores[row][col] -= MCOTHER
    
    if board.check_win() == user:
        for row in range( dim ):
            for col in range( dim ):
                status = board.square(row ,col)                
                if status == machine:
                    scores[row][col] -= MCMATCH
                elif status == user:
                    scores[row][col] += MCOTHER
    
def get_best_move(board, scores):
    """ 
    The function should find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple.
    Ignore when the board has no empty squares.
    """
    if board.check_win() != None or not board.get_empty_squares():
        return
    
    dim = board.get_dim()
    max_score = -1    
    result = set()
    
    for row in range( dim ):
        for col in range( dim ):
            if board.square(row , col) != provided.EMPTY:
                continue
            if scores[row][col] > max_score:
                max_score = scores[row][col]
                result = set()	
                result.add((row , col))
            elif scores[row][col] == max_score:
                result.add((row , col))
            
    return result.pop()

    
def mc_move(board, player, trials):
    """
    The function should use the Monte Carlo simulation described above
    to return a move for the machine player in the form of a (row, column) tuple.
    Be sure to use the other functions you have written! 
    """
    dim = board.get_dim()
    scores = [[0 for dummy_i in range(dim)] for dummy_j in range(dim)]
    
    for dummy_i in range(trials):        
        test_board = board.clone()
        mc_trial (test_board , player)
        mc_update_scores(scores , test_board , player)     
    
    return get_best_move(board, scores)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

#run()

# Test suite for individual functions
#import user34_Uc9ea2tRiN_0 as test_ttt
#test_ttt.test_trial(mc_trial)
# print
#test_ttt.test_update_scores(mc_update_scores, MCMATCH, MCOTHER)
# print
#test_ttt.test_best_move(get_best_move)