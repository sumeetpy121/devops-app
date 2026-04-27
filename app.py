from flask import Flask, render_template_string
import random
import os



app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background: #0f172a;
            color: white;
        }

        header {
            background: linear-gradient(135deg, #1e3a8a, #9333ea);
            padding: 40px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 42px;
        }

        header p {
            opacity: 0.8;
            margin-top: 10px;
        }

        .container {
            padding: 30px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        .card {
            background: #1e293b;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card h2 {
            margin: 0;
            font-size: 18px;
            opacity: 0.8;
        }

        .card .value {
            font-size: 32px;
            margin-top: 10px;
            font-weight: bold;
        }

        .status-green { color: #22c55e; }
        .status-yellow { color: #eab308; }
        .status-red { color: #ef4444; }

        .section {
            margin-top: 40px;
        }

        .logs {
            background: #020617;
            padding: 20px;
            border-radius: 12px;
            font-family: monospace;
            font-size: 14px;
            max-height: 200px;
            overflow-y: auto;
        }

        footer {
            text-align: center;
            padding: 20px;
            opacity: 0.6;
            font-size: 14px;
        }
    </style>
</head>

<body>

<header>
    <p>Version: v2</p>
    <h1>🚀 DevOps Control Panel</h1>
    <p>Real-time Infrastructure Monitoring & Deployment Insights</p>
</header>

<div class="container">

    <div class="cards">
        <div class="card">
            <h2>Active Pods</h2>
            <div class="value status-green">{{ pods }}</div>
        </div>

        <div class="card">
            <h2>Running Services</h2>
            <div class="value status-green">{{ services }}</div>
        </div>

        <div class="card">
            <h2>Deployments</h2>
            <div class="value status-yellow">{{ deployments }}</div>
        </div>

        <div class="card">
            <h2>Errors</h2>
            <div class="value status-red">{{ errors }}</div>
        </div>
    </div>

    <div class="section">
        <h2>📊 System Metrics</h2>
        <div class="cards">
            <div class="card">
                <h2>CPU Usage</h2>
                <div class="value">{{ cpu }}%</div>
            </div>

            <div class="card">
                <h2>Memory Usage</h2>
                <div class="value">{{ memory }}%</div>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>📜 Recent Logs</h2>
        <div class="logs">
            <p>[INFO] Deployment successful</p>
            <p>[INFO] Pod scaled to 3 replicas</p>
            <p>[WARN] High memory usage detected</p>
            <p>[ERROR] Service timeout in auth-api</p>
            <p>[INFO] Health checks passing</p>
        </div>
    </div>

</div>

<footer>
    Built with ❤️ for DevOps Engineers | Flask Dashboard
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        pods=random.randint(5, 20),
        services=random.randint(3, 10),
        deployments=random.randint(2, 8),
        errors=random.randint(0, 3),
        cpu=round(os.getloadavg()[0] * 100, 2),
        memory=round(int(open('/proc/meminfo').read().split('MemAvailable:')[1].split()[0]) / 1024, 2),
    )

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)