# ✅ To Do List — Django

A clean, task management web application built with Django. Create, update, complete, and delete your daily tasks with ease.

---

## 🚀 Features

- 📝 Create, edit, and delete tasks
- ✔️ Mark tasks as complete/incomplete
- 👤 User authentication (register, login, logout)
- 🔒 Each user sees only their own tasks
- 📱 Responsive UI

---

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Backend    | Python, Django    |
| Database   | SQLite (default)  |
| Frontend   | HTML, CSS         |
| Auth       | Django Auth       |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/ahnaftnn/ToDo_list-Django-.git
cd ToDo_list-Django-
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

6. **Open in your browser**

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
ToDo_list-Django-/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── base/                  # Main app
│   ├── models.py          # Task model
│   ├── views.py           # App logic
│   ├── urls.py            # URL routes
│   └── templates/         # HTML templates
└── todo_list/                  # Project settings
    ├── settings.py
    └── urls.py
```

---

## 🗄️ Database

The project uses **SQLite** by default — no setup needed. To switch to PostgreSQL or another database, update the `DATABASES` setting in `core/settings.py`.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Ahnaf** — [@ahnaftnn](https://github.com/ahnaftnn)