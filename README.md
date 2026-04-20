<<<<<<< HEAD
# 🏥 Doctor Patient Management API

A backend system built using **FastAPI** and **MySQL** to manage doctors, patients, and their assignments (appointments/relationships).
=======
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
>>>>>>> b10f97c

---

## 🚀 Features

<<<<<<< HEAD
=======
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
>>>>>>> b10f97c
* 👨‍⚕️ Doctor Management (Create, Read, Delete)
* 🧑‍🤝‍🧑 Patient Management (Create, Read, Soft Delete)
* 🔗 Doctor ↔ Patient Assignment System
* ❌ Prevent duplicate assignments
* 🏥 Discharge patients from doctors
* 🗄️ MySQL Database Integration
* 🔄 SQLAlchemy ORM with Relationships
* 📄 Auto API Docs using Swagger UI
<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

---

## 🧠 Tech Stack

<<<<<<< HEAD
=======
<<<<<<< HEAD
| Layer    | Technology |
| -------- | ---------- |
| Backend  | FastAPI    |
| Database | MySQL      |
| ORM      | SQLAlchemy |
| Language | Python     |
=======
>>>>>>> b10f97c
* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Language:** Python
<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

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
## ⚙️ Setup Instructions
=======
<<<<<<< HEAD
## ⚙️ Installation & Setup
=======
## ⚙️ Setup Instructions
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

### 1️⃣ Clone the repository

```
<<<<<<< HEAD
=======
<<<<<<< HEAD
git clone https://github.com/YOUR_USERNAME/doctor-patient-api.git
cd doctor-patient-api
```

=======
>>>>>>> b10f97c
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c
### 2️⃣ Create virtual environment

```
python -m venv venv
<<<<<<< HEAD
=======
<<<<<<< HEAD
venv\Scripts\activate
```

## 📸 API Preview

![Swagger UI](./assets/swagger.png)
=======
>>>>>>> b10f97c
venv\Scripts\activate   (Windows)
```

---
<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

<<<<<<< HEAD
=======
<<<<<<< HEAD
### 4️⃣ Configure Database

Update:

```
app/core/database.py
```
=======
>>>>>>> b10f97c
---

### 4️⃣ Configure Database

Update your database URL in:

📁 `app/core/database.py`
<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

```
DATABASE_URL = "mysql+pymysql://username:password@localhost/hospital_db"
```

<<<<<<< HEAD
> ⚠️ If your password contains `@`, replace it with `%40`
=======
<<<<<<< HEAD
> ⚠️ Replace `@` in password with `%40` if needed
=======
> ⚠️ If your password contains `@`, replace it with `%40`
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

---

### 5️⃣ Run the server

```
uvicorn app.main:app --reload
```

---

## 📄 API Documentation

<<<<<<< HEAD
After running the server, open:
=======
<<<<<<< HEAD
Open in browser:
=======
After running the server, open:
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

```
http://127.0.0.1:8000/docs
```

👉 Interactive Swagger UI for testing APIs

---

<<<<<<< HEAD
=======
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
>>>>>>> b10f97c
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
<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

---

## 🔮 Future Improvements

<<<<<<< HEAD
=======
<<<<<<< HEAD
* 🔐 JWT Authentication
* 🔑 Password Hashing
* 📅 Appointment Scheduling
* 🎨 Frontend UI (React)
* 📊 Admin Dashboard
=======
>>>>>>> b10f97c
* 🔐 JWT Authentication (Login system)
* 🔑 Password Hashing
* 🎨 Frontend (React / HTML UI)
* 📊 Dashboard for Doctors & Patients
* 📅 Appointment Scheduling System
<<<<<<< HEAD
=======
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

---

## 👨‍💻 Author

<<<<<<< HEAD
**Ratnambar baghel**
=======
<<<<<<< HEAD
**Ratnambar Baghel**
=======
**Ratnambar baghel**
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c

---

## ⭐ Support

<<<<<<< HEAD
If you like this project, give it a ⭐ on GitHub!
=======
<<<<<<< HEAD
If you found this useful, give it a ⭐ on GitHub!
=======
If you like this project, give it a ⭐ on GitHub!
>>>>>>> c0abe50 (Clean FastAPI project setup)
>>>>>>> b10f97c
