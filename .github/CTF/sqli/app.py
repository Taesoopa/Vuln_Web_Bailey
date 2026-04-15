from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

db = sqlite3.connect(':memory:', check_same_thread=False)
db.execute("CREATE TABLE users (username TEXT, password TEXT)")
db.execute("INSERT INTO users VALUES ('admin', 'Flag{miaaawwww}')")

@app.route('/')
def index():
    return '''
        <form action="/login" method="post">
            Username: <input type="text" name="user"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{password}'"
    result = db.execute(query).fetchone()
    
    if result:
        return f"Lezgoooo ! voici le flag : {result[1]}"
    return "Identifiants incorrects."

if __name__ == '__main__':
    app.run(port=5001) 