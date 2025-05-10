# Rock, Paper, Scissors

This project implements the classic game in Python using two interfaces:

- ✅ A command-line interface (`cli/`)
- ✅ A browser-based app using Streamlit (`web/`)
- 🧪 Includes simple test cases

---

## 🗂️ Project Structure

```
game_rock_paper_scissors/
├── cli/
│   ├── play_game.py         # CLI version of the game
│   ├── test_game.py         # Tests using assert statements
│
├── web/
│   └── app.py               # Streamlit app version
│
├── venv/                    # Virtual environment (optional, in .gitignore)
├── requirements.txt         # Python package dependencies
├── .gitignore
└── README.md
```

---

## 🎮 How to Play – CLI Version

```bash
cd cli
python play_game.py
```

---

## 🌐 How to Launch – Streamlit Web App

```bash
streamlit run web/app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Run the Tests

```bash
cd cli
python test_game.py
```

You'll see `All tests passed!` if everything is working correctly.

---

## ⚙️ Setup Instructions

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

2. **Activate it**:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Example `requirements.txt`

You can generate it using:

```bash
pip freeze > requirements.txt
```

Typical contents:
```
streamlit
```

---

## 📄 .gitignore (sample)

Make sure you exclude environment files:

```
venv/
__pycache__/
*.pyc
*.DS_Store
```

---

## ✅ You're All Set!

Fork it, build on it, or deploy it to [Streamlit Cloud](https://streamlit.io/cloud) to share it with others.

Enjoy building with Python 🚀