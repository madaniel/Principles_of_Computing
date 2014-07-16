"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._zombie_list = []
        self._human_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row , col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
                  
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row , col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        return
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        # initialize
        visited = poc_grid.Grid(self.get_grid_height() , self.get_grid_width() )
        init_value_distance_field = self.get_grid_height() * self.get_grid_width()
        distance_field = [[init_value_distance_field for x in range( self.get_grid_width() )] for y in range( self.get_grid_height() ) ] 
         
        # Turn the list of zombie / human into Queue object
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            copy_list = list(self._zombie_list)
        elif entity_type == HUMAN:
            copy_list = list(self._human_list)
        
        if not copy_list:
            return
        
        # following the list , update the visited list to "Full" state
        for cell in copy_list:
            boundary.enqueue(cell)
            visited.set_full(cell[0] , cell[1])
            distance_field[cell[0]][cell[1]] = 0
        
        # For each neighbor_cell, check whether the cell is passable and update the neighbor's distance to be the minimum of its current distance and distance_field[cell_index[0]][cell_index[1]] + 1.
        distance = 1
        
        while len(boundary) != 0:
            current_cell = boundary.dequeue()		
            neighbors = self.four_neighbors(current_cell[0], current_cell[1])
                        
            for neighbor in neighbors:                
                if visited.is_empty(neighbor[0] , neighbor[1]) and self.is_empty(neighbor[0] , neighbor[1]):
                    distance = distance_field[current_cell[0]][current_cell[1]] + 1
                    visited.set_full(neighbor[0] , neighbor[1])
                                        
                    if distance < distance_field[neighbor[0]][neighbor[1]]:
                        distance_field[neighbor[0]][neighbor[1]] = distance
                    
                    boundary.enqueue(neighbor)
            
        return distance_field
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        # 1. Scan all applicable neighbours for each human.
        # 2. Find to maximum distance cell to move to
        # 3. Append this position to a temp list
        # 4. set the humans list to be the temp list
        
        temp_humans_list = []
        
        for human in self.humans():
            max_position = human
            current_distance = zombie_distance[ human[0] ] [ human[1] ]
            maximum_distance = current_distance
            
            neighbors = self.eight_neighbors(human[0], human[1])
            # find the maximum distance, if exists
            for neighbor in neighbors:
                if self.is_empty(neighbor[0] , neighbor[1]) and zombie_distance [ neighbor[0] ] [ neighbor[1] ] > maximum_distance :
                    maximum_distance = zombie_distance [ neighbor[0] ] [ neighbor[1] ]
                    max_position = (neighbor[0] , neighbor[1] )
                                
            # save the new / current position of human
            temp_humans_list.append(max_position)
            
            # update the grid
            #if max_position != human:
            #	self.set_full(max_position[0] , max_position[1])
            #	self.set_empty(human[0] , human[1])
        
        self._human_list = temp_humans_list
                    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        temp_zombies_list = []
        
        for zombie in self.zombies():
            min_position = zombie
            current_distance = human_distance[ zombie[0] ] [ zombie[1] ]
            minimum_distance = current_distance
            
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            # find the minimum distance, if exists
            for neighbor in neighbors:
                if self.is_empty(neighbor[0] , neighbor[1]) and human_distance [ neighbor[0] ] [ neighbor[1] ] < minimum_distance :
                    minimum_distance = human_distance [ neighbor[0] ] [ neighbor[1] ]
                    min_position = (neighbor[0] , neighbor[1] )
                                
            # save the new / current position of human
            temp_zombies_list.append(min_position)
            
            # update the grid
            #if max_position != human:
            #	self.set_full(max_position[0] , max_position[1])
            #	self.set_empty(human[0] , human[1])
        
        self._zombie_list = temp_zombies_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(30, 40))



#import user35_EPZOWWGoUeaEemm as test
#test.phase1_test(Zombie)
#test.phase2_test(Zombie)
#test.phase3_test(Zombie)
