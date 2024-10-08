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
    

while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()   
    
    if user_action.startswith("add"):
        todo = (user_action[4:] + "\n")
        
        todos = get_todos()
                
        todos.append(todo)
        
        todos = modify_todos(todos)
                        
    elif user_action.startswith("show"):
        
        todos = get_todos()        
        new_todos = [item.strip('\n') for item in todos]
        
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
            
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()
                
            new_todo = input("Enter new todo: ") + '\n'
            todos[number - 1] = new_todo
            
            todos = modify_todos(todos)

        except ValueError:
            print("your command is invalid")
            continue
        
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()    
            
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            todos = modify_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item in that range")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("The Enter command is not valid")

print("Byee!!")    