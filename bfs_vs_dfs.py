import copy
import time


def input_check(start_state):
    """
    Validation of input value for grid start state

    """
    try:
        """Validating length of input value"""
        if len(start_state) != 9: 
            print("Please enter valid input for state of grid")
            return False

        """Checking for duplicate entries in the input field for start state of grid"""    
        duplicate_values = []
        input_list = list(start_state)
        for value in input_list:
            if input_list.count(value) > 1:
                duplicate_values.append(value)
        if len(duplicate_values)>0:
            print("Duplicate values present in input, please enter valid inputs")        
            return False

        """If validation is successful then return True"""    
        return True
    except Exception as exception:
        print("Exceptions occured while handling input, please enter integer type values only")
        return False


def inversion_check(start_state):
    """
    This function is used to check whether the start state of grid is even inversion or odd inversion.
    For odd inversion it cannot be solved because on every slide we add two inversion or remove two inversions,
    So only even inversions are accepted as input

    """

    try:
        length_of_start_state = len(start_state)
        count_of_inversions = 0   #Initializing count as zero
        for start in range(0, length_of_start_state):
            for next in range(start + 1, length_of_start_state):
                # Blank 'B' is not considered for inversion check
                if (int(start_state[start]) != 'B' and int(start_state[next]) != 'B' and int(start_state[start]) > int(start_state[next])):
                    count_of_inversions = count_of_inversions + 1

        """Checking for even or odd inversion"""            
        if count_of_inversions % 2 != 0:  
            print("Input value failed in inversion check, please enter valid input")
            return False
        return True
    except KeyError:
        return KeyError
    except ValueError:
        return ValueError  


def grid_update(state_of_current_grid, move, blank_position):

    """
    This function is used to do swapping of grids based on the move and blank position

    """

    """Storing current values of grid and steps"""
    current_value_of_grid = state_of_current_grid[0]
    current_value_of_steps = state_of_current_grid[1]

    """Saving a temporary copy of current value of grid to perform action on current value of grid"""
    temp_copy_of_grid = copy.deepcopy(current_value_of_grid)

    """Down move can only be done if the blank space is in 1st or 2nd row , which means index=0 to 5 i.e {<6}"""
    if move == 'Down' and blank_position < 6:
        temp_copy_of_grid[blank_position], temp_copy_of_grid[blank_position + 3] = temp_copy_of_grid[blank_position+3], temp_copy_of_grid[blank_position]
        current_value_of_steps = current_value_of_steps+1

    """Left move can only be done if the blank space is in 2nd or 3rd coloumn , which means index=(no. of coloumn)%3 i.e {>0}"""
    if move == 'Left' and (blank_position % 3) > 0:
        temp_copy_of_grid[blank_position], temp_copy_of_grid[blank_position -1] = temp_copy_of_grid[blank_position-1], temp_copy_of_grid[blank_position]
        current_value_of_steps = current_value_of_steps+1

    """Up move can only be done if the blank space is in 2nd or 3rd row , which means index=3 to 8 i.e {>2}"""
    if move == 'Up' and blank_position > 2:
        temp_copy_of_grid[blank_position], temp_copy_of_grid[blank_position -3] = temp_copy_of_grid[blank_position-3], temp_copy_of_grid[blank_position]
        current_value_of_steps = current_value_of_steps+1

    """Right move can only be done if the blank space is in 1st or 2nd coloumn , which means index=(no. of coloumn)%3 i.e {<2}"""
    if move == 'Right' and (blank_position % 3) < 2:
        temp_copy_of_grid[blank_position], temp_copy_of_grid[blank_position +1] = temp_copy_of_grid[blank_position+1], temp_copy_of_grid[blank_position]
        current_value_of_steps = current_value_of_steps+1

    return [temp_copy_of_grid, current_value_of_steps]


def depth_first_search(input_grid, target_grid):
    """
    This function is used for depth first search with parameters input grid value and target grid value
    
    """
    dfs_stack = [] #Initilizing a stack for DFS
    grid_set = set()
    steps_count = 0  # Initilizing step counts as 0
    dfs_stack.append([input_grid, steps_count])

    """setting a start time to evalute processing time for DFS"""
    start_time = time.time()

    while dfs_stack:
        state_of_current_grid = dfs_stack.pop() #Taking a value out from dfs stack to keep it in current state of grid
        current_grid = state_of_current_grid[0]

        if (current_grid == target_grid):
            time_difference = time.time()-start_time #Calculating execution time for DFS
            print("*****Target grid found in DFS*****")
            print("Target grid found by DFS in:", time_difference,"sec")
            dfs_steps = state_of_current_grid[1]
            return [dfs_steps, time_difference]

        """If current grid does not matches with target grid then check that it present in grid set or not"""    
        grid = "".join(current_grid)
        if (grid not in grid_set):
            grid_set.add(grid)
            for move in ["Down", "Left", "Up", "Right"]:

                """Make a move in the grid with the current state of grid to obtain a moved state of grid"""
                updated_grid = grid_update(
                    state_of_current_grid, move, current_grid.index('B'))

                """Compare the target grid with moved state of grid"""    
                if (updated_grid[0] == target_grid):
                    print("*****Target grid found in DFS*****")

                    """Calculate execution time for DFS"""
                    time_difference = time.time()-start_time
                    print("Target grid found by DFS in:", time_difference,"sec")
                    dfs_steps = updated_grid[1]
                    return [dfs_steps, time_difference]
                dfs_stack.append(updated_grid)


def breadth_first_search(input_grid, target_grid):
    """
    This function is used for breadth first search with parameters input grid value and target grid value
    
    """
    bfs_queue = [] #Initilizing a queue for BFS
    grid_set = set()
    steps_count = 0
    bfs_queue.append([input_grid, steps_count])

    """setting a start time to evalute processing time for DFS"""
    bfs_start_timestamp = time.time()

    while bfs_queue:
        """Taking a value out from dfs stack to keep it in current state of grid"""
        state_of_current_grid = bfs_queue.pop(0)
        current_grid = state_of_current_grid[0]

        if (current_grid == target_grid):
            print("*****Target Grid Found in BFS*****")
            time_difference = time.time()-bfs_start_timestamp
            print("Target Grid Found by BFS in:",
                  time_difference,"sec")
            steps_count = state_of_current_grid[1]
            return [steps_count, time_difference]

        """If current grid does not matches with target grid then check that it present in grid set or not"""
        grid = "".join(current_grid)
        if (grid not in grid_set):
            grid_set.add(grid)
            for move in ['Down', 'Left', 'Up', 'Right']:
                """Make a move in the grid with the current state of grid to obtain a moved state of grid"""
                updated_grid = grid_update(
                state_of_current_grid, move, current_grid.index('B'))

                """Compare the target grid with moved state of grid"""
                if (updated_grid[0] == target_grid):
                    print("*****Target Grid Found in BFS*****")
                    """Calculate execution time for DFS"""
                    time_difference = time.time()-bfs_start_timestamp
                    print("Target Grid Found by BFS in:", time_difference,"sec")
                    steps_count = updated_grid[1]
                    return [steps_count, time_difference]
                bfs_queue.append(updated_grid)




if __name__ == "__main__":
    try:
        """
        Taking input for start state and goal state of grid

        """
        start_state = input("Enter the values of start state of grid: ")
        goal_state = input("Enter the values of goal state of grid: ")
        
        """Checking for input value validation and inversion check of input values"""
        if input_check(start_state) and inversion_check(start_state):

            """Calling DFS function to evaluate steps and execution time in DFS"""
            steps_in_dfs, execution_time_of_dfs = depth_first_search(
                list(start_state), list(goal_state))

            """Calling BFS function to evaluate steps and execution time in BFS"""
            steps_in_bfs, execution_time_of_bfs = breadth_first_search(
                list(start_state), list(goal_state))

            """Calculating Difference in steps"""    
            difference_in_steps=0
            if steps_in_bfs>=steps_in_dfs:
                difference_in_steps=steps_in_bfs-steps_in_dfs
            else:
                difference_in_steps=steps_in_dfs-steps_in_bfs   

            """Result of evaluation"""     
            print("=================================")
            print("COMPARISION RESULT OF DFS vs BFS")
            print("=================================")
            if execution_time_of_dfs > execution_time_of_bfs:
                print("Execution of BFS is faster than DFS by",
                      execution_time_of_dfs-execution_time_of_bfs,"sec for the given input grid")
                print("Steps taken by BFS is:", steps_in_bfs,
                      " and by DFS is:", steps_in_dfs)
                print("Difference in steps is:", difference_in_steps)
            else:
                print("Execution of DFS is faster than BFS by",
                      execution_time_of_bfs-execution_time_of_dfs, "sec for the given input grid")
                print("Steps taken by BFS is:", steps_in_bfs,
                      " and by DFS is:", steps_in_dfs)
                print("Difference in steps is:", difference_in_steps)

        else:
            raise Exception
    except Exception as exception:
        print("Exit : Please correct your grid values")



