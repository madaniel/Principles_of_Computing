"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    temp = []
    
    if len (list1) < 2:
        return list1
    
    for i in range( len(list1) - 1 ):
        if list1[i] != list1[i+1]:
            temp.append(list1[i])
            
    if list1[-1] not in temp:
        temp.append(list1[-1])
                
    return temp

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    temp = []
        
    if len(list1) < len(list2):
        short = list1
        long = list2
    else:
        short = list2
        long = list1
        
    for i in range(len(short) ):
        if short[i] in long:
            temp.append(short[i])
    return temp

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    return []
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    return []

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()


#import user36_YSYfr6I5AWFWCqN_0 as week5_tests
#week5_tests.test_remove_duplicates(remove_duplicates)
#week5_tests.test_intersect(intersect)
#week5_tests.test_merge(merge)
#week5_tests.test_merge_sort(merge_sort)
    
    
