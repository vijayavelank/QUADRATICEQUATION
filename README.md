# 📝 Quadratic Equation Solver (Flask + Docker)

This project is a **Quadratic Equation Solver** built using **Flask** and deployed using **Docker**. It provides a web interface to solve quadratic equations of the form:

\[ ax^2 + bx + c = 0 \]

## 🚀 Features
- Solves quadratic equations instantly.
- Supports both real and complex roots.
- Provides user-friendly error messages.
- Runs in a **Docker container** for easy deployment.
- Works with **Gunicorn** for production.

## 🛠️ Technologies Used
- **Flask** - Web framework for backend logic.
- **Gunicorn** - WSGI server for production.
- **Docker** - Containerized deployment.
- **HTML & CSS** - Frontend UI.
- **Python 3.9+** - Core programming language.

## 📥 Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/quadratic-solver.git
cd quadratic-solver
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Locally
```bash
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

### 4️⃣ Run with Gunicorn (Production Mode)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🐳 Deploy with Docker
### 1️⃣ Build the Docker Image
```bash
docker build -t quadratic-solver .
```

### 2️⃣ Run the Container
```bash
docker run -p 5000:5000 quadratic-solver
```
Access the app at `http://localhost:5000/`.

## 📂 Project Structure
```
📂 quadratic-solver
│-- app.py                # Flask app logic
│-- templates/
│   ├── index.html        # UI template
│-- requirements.txt      # Dependencies
│-- Dockerfile            # Docker setup
│-- README.md             # Documentation
```

