# 🔐 Simple Web Application Firewall (WAF)

A basic Web Application Firewall (WAF) built using Python and Flask to filter, monitor, and block malicious HTTP requests such as SQL Injection, Cross-Site Scripting (XSS), and more. Also includes a visual dashboard for analyzing traffic and attacks.

---

## 📌 Features

- ✅ Filters malicious input using regex patterns
- ✅ Logs both safe and malicious inputs
- ✅ Tracks and logs client IP addresses
- ✅ Blocks harmful requests (HTTP 403)
- ✅ Visual dashboard with:
  - Request statistics
  - Top attacker IPs
  - Common attack patterns
  - Chart of safe vs. blocked traffic

---

## 🛠️ Tech Stack

| Component         | Technology         |
|------------------|--------------------|
| Language          | Python 3           |
| Web Framework     | Flask              |
| Visualization     | Matplotlib         |
| Data Handling     | Pandas             |
| Log Format        | Custom `waf.log`   |

---

## 📁 Folder Structure
├── app.py # Main WAF web application
├── dashboard.py # Dashboard for visualization
├── waf.log # Log file with tracked inputs
├── requirements.txt # Dependencies list
├── templates/
│ └── dashboard.html # HTML for dashboard UI
├── static/
│ └── chart.png # Visualization chart image
└── README.md # Project documentation

---

## 🚀 Getting Started

### 1. Clone the Project

git clone https://github.com/yourusername/simple-waf.git
cd simple-waf

### 2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate on Windows

### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run the WAF Application

python app.py

### 5. Run the Dashboard

python dashboard.py

### View:

Total, safe, and blocked requests

Top IPs

Attack types

Status chart
