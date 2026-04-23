import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# Fix 1: Environment Variables භාවිතය (Secrets code එකෙන් අයින් කරලා තියෙන්නේ)
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    
    # Fix 2: Parameterized Queries භාවිතය (SQL Injection එක වලක්වා ඇත)
    # මෙතනදී '?' පාවිච්චි කරලා වෙනම data pass කරන නිසා attacker කෙනෙක්ට query එක වෙනස් කරන්න බෑ
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    
    return str(result)

@app.route('/ping')
def ping_server():
    target_ip = request.args.get('ip')
    
    # Fix 3: System commands වෙනුවට ආරක්ෂිත ක්‍රම භාවිතා කිරීම හෝ input validation කිරීම
    # මෙතනදී අපි සරලවම ඒ function එක disable කරලා තියෙනවා
    return "Ping function has been secured/disabled."

if __name__ == '__main__':
    # Production වලදී කවදාවත් debug=True දෙන්නේ නෑ
    app.run(debug=False)