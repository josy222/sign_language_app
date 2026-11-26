import os
from flask import Flask, send_from_directory, render_template_string

BASE_DIR = os.path.expanduser("~")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

app = Flask(__name__, static_folder=ASSETS_DIR, static_url_path="/assets")

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sign Language App</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; background: #f7f7f7; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 12px; margin-top: 20px; }
    .card { background: #fff; padding: 8px; border-radius: 8px; text-align: center; box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
    .card img { width: 100%; height: 90px; object-fit: contain; }
  </style>
</head>
<body>
  <h2>Welcome!</h2>
  <p>Enter your name:</p>
  <input id="nameInput" type="text" placeholder="Your name">
  <button onclick="document.getElementById('greet').innerText = 'Hello, ' + document.getElementById('nameInput').value">Submit</button>
  <p id="greet"></p>
  <div class="grid">
    {% for f in files %}
      <div class="card">
        <img src="/assets/{{ f }}" alt="{{ f }}">
        <div>{{ f }}</div>
      </div>
    {% endfor %}
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    files = []
    if os.path.isdir(ASSETS_DIR):
        files = sorted([
            f for f in os.listdir(ASSETS_DIR)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))
        ])
    return render_template_string(HTML, files=files)

@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(ASSETS_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)