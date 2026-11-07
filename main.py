from flask import Flask, jsonify, render_template_string
from datetime import datetime, timezone

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HuyMeow Cloud App</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f6f4;
            color: #26352d;
        }

        header {
            background: #263d30;
            color: white;
            padding: 25px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            color: #a8e6a3;
        }

        main {
            max-width: 850px;
            margin: 45px auto;
            padding: 25px;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.07);
            margin-bottom: 20px;
        }

        .status {
            color: #18864b;
            font-weight: bold;
        }

        .info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
        }

        .info div {
            background: #eef7ef;
            padding: 18px;
            border-radius: 10px;
        }

        footer {
            text-align: center;
            padding: 20px;
            color: #68756d;
        }
    </style>
</head>
<body>
    <header>
        <h1>HuyMeow Cloud App</h1>
        <p>Ứng dụng Python Flask trên nền tảng đám mây</p>
    </header>

    <main>
        <section class="card">
            <h2>Xin chào!</h2>
            <p>
                Chào mừng bạn đến với HuyMeow Cloud App.
                Đây là ứng dụng web được xây dựng bằng Python
                và Flask, triển khai trên nền tảng Render.
            </p>
            <p>Trạng thái hệ thống:
                <span class="status">Đang hoạt động</span>
            </p>
        </section>

        <section class="card">
            <h2>Thông tin ứng dụng</h2>
            <div class="info">
                <div>
                    <strong>Ngôn ngữ</strong>
                    <p>Python</p>
                </div>
                <div>
                    <strong>Framework</strong>
                    <p>Flask</p>
                </div>
                <div>
                    <strong>Mô hình</strong>
                    <p>PaaS</p>
                </div>
                <div>
                    <strong>Nền tảng</strong>
                    <p>Render</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        Cloud Computing Lab - HuyMeow
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "HuyMeow Cloud App",
        "framework": "Flask",
        "platform": "Render",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)