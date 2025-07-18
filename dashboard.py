from flask import Flask, render_template
import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

app = Flask(__name__)

# Extract logs
def parse_logs(filepath):
    entries = []
    with open(filepath, 'r') as f:
        for line in f:
            # Match SAFE or BLOCKED log entries
            if "[BLOCKED]" in line or "[SAFE INPUT]" in line:
                match = re.search(r"\[(.*?)\].*?IP: (.*?) \| Param='(.*?)' \| Value='(.*?)'(?: \| Pattern='(.*?)')?", line)
                if match:
                    status = match.group(1)
                    ip = match.group(2)
                    param = match.group(3)
                    value = match.group(4)
                    pattern = match.group(5) if match.group(5) else ''
                    entries.append({
                        'status': status,
                        'ip': ip,
                        'param': param,
                        'value': value,
                        'pattern': pattern
                    })
    return pd.DataFrame(entries)

@app.route('/')
def dashboard():
    df = parse_logs('waf.log')

    if df.empty:
        return "No logs to display yet."

    # Stats
    total = len(df)
    blocked = df[df['status'] == 'BLOCKED']
    safe = df[df['status'] == 'SAFE INPUT']

    top_ips = blocked['ip'].value_counts().head(5)
    top_patterns = blocked['pattern'].value_counts().head(5)

    # Plot
    plt.figure(figsize=(6, 4))
    counts = Counter(df['status'])
    plt.bar(counts.keys(), counts.values(), color=['green', 'red'])
    plt.title("Request Status Overview")
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("dashboard.html",
                           total=total,
                           blocked=len(blocked),
                           safe=len(safe),
                           top_ips=top_ips.to_dict(),
                           top_patterns=top_patterns.to_dict(),
                           chart_url="static/chart.png"
                           )

if __name__ == '__main__':
    app.run(port=5001, debug=True)
