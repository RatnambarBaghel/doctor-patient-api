![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🏥 Doctor Patient Management API

A scalable backend system built using **FastAPI** and **MySQL** to manage doctors, patients, and their assignments efficiently.

---

## 🚀 Features

* 👨‍⚕️ Doctor Management (CRUD)
* 🧑 Patient Management (CRUD with Soft Delete)
* 🔗 Doctor ↔ Patient Assignment System
* 🚫 Prevent duplicate assignments
* 🏥 Patient discharge system
* 🗄️ MySQL Database Integration
* 🔄 SQLAlchemy ORM with Relationships
* 📄 Interactive API Docs (Swagger UI)

---

## 🧠 Tech Stack

| Layer    | Technology |
| -------- | ---------- |
| Backend  | FastAPI    |
| Database | MySQL      |
| ORM      | SQLAlchemy |
| Language | Python     |

---

## 📁 Project Structure

```
app/
├── main.py
├── core/
│   └── database.py
├── models/
│   ├── patient.py
│   ├── doctor.py
│   └── assignment.py
├── schemas/
│   ├── patient.py
│   ├── doctor.py
│   └── assignment.py
└── routers/
    ├── patient.py
    ├── doctor.py
    └── assignment.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/doctor-patient-api.git
cd doctor-patient-api
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

## 📸 API Preview

![Swagger UI](./assets/swagger.png)

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update:

```
app/core/database.py
```

```
DATABASE_URL = "mysql+pymysql://username:password@localhost/hospital_db"
```

> ⚠️ Replace `@` in password with `%40` if needed

---

### 5️⃣ Run the server

```
uvicorn app.main:app --reload
```

---

## 📄 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

👉 Interactive Swagger UI for testing APIs

---

## 🔑 Core Endpoints

### Doctors

* `POST /doctors/`
* `GET /doctors/`
* `DELETE /doctors/{id}`

### Patients

* `POST /patients/`
* `GET /patients/`
* `DELETE /patients/{id}` (Soft Delete)

### Assignments

* `POST /assignments/`
* `GET /assignments/`
* `GET /assignments/doctor/{id}`
* `PUT /assignments/discharge/{id}`

---

## 🧠 Key Concepts

* ORM Relationships (Doctor ↔ Assignment ↔ Patient)
* Soft Delete Pattern
* Data Validation with Pydantic
* REST API Design
* Dependency Injection (FastAPI)

---

## 🔮 Future Improvements

* 🔐 JWT Authentication
* 🔑 Password Hashing
* 📅 Appointment Scheduling
* 🎨 Frontend UI (React)
* 📊 Admin Dashboard

---

## 👨‍💻 Author

**Ratnambar Baghel**

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
