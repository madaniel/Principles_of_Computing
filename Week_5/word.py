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
    
    for idx in range( len(list1) - 1 ):
        if list1[idx] != list1[idx+1]:
            temp.append(list1[idx])
            
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
        short_list = list1
        long_list = list2
    else:
        short_list = list2
        long_list = list1
        
    for idx in range(len(short_list) ):
        if short_list[idx] in long_list:
            temp.append(short_list[idx])
    return temp

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    temp = []
           
    if len(list1) < len(list2):
        short_list = list(list1)
        long_list = list(list2)
    else:
        short_list = list(list2)
        long_list = list(list1)
    
    while len(short_list) > 0 and len(long_list) > 0:
        if short_list[0] < long_list[0]:
            temp.append(short_list.pop(0))
        else:
            temp.append(long_list.pop(0))
    
  
    while len(short_list) > 0:
        temp.append(short_list.pop(0))
    
    while len(long_list) > 0:
        temp.append(long_list.pop(0))
        
        
    
        
    return temp
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    else:
        mid = int(len(list1) / 2)
        return merge(merge_sort(list1[:mid]),merge_sort(list1[mid:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) < 1:
        return [""]
    
    first = word[0]    
    rest = word[1:]  

    rest_strings = gen_all_strings(rest)    
    copy_list = list(rest_strings)
    for item in rest_strings:
        if (len(item) == 0):
            copy_list.append(first)
        else:
            for idx in range( len(item)+1):
                copy_list.append(item[:idx] + first + item[idx:])
               
    return copy_list

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

#import user36_FF1tf9hk4VlRZ82 as testsuite

#testsuite.run_test1(remove_duplicates)
#testsuite.run_test2(intersect)
#testsuite.run_test3(merge)
#testsuite.run_test4(merge_sort)
#testsuite.run_test5(gen_all_strings)

#testsuite.run_all(remove_duplicates, intersect, merge, merge_sort, gen_all_strings)


#print gen_all_strings("abc")



