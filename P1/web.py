import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.modify_todos(todos)

sl.title("Todo list Web Application")
sl.subheader("This is my todo app")
sl.write("This app to increase your productivity")


for todo in todos:
    sl.checkbox(todo)

sl.text_input(label="",placeholder="Add new todo ....",on_change=add_todo,key="new_todo")