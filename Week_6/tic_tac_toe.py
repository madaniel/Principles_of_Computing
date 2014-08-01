"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    moves = []
    results = []
    best_score = None
    best_move = None
    
    opponet = op_player(player)
    
    if board.check_win() != None:
        
        if board.check_win() == provided.PLAYERX:
            return SCORES[provided.PLAYERX] , (-1, -1)
        
        if board.check_win() == provided.PLAYERO:
            return SCORES[provided.PLAYERO] , (-1, -1)
        
        if board.check_win() == provided.DRAW:
            return SCORES[provided.DRAW] , (-1, -1)
    
    free_steps = board.get_empty_squares()
    
    for step in free_steps:
        clone = board.clone()        
        clone.move(step[0],step[1],player)
        temp = mm_move(clone,opponet)
        
        if temp != None:
            if temp[0] == SCORES[player]:                
                return temp[0] , step                
            else:                
                results.append(temp)
                moves.append(step)
                
    for result, move in zip(results, moves):        
        if result[0] * SCORES[player] > best_score:
            best_score = result[0]
            best_move = move
    return best_score, best_move
        
        
         
         

    
    
    


    
def op_player(player):
    if player == provided.PLAYERX:
        return provided.PLAYERO
    else:
        return provided.PLAYERX

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)






#print mm_move(board,provided.PLAYERX)
#mm_move(board, provided.PLAYERO)

