from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def check_login(username, password):
    conn = sqlite3.connect('école1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    print(f"User found: {user}")
    return user is not None


@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if check_login(username, password):
        return render_template('Nav.html', username=username)
    else:
        return "Nom d'utilisateur ou mot de passe incorrect."

if __name__ == '__main__':
    app.run(debug=True)
