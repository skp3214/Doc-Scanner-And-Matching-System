
# **📄 Document Scanning & Matching System**

🔍 A self-contained **document scanning and matching system** with a built-in **credit system**. Users can upload documents, scan them for matches, and manage their credits, while admins can view analytics and approve credit requests.  

---

### 🖥️ Project Video
https://github.com/user-attachments/assets/3f877bad-e8f4-4952-9c60-cc52a271f141

## ✨ Features

### 🔑 **User Management**
✅ User **registration & login**  
✅ User **roles**: Regular Users & Admins  
✅ Profile section with **credits, past scans, and credit requests**  

### 💰 **Credit System**
🎟️ Users get **20 free scans per day** (auto-reset at **midnight** 🕛)  
➕ Users can **request additional credits**, which admins can **approve/deny**  
📄 Each **document scan deducts 1 credit**  

### 📄 **Document Scanning & Matching**
📂 Upload **plain text, PDF, or Word documents**  
🧠 Scanning methods:  
   - **Basic Text Matching** (Levenshtein distance)  
   - **AI-powered Matching** (spaCy for semantic similarity)  
📊 Displays **matching documents with percentage similarity**  

### 📊 **Smart Analytics Dashboard (Admin Only)**
📌 Track **number of scans per user**  
📌 Identify **most common scanned document topics**  
📌 View **top users by scans & credit usage**  
📌 Generate **credit usage statistics**  

### 🔒 **Security**
🔐 Secure **user authentication with hashed passwords**  
🚫 **Admin-only access** to sensitive features (e.g., analytics, credit approval)  

---

## 🛠️ Tech Stack

- **🌐 Frontend**: HTML, CSS, JavaScript  
- **🖥️ Backend**: Django (Python)  
- **📦 Database**: SQLite (for development)  
- **📁 File Storage**: Local storage for uploaded documents  
- **🧠 AI Matching**: spaCy for semantic similarity  

---

## 🚀 Setup Instructions  

### **🔗 Prerequisites**
1️⃣ **Python 3.8+** installed on your system  
2️⃣ **pip** (Python package manager)  

### **⚙️ Installation**  

📥 **Clone the Repository**  
```bash
git clone https://github.com/skp3214/document-scanning-and-matching-system.git
cd document-scanning-and-matching-system
```

🛠️ **Create a Virtual Environment**  
```bash
python -m venv venv
venv\Scripts\activate
```
📥 **Move to Project Directory**
```bash
cd Doc_Scanner_Matcher
```
📦 **Install Dependencies**  
```bash
pip install -r requirements.txt
```

🗄️ **Set Up the Database**  
```bash
python manage.py migrate
```

🔑 **Create an Admin User**  
```bash
python manage.py createsuperuser
```

▶️ **Run the Development Server**  
```bash
python manage.py runserver
```

🌍 **Access the App**: Open **`http://127.0.0.1:8000/`** in your browser  

---

## 🌐 API Endpoints

| **Endpoint**                 | **URL Path**                   | **View Function**          | **Description**                                      |
|------------------------------|--------------------------------|----------------------------|------------------------------------------------------|
| **User Registration**        | `auth/register/`               | `register`                 | Registers a new user.                               |
| **User Login**               | `auth/login/`                  | `user_login`               | Logs in a user.                                    |
| **Home Page**                | `/`                            | `home`                     | Displays the homepage.                             |
| **User Profile**             | `user/profile/`                | `profile`                  | Shows user profile.                    |
| **Request Credits**          | `credits/request/`             | `request_credits`          | Allows users to request additional credits.       |
| **Admin Credit Management**  | `credits/admins/`              | `admin_credits`            | Admins manage credit requests.                     |
| **Scan Document**            | `scan/`                        | `scan_document`            | Upload and scan a document for matches.           |
| **View Matches**             | `matches/<int:doc_id>/`        | `matches`                  | Displays matching documents.                      |
| **Document Details**         | `document/<int:doc_id>/`       | `document_detail`          | Shows details of a scanned document.              |
| **Download Scan History**    | `download-scan-history/`       | `download_scan_history`    | Downloads user's scan history.                    |
| **Admin Analytics**          | `admins/analytics/`            | `analytics`                | Admin dashboard with scan and credit statistics.  |
| **User Logout**              | `logout/`                      | `user_logout`              | Logs out the user.                                |

---

## 🎯 Usage  

### **👤 User Features**  
1️⃣ **Register & Log In** 📝  
2️⃣ **Upload & Scan Documents** 📂  
3️⃣ **Check Profile** (Credits, Past Scans, Requests) 👤  
4️⃣ **Request More Credits** ➕  

### **🛠️ Admin Features**  
1️⃣ **Approve/Deny Credit Requests** ✔️❌  
2️⃣ **View Analytics Dashboard** 📊  

---

## 📬 Contact  

For questions or feedback, reach out:  

📧 **Email**: spsm1818@gmail.com  
🐙 **GitHub**: [skp3214](https://github.com/skp3214)  

---

### 🚀 **Happy Coding!** 😊