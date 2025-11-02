# 🏕️ Pilgrimap

**Pilgrimap** is a web platform built with **Django** that lets travelers discover, create, and book hostels and rooms.  
It includes an owner dashboard and a simple UI for guests.

---

## 🚀 Features

### For Travelers
- Browse all **hostels**
- View each hostel’s **rooms**
- Book a room
- (Soon) Manage your reservations

### For Hostel Owners
- Create and manage **hostels**
- Add **rooms** to each hostel
- Edit and delete listings

### General
- Responsive UI with **Bootstrap**
- Authentication (login/logout/register)
- SQLite for local dev
- Clean URL routing, modular apps

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django 4.2 |
| Language | Python 3.9+ |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap |
| Auth | Django Auth |

---

## ⚙️ Setup (Local)

# 🏕️ Pilgrimap

**Pilgrimap** is a web platform built with **Django** that lets travelers discover, create, and book hostels and rooms.  
It includes an owner dashboard and a simple UI for guests.

---

## 🚀 Features

### For Travelers
- Browse all **hostels**
- View each hostel’s **rooms**
- Book a room
- (Soon) Manage your reservations

### For Hostel Owners
- Create and manage **hostels**
- Add **rooms** to each hostel
- Edit and delete listings

### General
- Responsive UI with **Bootstrap**
- Authentication (login/logout/register)
- SQLite for local dev
- Clean URL routing, modular apps

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django 4.2 |
| Language | Python 3.9+ |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap |
| Auth | Django Auth |

---

## ⚙️ Setup (Local)

```bash
git clone https://github.com/cmichel0369/pilgrimap.git
cd pilgrimap
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows (PowerShell)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

