# 🌾 Farm Management System

A comprehensive web-based farm management system built with Flask (Python) and MySQL for managing farmer registrations, agro products, and farming types.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![MySQL](https://img.shields.io/badge/MySQL-10.4+-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- 🔐 **User Authentication**: Secure login and registration system
- 👨‍🌾 **Farmer Management**: Add, edit, view, and delete farmer records
- 🌾 **Agro Products**: Manage agricultural products with pricing
- 🚜 **Farming Types**: Categorize different farming methods
- 📊 **Database Triggers**: Automated audit trail for all operations
- 🔒 **Access Control**: Protected routes with login requirements

### Technical Features
- RESTful API design
- Session management with Flask-Login
- MySQL database with triggers
- Responsive web interface
- Flash messaging system
- CRUD operations for all entities

## 🛠️ Technology Stack

### Backend
- **Flask** - Python web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **Flask-Login** - User session management
- **MySQL** - Relational database

### Frontend
- **HTML5/CSS3** - Structure and styling
- **Bootstrap** - Responsive design
- **JavaScript** - Client-side interactivity
- **jQuery** - DOM manipulation

### Testing
- **pytest** - Testing framework
- **pytest-cov** - Code coverage analysis
- **Selenium** - UI testing (configured)

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- MySQL Server 10.4+
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/farm-management-system.git
cd farm-management-system
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv myvenv
.\myvenv\Scripts\activate

# Linux/Mac
python3 -m venv myvenv
source myvenv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup Database

1. Start MySQL server
2. Create database:
```sql
CREATE DATABASE farmers;
```

3. Import schema:
```bash
mysql -u root -p farmers < farmers.sql
```

### Step 5: Configure Application

Edit `main.py` line 24 with your database credentials:
```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/farmers'
```

### Step 6: Run Application

```bash
python main.py
```

The application will be available at: `http://127.0.0.1:5000`

## 🚀 Usage

### Access the Application

1. **Home Page**: `http://127.0.0.1:5000/`
2. **Login**: `http://127.0.0.1:5000/login`
3. **Signup**: `http://127.0.0.1:5000/signup`

### Default Test User

After importing the SQL file, you can use:
- Email: `arkpro@gmail.com`
- Password: Check database (hashed)

### Main Routes

| Route | Method | Description | Auth Required |
|-------|--------|-------------|---------------|
| `/` | GET | Home page | No |
| `/signup` | GET, POST | User registration | No |
| `/login` | GET, POST | User login | No |
| `/logout` | GET | User logout | Yes |
| `/register` | GET, POST | Register new farmer | Yes |
| `/farmerdetails` | GET | View all farmers | Yes |
| `/edit/<rid>` | GET, POST | Edit farmer details | Yes |
| `/delete/<rid>` | POST | Delete farmer | Yes |
| `/addagroproduct` | GET, POST | Add agro product | Yes |
| `/agroproducts` | GET | View all products | No |
| `/addfarming` | GET, POST | Add farming type | Yes |
| `/triggers` | GET | View trigger logs | Yes |

## 🧪 Testing

### Run All Tests

```bash
python run_tests.py
```

### Run Specific Tests

```bash
# Authentication tests
pytest tests/test_auth.py -v

# Farmer management tests
pytest tests/test_farmer.py -v
```

### View Coverage Report

After running tests, open `coverage_html/index.html` in your browser.

### Test Documentation

- **Test Plan**: `TEST_PLAN.md`
- **Test Cases**: `TEST_CASES.md` (25 test cases)
- **Testing Guide**: `TESTING_README.md`
- **Quick Start**: `QUICK_START_TESTING.md`

### Test Coverage

- 25+ test cases
- Black-box and white-box testing
- Unit and integration tests
- Target: >80% code coverage

## 🗄️ Database Schema

### Tables

1. **user** - User accounts
2. **register** - Farmer registrations
3. **farming** - Farming types
4. **addagroproducts** - Agricultural products
5. **trig** - Trigger audit logs
6. **test** - Database connection test

### Database Triggers

- **insertion**: Logs farmer additions
- **updation**: Logs farmer updates
- **deletion**: Logs farmer deletions

## 📁 Project Structure

```
farm-management-system/
├── main.py                  # Main application file
├── farmers.sql              # Database schema
├── requirements.txt         # Python dependencies
├── run_tests.py            # Test execution script
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_auth.py
│   └── test_farmer.py
├── templates/              # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── farmer.html
│   └── ...
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
└── Documentation/          # Test documentation
    ├── TEST_PLAN.md
    ├── TEST_CASES.md
    └── TESTING_README.md
```

## 🔮 Future Enhancements

- [ ] Email notifications
- [ ] Export data to PDF/Excel
- [ ] Dashboard with analytics
- [ ] Mobile app version
- [ ] Weather integration
- [ ] Crop recommendation system
- [ ] Multi-language support
- [ ] Payment integration

## 📊 Project Status

**Status**: Active Development  
**Version**: 1.0.0  
**Last Updated**: 2024

---

⭐ **If you find this project useful, please star the repository!** ⭐

