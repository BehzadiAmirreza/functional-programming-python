def create_history():
    # states = ["", "Hello", "Hello, World!"]
    # current_index = 1    
    
    return ([""], 0)

def edit(history, new_text):
    states, current_index = history
    new_states = states[:current_index + 1] + [new_text]
    return (new_states, current_index + 1) 

def undo(history):
    states, current_index = history
    new_index = max(0, current_index - 1)
    return (states, new_index)

def redo(history):
    states, current_index = history
    new_index = min(len(states) - 1, current_index + 1)
    return (states, new_index)

def current_state(history):
    states, current_index = history    
    return states[current_index]

history = create_history() # create a new history object
history = edit(history, "Hello") # add a new edit to the history
history = edit(history, "Hello, World!") # add another edit to the history
history = undo(history) # undo the last edit; resulting history: "Hello"
history = redo(history) # redo the last edit; resulting history: "Hello, World!"
history = undo(history) # undo the last edit; resulting history: "Hello" 