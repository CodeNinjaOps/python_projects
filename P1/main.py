while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()   
    
    if user_action.startswith("add"):
        todo = (user_action[4:] + "\n")
        
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo)
        
        with open('todo.txt','w') as file:
            file.writelines(todos)
                        
    elif user_action.startswith("show"):
        
        with open('todo.txt', 'r') as file:
            todos = file.readlines()            
        
        new_todos = [item.strip('\n') for item in todos]
        
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
            
    elif user_action.startswith("edit"):
        number = int(user_action[5:])

        with open('todo.txt', 'r') as file:
            todos = file.readlines()    
            
        new_todo = input("Enter new todo: ") + '\n'
        todos[number - 1] = new_todo

        with open('todo.txt','w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open('todo.txt', 'r') as file:
            todos = file.readlines()    
        
        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number - 1)

        with open('todo.txt','w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
        
    elif user_action.startswith("exit"):
        break
    else:
        print("The Enter command is not valid")

print("Byee!!")    