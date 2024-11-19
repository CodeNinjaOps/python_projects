import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.modify_todos(todos)
    st.session_state["new_todo"] = ""

st.title("Todo list Web Application")
st.subheader("This is my todo app")
st.write("This app to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    print(f"index:{index}, todo:{todo}")
    if checkbox:
        todos.pop(index)
        functions.modify_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo ....",on_change=add_todo,key="new_todo")

st.session_state
