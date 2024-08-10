from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database/3dlab_db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ? AND user_type = ?', (email, request.form['user_type'])).fetchone()
        conn.close()

        if user and user['password'] == password:
            session['user_id'] = user['id']
            session['user_type'] = user['user_type']
            if user['user_type'] == 'Admin':
                return redirect(url_for('admin_dashboard'))
            elif user['user_type'] == 'Teacher':
                return redirect(url_for('teacher_dashboard'))
            elif user['user_type'] == 'Student':
                return redirect(url_for('student_dashboard'))
        else:
            return "Usuario o contraseña incorrectos"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/admin')
def admin_dashboard():
    if 'user_id' not in session or session['user_type'] != 'Admin':
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

@app.route('/teacher')
def teacher_dashboard():
    if 'user_id' not in session or session['user_type'] != 'Teacher':
        return redirect(url_for('login'))
    return render_template('teacher_dashboard.html')

@app.route('/student')
def student_dashboard():
    if 'user_id' not in session or session['user_type'] != 'Student':
        return redirect(url_for('login'))
    return render_template('student_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
