while True:
    user_action = input("Type add,show,edit,completed or exit: ")
    user_action = user_action.strip()   
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('todo.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'show' | 'display':
            file  = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
                
        case 'edit':
            number = int(input("Number of todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
            
        case 'complete':
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)
            
        case 'exit':
            break
        
        case whatever:
            print("The Command You Enter Is Unknown")