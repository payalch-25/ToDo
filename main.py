import streamlit as st
import json
import os
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Streamlit To-Do Application",
    page_icon="📋",
    layout="wide"
)

# File to store tasks
TASKS_FILE = "tasks.json"

# Initialize the JSON file if it doesn't exist
def initialize_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

# Load tasks from the JSON file
def load_tasks():
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Streamlit App
def main():

    st.title("📋 Streamlit To-Do Application")
    col3, col4 = st.columns(2, vertical_alignment='top')
    with col3:
        with st.container(border=True):
            # View Tasks
            st.subheader("Your To-Do List")
            tasks = load_tasks()
            if not tasks:
                st.info("No tasks found!")
            else:
                for idx, task in enumerate(tasks, start=1):
                    # Display checkbox and task text on the same line using a column layout
                    cols = st.columns([0.04, 0.96], vertical_alignment='center')  # Adjust column widths as needed
                    with cols[0]:
                        completed = st.checkbox("", key=f"view_{idx}")  # Key prevents duplicate issues
                    with cols[1]:
                        task_text = f"*{idx}.* [{task['category'].upper()}] ({task['priority'].upper()}) {task['title']}: {task['description']}"
                        if completed:
                            task_text = f"~:gray[{task_text}]~"

                        st.markdown(task_text, unsafe_allow_html=True)
    with col4:
        # Navigation
        option = st.selectbox("Choose an option", ("Add Task", "Update Task", "Delete Task"), index=None)

        # Add Task
        if option == "Add Task":
            with st.container(border=True):
                st.subheader("Add a New Task")
                title = st.text_input("Task Title")
                description = st.text_area("Task Description")
                category = st.text_input("Task Category (e.g., Work, Personal, Study)")
                priority = st.selectbox("Task Priority", ["Low", "Medium", "High"])
                if st.button("Add Task"):
                    if title.strip() == "":
                        st.error("Title cannot be empty!")
                    else:
                        tasks = load_tasks()
                        new_task = {
                            "title": title,
                            "description": description,
                            "category": category,
                            "priority": priority
                        }
                        tasks.append(new_task)
                        save_tasks(tasks)
                        st.success("Task added successfully!")
                        st_autorefresh(interval=1000, limit=2)

        # Update Task
        elif option == "Update Task":
            st.subheader("Update a Task")
            tasks = load_tasks()
            if not tasks:
                st.info("No tasks found to update!")
            else:
                task_titles = [f"{idx + 1}. {task['title']}" for idx, task in enumerate(tasks)]
                selected_task = st.selectbox("Select a Task to Update", task_titles)
                task_index = task_titles.index(selected_task)
                task = tasks[task_index]

                title = st.text_input("Task Title", task["title"])
                description = st.text_area("Task Description", task["description"])
                category = st.text_input("Task Category", task["category"])
                priority = st.selectbox("Task Priority", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(task["priority"]))

                if st.button("Update Task"):
                    tasks[task_index] = {
                        "title": title,
                        "description": description,
                        "category": category,
                        "priority": priority
                    }
                    save_tasks(tasks)
                    st.success("Task updated successfully!")
                    st_autorefresh(interval=1000, limit=2)

        # Delete Task
        elif option == "Delete Task":
            st.subheader("Delete a Task")
            tasks = load_tasks()
            if not tasks:
                st.info("No tasks found to delete!")
            else:
                task_titles = [f"{idx + 1}. {task['title']}" for idx, task in enumerate(tasks)]
                selected_task = st.selectbox("Select a Task to Delete", task_titles)
                task_index = task_titles.index(selected_task)

                if st.button("Delete Task"):
                    deleted_task = tasks.pop(task_index)
                    save_tasks(tasks)
                    st.success(f"Task '{deleted_task['title']}' deleted successfully!")
                    st_autorefresh(interval=1000, limit=2)

# Run the Streamlit app
if _name_ == "_main_":
    initialize_file()
    main()