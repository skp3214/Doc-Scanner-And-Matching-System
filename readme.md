
# **📄 Document Scanning & Matching System**

🔍 A self-contained **document scanning and matching system** with a built-in **credit system**. Users can upload documents, scan them for matches, and manage their credits, while admins can view analytics and approve credit requests.  

---

### 🖥️ Project Video
https://github.com/user-attachments/assets/3f877bad-e8f4-4952-9c60-cc52a271f141

## [Documentation](#documentation)
- ### [API Endpoints](#api-endpoints-1)
- ### [View Documentation](#django-views-documentation)
- ### [Models Documentation](#django-models-documentation)

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

--- 
# [Documentation]()

## [API Endpoints]()

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

# [Django Views Documentation]()

This documentation provides an overview of the Django views used in the **Document Scanning and Matching System**. The views handle user authentication, document scanning, credit management, and analytics.

---

### [1. Authentication Views]()

#### **`register`**
- **Purpose**: Handles user registration.
- **Methods**:
  - **GET**: Displays the registration form.
  - **POST**: Processes the form data, creates a new user, and logs them in.
- **Redirects**: To the `home` page after successful registration.
- **Template**: `register.html`

#### **`user_login`**
- **Purpose**: Handles user login.
- **Methods**:
  - **GET**: Displays the login form.
  - **POST**: Authenticates the user and logs them in.
- **Redirects**: To the `home` page (or the `next` URL if provided) after successful login.
- **Template**: `login.html`

#### **`user_logout`**
- **Purpose**: Handles user logout.
- **Methods**:
  - **GET**: Logs out the user.
- **Redirects**: To the `home` page after logout.

---

### [2. Core Views]()

#### **`home`**
- **Purpose**: Displays the home page.
- **Methods**:
  - **GET**: Renders the home page with the logged-in user's username.
- **Template**: `home.html`

#### **`profile`**
- **Purpose**: Displays the user's profile, including their credits, past scans, and credit requests.
- **Methods**:
  - **GET**: Renders the profile page with the user's data.
- **Template**: `profile.html`

#### **`request_credits`**
- **Purpose**: Handles credit requests from users.
- **Methods**:
  - **GET**: Displays the credit request form.
  - **POST**: Processes the form data and creates a new `CreditRequest`.
- **Redirects**: To the `profile` page after submitting the request.
- **Template**: `creditsrequest.html`

#### **`admin_credits`**
- **Purpose**: Allows admins to approve or deny credit requests.
- **Methods**:
  - **GET**: Displays a list of pending credit requests.
  - **POST**: Processes the admin's action (approve/deny) and updates the request status.
- **Redirects**: To the `profile` page if the user is not an admin.
- **Template**: `admincredits.html`

---

### [3. Document Views]()

#### **`scan_document`**
- **Purpose**: Handles document uploads and scans.
- **Methods**:
  - **GET**: Displays the document upload form.
  - **POST**: Processes the uploaded file, extracts its content, and creates a new `Document`.
- **Redirects**: To the `matches` page after successful upload.
- **Template**: `scan.html`

#### **`matches`**
- **Purpose**: Displays documents similar to the uploaded document.
- **Methods**:
  - **GET**: Renders the matches page with the uploaded document and its matches.
- **Template**: `matches.html`

#### **`document_detail`**
- **Purpose**: Displays the content of a specific document.
- **Methods**:
  - **GET**: Renders the document detail page.
- **Template**: `document_detail.html`

#### **`download_scan_history`**
- **Purpose**: Allows users to download their scan history as a text file.
- **Methods**:
  - **GET**: Generates and serves a text file with the user's scan history.
- **Response**: A plain text file with the scan history.

---

### [4. Analytics Views]()

#### **`analytics`**
- **Purpose**: Displays analytics for admins, including scans per user, credit usage, and common topics.
- **Methods**:
  - **GET**: Renders the analytics dashboard.
- **Redirects**: To the `profile` page if the user is not an admin.
- **Template**: `analytics.html`

---

### [5. Utility Functions]()

#### **`reset_credits`**
- **Purpose**: Resets the user's credits at midnight.
- **Usage**: Called in the `profile` view to ensure credits are reset daily.

#### **`find_matches`**
- **Purpose**: Finds documents similar to the uploaded document using basic text matching (e.g., Levenshtein distance).
- **Usage**: Called in the `matches` view.

#### **`ai_find_matches`**
- **Purpose**: Finds documents similar to the uploaded document using AI-powered matching (spaCy).
- **Usage**: Called in the `matches` view.

---

### [6. Example Workflow]()

1. **User Registration**:
   - A new user registers using the `register` view.
   - They are redirected to the `home` page after registration.

2. **User Login**:
   - The user logs in using the `user_login` view.
   - They are redirected to the `home` page (or the `next` URL) after login.

3. **Document Upload**:
   - The user uploads a document using the `scan_document` view.
   - They are redirected to the `matches` page to view similar documents.

4. **Credit Request**:
   - The user requests additional credits using the `request_credits` view.
   - An admin approves or denies the request using the `admin_credits` view.

5. **Analytics**:
   - An admin views analytics using the `analytics` view.

---

### [7. Templates]()

- **`register.html`**: Registration form.
- **`login.html`**: Login form.
- **`home.html`**: Home page.
- **`profile.html`**: User profile page.
- **`creditsrequest.html`**: Credit request form.
- **`admincredits.html`**: Admin credit approval page.
- **`scan.html`**: Document upload form.
- **`matches.html`**: Matches page.
- **`document_detail.html`**: Document detail page.
- **`analytics.html`**: Analytics dashboard.

---

### [8. Dependencies]()

- **spaCy**: Used for AI-powered document matching.
  - Install with: `pip install spacy`
  - Download the English model: `python -m spacy download en_core_web_sm`

---

# [Django Models Documentation]()

## [UserProfile Model]()
Stores additional user-related data, such as credits and the last reset time.

### Fields:
- `user`: One-to-One relationship with Django's built-in `User` model.
- `credits`: Integer field to track the user's available credits (default: 20).
- `last_reset`: DateTime field to store the last time credits were reset (auto-generated on creation).

---

## [Document Model]()
Stores user-uploaded documents and their processed data.

### Fields:
- `user`: ForeignKey relationship with the `User` model (one user can have multiple documents).
- `file`: FileField to store the uploaded document in the `documents/` directory.
- `uploaded_at`: DateTime field to record when the document was uploaded (auto-generated).
- `content`: TextField to store extracted text content from the document.
- `vector`: BinaryField to store the document’s processed vector representation (nullable and optional).

### Methods:
- `save(self, *args, **kwargs)`: Overrides the default save method to:
  - Process document content using SpaCy (`en_core_web_sm`).
  - Convert the processed content into a vector and store it as a binary field.
  - Call the parent class's `save()` method to persist data.

---

## [CreditRequest Model]()
Handles credit requests from users.

### Fields:
- `user`: ForeignKey relationship with the `User` model (one user can make multiple credit requests).
- `requested_credits`: Integer field to store the number of credits requested.
- `status`: CharField to store the request status (`pending` by default, can be updated later).
- `requested_at`: DateTime field to record when the request was made (auto-generated).

---

## Notes
- `spacy` is used for natural language processing, extracting vectors from document content.
- Binary vectors are stored in the `vector` field for future similarity searches.
- Credits help manage document processing, ensuring fair usage.


