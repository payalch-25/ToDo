import sqlite3
import streamlit as st

# Connect to SQLite database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    priority TEXT NOT NULL,
    deadline TEXT NOT NULL
)
''')

conn.commit()

def add_task(title, description, category, priority, deadline):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO tasks (title, description, category, priority, deadline)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, category, priority, deadline))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

def view_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_task(task_id, title, description, category, priority, deadline):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        UPDATE tasks
        SET title = ?, description = ?, category = ?, priority = ?, deadline = ?
        WHERE id = ?
    ''', (title, description, category, priority, deadline, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Page Title
st.title("To-Do App with SQLite")

option = st.selectbox("Select an option", ["Add Task", "Update Task"], index=None)

if option == "Add Task":
    with st.container(border=True):
        # Add a Task
        st.header("Add a Task")
        title = st.text_input("Task Title")
        description = st.text_area("Description")
        category = st.text_input("Category")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        deadline = st.date_input("Deadline")

        if st.button("Add Task"):
            if title and deadline:
                add_task(title, description, category, priority, deadline.strftime('%Y-%m-%d'))
                st.success("Task added successfully!")
            else:
                st.error("Please provide a title and deadline.")

elif option == "Update Task":
    with st.container(border=True):
        # Update Tasks
        st.header("Update a Task")
        update_id = st.number_input("Enter Task ID to Update", min_value=1, step=1)
        new_title = st.text_input("New Title")
        new_description = st.text_area("New Description")
        new_category = st.text_input("New Category")
        new_priority = st.selectbox("New Priority", ["Low", "Medium", "High"])
        new_deadline = st.date_input("New Deadline", key="update_deadline")

        if st.button("Update Task"):
            update_task(update_id, new_title, new_description, new_category, new_priority, new_deadline.strftime('%Y-%m-%d'))
            st.success("Task updated successfully!")

st.header("View Tasks")
tasks = view_tasks()

with st.container(border=True):
    for task in tasks:
        col0, col1, col2 = st.columns([0.04, 0.60, 0.16], vertical_alignment='center', gap='small')
        with col0:
            completed = st.checkbox("", key=f"view_{task[0]}")

        with col1:
            task_text = f"**{task[0]}.** **{task[1]}** - :blue-background[{task[4]}] ***:orange[(Due: {task[5]})]***  \n :green-background[Category: {task[3]}] | Description: {task[2]}"
            if completed:
                task_text = f"~~:gray[{task_text}]~~"
            st.markdown(task_text, unsafe_allow_html=True)

        with col2:
            if st.button(f":red[:material/delete: Delete Task]", key=f"del_{task[0]}"):
                delete_task(task[0])
                st.rerun()