def get_todos():
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
    return todos

def modify_todos():
    with open('todo.txt','w') as file:
        file.writelines(todos)
    return todos
    

while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()   
    
    if user_action.startswith("add"):
        todo = (user_action[4:] + "\n")
        
        todos = get_todos()
                
        todos.append(todo)
        
        todos = modify_todos()
                        
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
                
            todos = get_todos()
            
            todos = modify_todos()

        except ValueError:
            print("your command is invalid")
            continue
        
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()    
            
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(todo_to_remove - 1)

            todos = modify_todos()

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