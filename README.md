# 🏥 Doctor Patient Management API

A backend system built using **FastAPI** and **MySQL** to manage doctors, patients, and their assignments (appointments/relationships).

---

## 🚀 Features

* 👨‍⚕️ Doctor Management (Create, Read, Delete)
* 🧑‍🤝‍🧑 Patient Management (Create, Read, Soft Delete)
* 🔗 Doctor ↔ Patient Assignment System
* ❌ Prevent duplicate assignments
* 🏥 Discharge patients from doctors
* 🗄️ MySQL Database Integration
* 🔄 SQLAlchemy ORM with Relationships
* 📄 Auto API Docs using Swagger UI

---

## 🧠 Tech Stack

* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Language:** Python

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

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Database

Update your database URL in:

📁 `app/core/database.py`

```
DATABASE_URL = "mysql+pymysql://username:password@localhost/hospital_db"
```

> ⚠️ If your password contains `@`, replace it with `%40`

---

### 5️⃣ Run the server

```
uvicorn app.main:app --reload
```

---

## 📄 API Documentation

After running the server, open:

```
http://127.0.0.1:8000/docs
```

👉 Interactive Swagger UI for testing APIs

---

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

---

## 🔮 Future Improvements

* 🔐 JWT Authentication (Login system)
* 🔑 Password Hashing
* 🎨 Frontend (React / HTML UI)
* 📊 Dashboard for Doctors & Patients
* 📅 Appointment Scheduling System

---

## 👨‍💻 Author

**Ratnambar baghel**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
