import psutil
import os

# Graph search agent function
def my_graph_search_agent(problem):
    frontier = [] # Stores states to be explored
    explored_set = set() # Keeps track of explored states
    
    # Add initial state to the frontier
    frontier.append(problem.initial_state)
    
    # Main loop continues until the frontier is not empty
    while frontier:
        # Pop the current state from the frontier
        current_state = frontier.pop(0) 
        
        # Check if the current state is the goal state
        if problem.is_goal_state(current_state):
            # If the goal is found, return the reconstructed path
            return my_reconstruct_path(current_state)
        
        # Add the current state to the explored set
        explored_set.add(current_state)
        
        # Explore neighboring states
        for action in problem.actions(current_state):
            next_state = problem.result(current_state, action)
            
            # Check if the next state is not explored or in the frontier
            if next_state not in explored_set and next_state not in frontier:
                # Add the next state to the frontier
                frontier.append(next_state)
    
    # If the frontier becomes empty and the goal is not found, return failure
    return "failure"

# Backtracking path function
def my_backtracking_path(source_state, goal_state):
    path = [] # Stores the backtracked path
    current_state = goal_state # Start from the goal state
    
    # Backtrack until reaching the source state
    while current_state != source_state:
        # Find the action taken to reach the current state
        action = my_action_taken_to_reach(current_state) 
        
        # Prepend the action to the path
        path.insert(0, action)
        
        # Move to the parent state of the current state
        current_state = my_parent_of(current_state) 
    
    # Return the backtracked path
    return path

# Generate actions for Puzzle-8
def my_generate_actions(state):
    actions = []
    empty_index = state.index('_')
    row, col = divmod(empty_index, 3)
    if row > 0:
        actions.append('Up')
    if row < 2:
        actions.append('Down')
    if col > 0:
        actions.append('Left')
    if col < 2:
        actions.append('Right')
    return actions

# Apply action to generate next state for Puzzle-8
def my_apply_action(state, action):
    new_state = list(state)
    empty_index = new_state.index('_')
    if action == 'Up':
        new_state[empty_index], new_state[empty_index - 3] = new_state[empty_index - 3], new_state[empty_index]
    elif action == 'Down':
        new_state[empty_index], new_state[empty_index + 3] = new_state[empty_index + 3], new_state[empty_index]
    elif action == 'Left':
        new_state[empty_index], new_state[empty_index - 1] = new_state[empty_index - 1], new_state[empty_index]
    elif action == 'Right':
        new_state[empty_index], new_state[empty_index + 1] = new_state[empty_index + 1], new_state[empty_index]
    return tuple(new_state)

# Get current process's memory usage
def my_memory
