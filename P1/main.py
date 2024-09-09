while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()   
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            with open('todo.txt','w') as file:
                file.writelines(todos)
                            
        case 'show' | 'display':
            
            with open('todo.txt', 'r') as file:
                todos = file.readlines()            
            
            new_todos = [item.strip('\n') for item in todos]
            
            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
                
        case 'edit':
            number = int(input("Number of todo to edit: "))

            with open('todo.txt', 'r') as file:
                todos = file.readlines()    
                
            new_todo = input("Enter new todo: ") + '\n'
            todos[number - 1] = new_todo

            with open('todo.txt','w') as file:
                file.writelines(todos)
            
        case 'complete':
            number = int(input("Number of todo to complete: "))

            with open('todo.txt', 'r') as file:
                todos = file.readlines()    

            todos.pop(number - 1)

            with open('todo.txt','w') as file:
                file.writelines(todos)

            
        case 'exit':
            break
        
        case whatever:
            print("The Command You Enter Is Unknown")