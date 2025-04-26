from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secretkey123'  

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

users = {
    'admin': {
        'password': generate_password_hash('adminpass'),
        'role': 'admin'
    },
    'user1': {
        'password': generate_password_hash('userpass'),
        'role': 'user'
    }
}

class User(UserMixin):
    def __init__(self, id, role):
        self.id = id
        self.role = role

@login_manager.user_loader
def load_user(user_id):

    if user_id in users:
        user_info = users[user_id]
        return User(id=user_id, role=user_info['role'])
    
    return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and check_password_hash(user['password'], password):
            user_obj = User(id=username, role=user['role'])
            login_user(user_obj)
            return redirect(url_for('protected'))

        return render_template('login.html', error="Invalid credentials.")

    return render_template('login.html')

@app.route('/protected')
@login_required

def protected():
    return render_template('protected.html', username=current_user.id, role=current_user.role)

@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
