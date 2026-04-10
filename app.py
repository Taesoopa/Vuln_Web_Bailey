from flask import Flask, request
import sqlite3
import subprocess
import os

app = Flask(__name__)

# === VULN 1 : Injection SQL ===
@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULNÉRABILITÉ : pas de paramétrage, injection SQL possible
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    return str(results)

# === VULN 2 : Exécution de commande shell ===
@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    # VULNÉRABILITÉ : injection de commande shell
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output.decode()

# === VULN 3 : Path traversal ===
@app.route("/file")
def read_file():
    filename = request.args.get("name", "")
    # VULNÉRABILITÉ : path traversal possible
    with open("/var/www/" + filename, "r") as f:
        return f.read()

# === VULN 4 : Mot de passe en dur (hardcoded secret) ===
SECRET_KEY = "admin1234"
DB_PASSWORD = "superpassword123"

if __name__ == "__main__":
    app.run(debug=True)  # VULN : debug=True en production