# 🔐 Simple Web Application Firewall (WAF)

I built this Simple Web Application Firewall (WAF) to explore how security tools help detect and block malicious inputs in web applications.

This WAF is a lightweight Python + Flask project that monitors incoming HTTP requests, matches them against common attack patterns (like XSS, SQL injection, directory traversal, command injection, and XXE), and blocks them in real time. It also logs each request with the client's IP address and visualizes the blocked attack types using a dashboard.

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

## 🛠️ Tools Used

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
 └── dashboard.html # HTML for dashboard UI

├── static/
 └── chart.png # Visualization chart image

└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the Project

git clone https://github.com/AnmSri/Web-Application-Firewall

cd Web-Application-Firewall

### 2. Create a Virtual Environment

python -m venv venv

venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run the WAF Application

python app.py

After running the command, open http://127.0.0.1:5000/ in the browser.

### 5. Run the Dashboard

python dashboard.py

After running the command, open http://127.0.0.1:5001/ in the browser.

### View:

- Total, safe, and blocked requests

- Top IPs

- Attack types

- Status chart

# 🔒 Web Application Firewall – Test Inputs

This table lists example malicious payloads to test the detection and blocking behavior of the Simple Web Application Firewall.

---

## 💡 Common Web Attack Inputs

| Attack Type | Input Example |
|-------------|----------------|
| **XSS**     | `<script>alert(1)</script>` |
| **SQL Injection** | `1 UNION SELECT password` |
| **SQL Logic Bypass** | `' OR 1=1 --` |
| **Directory Traversal** | `../../etc/passwd` |
| **Command injection** | `; rm -rf /` |
| **XML External Entity** | `<?xml version="1.0"?> <!DOCTYPE foo [<!ELEMENT foo ANY > <!ENTITY xxe SYSTEM "file:///C:/Windows/system.ini" >]> <foo>&xxe;</foo>` |
| **Encoded payloads** | `%3Cscript%3E` |

---

## ✅ How to Test

You can enter these payloads into the form on the app's front end. The WAF should:

- 🚫 Block malicious inputs (403)
- ✅ Allow safe inputs (200) [In logs]

---



