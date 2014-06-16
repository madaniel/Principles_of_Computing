"""
Clone of 2048 game.
"""

import poc_2048_gui , random as rn  

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

INIT_TILES = {}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Generate target list to copy with 0 number
    result_idx = 0
    result = [0] * len(line)

    # copying only the numbers w/o zeros
    for cell in line:
        if cell != 0:
            result[result_idx] = cell
            result_idx += 1
    
    # merging equal close numbers
    for i in range (0, len(result)-1 ):
        if result[i] == result[i+1]:
            result[i] = result[i] + result[i+1]
            result[i+1] = 0
            
    # copying only the numbers w/o zeros
    temp = [0] * len(result)
    temp_idx = 0
    
    for cell in result:
        if cell != 0:
            temp[temp_idx] = cell
            temp_idx += 1
    
    result = list(temp)
    
    return result   
    
    
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        global INIT_TILES
        self.grid = [[]]
        self.grid_height = grid_height
        self.grid_width = grid_width        
        INIT_TILES = {
        UP : [ (0 , dummy_x) for dummy_x in range(grid_width) ] , 
        DOWN : [ (grid_height - 1 , dummy_x) for dummy_x in range( grid_width ) ] ,
        RIGHT : [ (dummy_x , grid_width - 1 ) for dummy_x in range( grid_height ) ] ,
        LEFT: [ ( dummy_x , 0 ) for dummy_x in range(grid_height)] }
        self.reset()        

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for dummy_x in range(self.grid_width)] for dummy_y in range(self.grid_height)]        
            
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for row in self.grid:
            string += str(row)
            string += "\n"
            
        return string    

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return int(self.grid_height)
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """        
        return int(self.grid_width)
                
    def move(self, direction):        
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # temp will be the array copy to send into merge
        temp = []
        temp_length = 0
        
        # calc temp length as width or height of grid
        if self.get_grid_width() == len( INIT_TILES[direction] ):
            temp_length = self.get_grid_height()
        else:
            temp_length = self.get_grid_width()
        
        
        # 1. Take the 1st cell coordinates in init_tiles as start position to start temp scan
        # 2. Start copying temp from starting coordicates into end of temp
        # 3. Forward the index on init_tiles to the next cell, take this point and repeat step 2
        
        # init_tiles[direction] = array of points
        # init_tiles[direction][x] = point
        # init_tiles[direction][x][0] = row of point
        # init_tiles[direction][x][1] = col of point
        
        # This loop walk over the init_tile
        for cell in INIT_TILES[direction]:
            row = cell[0]
            col = cell[1]
            # Collect cells and copy to temp list
            for dummy_temp_tile in range(temp_length):
                temp.append(self.get_tile(row,col))
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
            temp = merge(temp)            
            # Set the tiles on the grid
            row = cell[0]
            col = cell[1]
            
            for number in temp:                
                self.set_tile(row,col,number)
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
            temp = []
        
        self.new_tile()
        
           
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        col = rn.randrange(0,self.get_grid_width())
        row = rn.randrange(0,self.get_grid_height())        
        value = rn.choice([2,2,2,2,2,2,2,2,2,4])
        
        while self.get_tile(row , col) != 0:
            col = rn.randrange(0,self.get_grid_width())
            row = rn.randrange(0,self.get_grid_height())
        
        self.set_tile(row , col,value)          
          
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col]
    

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
