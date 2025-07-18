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


