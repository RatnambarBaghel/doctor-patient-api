<<<<<<< HEAD
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🏥 Doctor Patient Management API

A scalable backend system built using **FastAPI** and **MySQL** to manage doctors, patients, and their assignments efficiently.
=======
# 🏥 Doctor Patient Management API

A backend system built using **FastAPI** and **MySQL** to manage doctors, patients, and their assignments (appointments/relationships).
>>>>>>> c0abe50 (Clean FastAPI project setup)

---

## 🚀 Features

<<<<<<< HEAD
* 👨‍⚕️ Doctor Management (CRUD)
* 🧑 Patient Management (CRUD with Soft Delete)
* 🔗 Doctor ↔ Patient Assignment System
* 🚫 Prevent duplicate assignments
* 🏥 Patient discharge system
* 🗄️ MySQL Database Integration
* 🔄 SQLAlchemy ORM with Relationships
* 📄 Interactive API Docs (Swagger UI)
=======
* 👨‍⚕️ Doctor Management (Create, Read, Delete)
* 🧑‍🤝‍🧑 Patient Management (Create, Read, Soft Delete)
* 🔗 Doctor ↔ Patient Assignment System
* ❌ Prevent duplicate assignments
* 🏥 Discharge patients from doctors
* 🗄️ MySQL Database Integration
* 🔄 SQLAlchemy ORM with Relationships
* 📄 Auto API Docs using Swagger UI
>>>>>>> c0abe50 (Clean FastAPI project setup)

---

## 🧠 Tech Stack

<<<<<<< HEAD
| Layer    | Technology |
| -------- | ---------- |
| Backend  | FastAPI    |
| Database | MySQL      |
| ORM      | SQLAlchemy |
| Language | Python     |
=======
* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Language:** Python
>>>>>>> c0abe50 (Clean FastAPI project setup)

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

<<<<<<< HEAD
## ⚙️ Installation & Setup
=======
## ⚙️ Setup Instructions
>>>>>>> c0abe50 (Clean FastAPI project setup)

### 1️⃣ Clone the repository

```
<<<<<<< HEAD
git clone https://github.com/YOUR_USERNAME/doctor-patient-api.git
cd doctor-patient-api
```

=======
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

>>>>>>> c0abe50 (Clean FastAPI project setup)
### 2️⃣ Create virtual environment

```
python -m venv venv
<<<<<<< HEAD
venv\Scripts\activate
```

## 📸 API Preview

![Swagger UI](./assets/swagger.png)
=======
venv\Scripts\activate   (Windows)
```

---
>>>>>>> c0abe50 (Clean FastAPI project setup)

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

<<<<<<< HEAD
### 4️⃣ Configure Database

Update:

```
app/core/database.py
```
=======
---

### 4️⃣ Configure Database

Update your database URL in:

📁 `app/core/database.py`
>>>>>>> c0abe50 (Clean FastAPI project setup)

```
DATABASE_URL = "mysql+pymysql://username:password@localhost/hospital_db"
```

<<<<<<< HEAD
> ⚠️ Replace `@` in password with `%40` if needed
=======
> ⚠️ If your password contains `@`, replace it with `%40`
>>>>>>> c0abe50 (Clean FastAPI project setup)

---

### 5️⃣ Run the server

```
uvicorn app.main:app --reload
```

---

## 📄 API Documentation

<<<<<<< HEAD
Open in browser:
=======
After running the server, open:
>>>>>>> c0abe50 (Clean FastAPI project setup)

```
http://127.0.0.1:8000/docs
```

👉 Interactive Swagger UI for testing APIs

---

<<<<<<< HEAD
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
=======
## 🔑 API Endpoints

### 👨‍⚕️ Doctors

* `POST /doctors/` → Create doctor
* `GET /doctors/` → Get all doctors
* `DELETE /doctors/{id}` → Delete doctor

---

### 🧑 Patients

* `POST /patients/` → Create patient
* `GET /patients/` → Get all active patients
* `DELETE /patients/{id}` → Soft delete patient

---

### 🔗 Assignments

* `POST /assignments/` → Assign patient to doctor
* `GET /assignments/` → Get all assignments
* `GET /assignments/doctor/{id}` → Get patients of a doctor
* `PUT /assignments/discharge/{id}` → Discharge patient

---

## 🧠 Key Concepts Implemented

* 🔄 One-to-Many Relationships (Doctor ↔ Assignments, Patient ↔ Assignments)
* 🧹 Soft Delete (Patient deactivation)
* 🚫 Duplicate Prevention Logic
* 🔗 Automatic JOIN using SQLAlchemy relationships
>>>>>>> c0abe50 (Clean FastAPI project setup)

---

## 🔮 Future Improvements

<<<<<<< HEAD
* 🔐 JWT Authentication
* 🔑 Password Hashing
* 📅 Appointment Scheduling
* 🎨 Frontend UI (React)
* 📊 Admin Dashboard
=======
* 🔐 JWT Authentication (Login system)
* 🔑 Password Hashing
* 🎨 Frontend (React / HTML UI)
* 📊 Dashboard for Doctors & Patients
* 📅 Appointment Scheduling System
>>>>>>> c0abe50 (Clean FastAPI project setup)

---

## 👨‍💻 Author

<<<<<<< HEAD
**Ratnambar Baghel**
=======
**Ratnambar baghel**
>>>>>>> c0abe50 (Clean FastAPI project setup)

---

## ⭐ Support

<<<<<<< HEAD
If you found this useful, give it a ⭐ on GitHub!
=======
If you like this project, give it a ⭐ on GitHub!
>>>>>>> c0abe50 (Clean FastAPI project setup)
