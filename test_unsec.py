import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: Hardcoded Secrets (කවදාවත් API keys, Passwords code එකේ ලියන්න හොඳ නෑ)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "supersecretpassword123"

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    
    # Vulnerability 2: SQL Injection (SQLi)
    # User ගෙන් එන input එක කෙලින්ම SQL query එකට pass කරනවා
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}" 
    cursor.execute(query)
    result = cursor.fetchall()
    
    return str(result)

@app.route('/ping')
def ping_server():
    target_ip = request.args.get('ip')
    
    # Vulnerability 3: Command Injection
    # User ගෙන් එන input එක system command එකක් විදියට run කරනවා
    os.system(f"ping -c 1 {target_ip}")
    
    return "Ping executed"

if __name__ == '__main__':
    app.run(debug=True)