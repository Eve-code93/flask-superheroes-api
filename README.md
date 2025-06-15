# Superheroes Flask API


A RESTful Flask API for managing heroes, their powers, and their abilities.  
Built for educational purposes and designed to demonstrate full-stack API design using Flask, SQLAlchemy, Flask-Migrate, and proper REST conventions.

---

##  Features

- Manage Heroes (`/heroes`)
- Manage Powers (`/powers`)
- Manage Hero Powers (`/hero_powers`)
- Full CRUD operations for Powers and Hero Powers
- Validations with informative error handling
- Database migrations using Flask-Migrate
- Full testing via provided Postman collection

---

## Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (for development)
- Postman (for API testing)

---

## Project Structure

```bash
.
├── app/
│   ├── __init__.py      # App factory & configuration
│   ├── models.py        # SQLAlchemy models & validations
│   ├── routes.py        # All API routes
│   └── config.py        # Database configurations
├── migrations/          # Flask-Migrate migrations
├── seed.py              # Seed data to populate database
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore
└── run.py               # Entry point to start Flask server
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables (optional)
If you need:
export FLASK_APP=run.py
export FLASK_ENV=development
On Windows (PowerShell):

powershell

$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"

5️⃣ Initialize Database Migrations
If not already done:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

6️⃣ Seed the Database
python seed.py

7️⃣ Run The Server
flask run
Your server will be running at http://127.0.0.1:5000/

🔎 API Endpoints
✅ Heroes
Method	Endpoint	Description
GET	/heroes	Get list of heroes
GET	/heroes/:id	Get hero details

✅ Powers
Method	Endpoint	Description
GET	/powers	Get list of powers
GET	/powers/:id	Get power details
PATCH	/powers/:id	Update power description

✅ Hero Powers
Method	Endpoint	Description
POST	/hero_powers	Create new hero power

✅ Validations
Power.description must be at least 20 characters.

HeroPower.strength must be one of: "Strong", "Average", "Weak".

Proper error handling on invalid inputs.

🧪 Testing with Postman
You can use the provided Postman collection:

Open Postman.

Import challenge-2-superheroes.postman_collection.json.

All API routes are pre-configured.

Start your Flask server and test all routes directly.


📄 License
This project is for educational use only.

---
