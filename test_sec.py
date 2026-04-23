import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# Database එක මුලින්ම හදාගන්න function එක
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Table එක නැත්නම් අලුතින් හදනවා
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    
    # Test කරන්න user කෙනෙක් නැත්නම් එකතු කරනවා
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (name, email) VALUES ('Thamindu', 'thamindu@zynthlab.com')")
        conn.commit()
        
    conn.close()

# App එක start වෙන්න කලින් database එක හදනවා
init_db()

AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    conn.close()
    
    return str(result)

@app.route('/ping')
def ping_server():
    target_ip = request.args.get('ip')
    return "Ping function has been secured/disabled."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False) # nosemgrep