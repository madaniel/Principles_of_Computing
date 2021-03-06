"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    results = [0 for dummy_x in range(6)]
    
    for dice in hand:
        if dice == 1:
            results[0] += 1
        elif dice == 2:
            results[1] += 2
        elif dice == 3:
            results[2] += 3
        elif dice == 4:
            results[3] += 4
        elif dice == 5:
            results[4] += 5
        elif dice == 6:
            results[5] += 6
    return max(results)


def expected_value(held_dice, num_die_sides , num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
    You should use gen_all_sequences to compute all possible rolls for the dice being rolled.

    held_dice: dice that you will hold
    The dice being held are specified by the tuple held_dice
    
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value		
    """
    total_score = 0
    result = 0
    
    sequences = gen_all_sequences( set(i for i in range(1 , 7) ), num_free_dice)
    
    for item in sequences:
        total_score += score(held_dice + item)
          
    result = total_score / float( len(sequences) )
    return result
        

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
            
    answer_set = set([()])
    copy = set([()])
    
    for item in hand:
        for partial_sequence in answer_set:
            new_sequence = list(partial_sequence)
            new_sequence.append(item)
            copy.add(tuple(new_sequence))
        answer_set = set(copy)
    return answer_set
    

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

#import user35_oGFuhcPNLh_0 as score_testsuite
#score_testsuite.run_suite(score)
    
#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#expected_value_testsuite.run_suite(expected_value)

