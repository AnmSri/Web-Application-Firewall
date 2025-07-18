from flask import Flask, request
import re
import logging

app = Flask(__name__)

# Setup logging to 'waf.log'
logging.basicConfig(filename='waf.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define malicious patterns
malicious_patterns = [
    r"(?i)<script.*?>",             # XSS
    r"(?i)union.*select",           # SQL Injection
    r"(?i)or\s+\d+=\d+",            # SQL logic
    r"(?i)drop\s+table",            # SQL
    r"(?i)alert\s*\(",              # XSS alert
    r"(?i)base64_decode\s*\(",      # Obfuscation
    r"(?i)\.\./",                   # Directory traversal
]

# Check if input matches any malicious pattern
def is_malicious(value):
    for pattern in malicious_patterns:
        if re.search(pattern, value):
            return pattern
    return None

# WAF inspection before each request
@app.before_request
def waf_inspect():
    client_ip = request.remote_addr  # Get client IP

    for param, value in request.values.items():
        pattern = is_malicious(value)
        if pattern:
            log_msg = f"[BLOCKED] IP: {client_ip} | Param='{param}' | Value='{value}' | Pattern='{pattern}'"
            logging.info(log_msg)
            return "403 Forbidden - Request Blocked by WAF", 403

# Main route with form input
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("input")
        client_ip = request.remote_addr

        # Log safe input
        logging.info(f"[SAFE INPUT] IP: {client_ip} | Param='input' | Value='{user_input}'")

        return f"You entered: {user_input}"

    return '''
        <form method="post">
            <label>Input:</label><br>
            <input name="input" type="text" />
            <input type="submit" value="Submit" />
        </form>
    '''

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
