# 📝 To-Do App with Streamlit

A simple and interactive To-Do application built using **Streamlit**. The app allows users to manage tasks with an intuitive UI. It comes with two implementations: 
- A **basic version** that manages tasks in memory (no database).
- An **advanced version** that connects to an SQLite database for persistent task management.

---

## 🚀 Features

### Basic Version (Without Database)
- Add tasks with a title, description, category, priority, and deadline.
- View a list of tasks.
- Delete tasks.
- All data is stored in memory.

### Advanced Version (With SQLite Database)
- Add, view, update, and delete tasks with full CRUD operations.
- Task data is stored in an SQLite database for persistence.
- Interactive UI to manage tasks efficiently.

---

## 📦 Requirements

- Python 3.7 or higher
- Streamlit

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/payalch-25/ToDo.git
   cd ToDo
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install streamlit
   ```

---

## ▶️ How to Run

### Basic Version (Without Database)

1. Open the file `main.py`.
2. Run the app:
   ```bash
   streamlit run main.py
   ```

3. Interact with the app through your web browser.

---

### Advanced Version (With SQLite Database)

1. Open the file `app.py`.
2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. The database file (`todo.db`) will be created in the project directory if it doesn’t exist.

---

## 📂 File Structure

```plaintext
.
├── README.md
├── main.py      # Basic version (no database)
├── app.py    # Advanced version with SQLite
└── todo.db            # SQLite database (auto-created)
```

---

## 🔧 Usage Details

### Basic Version (Without Database)
- This version uses Python lists to manage tasks in memory.
- Tasks are lost when the app restarts.
- Ideal for quick prototyping or short-lived task management.

### Advanced Version (With SQLite Database)
- Stores tasks in an SQLite database for persistence.
- Supports updating existing tasks along with adding, viewing, and deleting.
- Designed for use cases where persistent task storage is required.

---

## 🤝 Contributions

Feel free to contribute! Fork the repository, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.