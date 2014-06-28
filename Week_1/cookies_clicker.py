"""
Cookie Clicker Simulator
"""

import simpleplot , math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 50.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._cps = 1.0
        self._current_time = 0.0
        self._history = [(0.0, None, 0.0, 0.0)]
        # a time 
        # an item bought at this time (or None)
        # cost of the item
        # total number of cookies produced until time
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Total cookies = "  + str(self._total_cookies) + "\nCurrent cookies= " + str(self._current_cookies) +  "\nCPS = " + str(self._cps) + "\nCurrent Time = " + str(self._current_time)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies <= self._current_cookies:
            return 0.0
        
        result = (cookies - self._current_cookies) / self._cps
        
        return math.ceil(result)
        
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time > 0:
            self._current_time += time
            self._current_cookies += (self._cps * time)
            self._total_cookies += (self._cps * time)                     
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._cps += additional_cps
            self._history.append( (self._current_time,item_name,cost,self._total_cookies))                                 
       
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    clicker = ClickerState()
            
    info = build_info.clone()	
    
    while ( duration >= clicker.get_time() ):        
        next_item = strategy(clicker.get_cookies() , clicker.get_cps() , duration - clicker.get_time() , info)
                        
        if next_item == None:
            break
            
        cost_required = info.get_cost(next_item)       
        time_required = clicker.time_until(cost_required)
                
        if (time_required + clicker.get_time() ) > duration:			            
            break
            
        clicker.wait(time_required)            
        clicker.buy_item(next_item, info.get_cost(next_item), info.get_cps(next_item) )
        info.update_item(next_item)
    clicker.wait(duration - clicker.get_time())
        
    return clicker

def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Takes the cheapest item in the item list    
    """
    items = build_info.build_items()
    prices = []
    
    for item in items:
        prices.append( build_info.get_cost(item) )
    
    target = min(prices)	
    cheapest_index = prices.index(target)	
    
    available_cookies = cookies + (cps * time_left)
    
    if target > available_cookies:
        return None		
    else:
        return str(items[cheapest_index])

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Take the most expensive item in the list
    """
    items = build_info.build_items()
    prices = []
    
    for item in items:
        prices.append( build_info.get_cost(item) )
    
    target = sorted(prices)[-1]
    target_index = prices.index(target)	
    
    # check if user can afford it
    available_cookies = cookies + (cps * time_left)    
    if target > available_cookies:
        return None		
    
    return str(items[target_index])

def strategy_best(cookies, cps, time_left, build_info):
    """
    Takes the most expensive item it can afford
    """
    items = build_info.build_items()
    prices = []
    
    
    for item in items:
        prices.append( build_info.get_cost(item) )
        
    available_cookies = cookies + (cps * time_left)
    
    for price in sorted(prices , reverse = True):
        if price > available_cookies:
            continue
        else:
            target_index = prices.index(price)
            return str(items[target_index])
    
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor)
    

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    print
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    print
    run_strategy("Best", SIM_TIME, strategy_best)
    

#run()


