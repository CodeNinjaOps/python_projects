def get_todos(filename="todo.txt"):
    """ Read a text file and return the list of 
    to-do items.
    """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def modify_todos(todos_arg, filename="todo.txt"):
    """Write the to-do items list in the text file."""
    with open(filename,'w') as file_local:
        file_local.writelines(todos_arg)