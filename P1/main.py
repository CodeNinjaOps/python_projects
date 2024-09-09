todos = []

while True:
    user_action = input("Type add,show,edit or exit: ")
    user_action = user_action.strip()   
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
        case 'exit':
            break
        case whatever:
            print("The Command You Enter Is Unknown")