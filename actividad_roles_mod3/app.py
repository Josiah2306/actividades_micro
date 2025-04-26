from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, AnonymousIdentity, identity_changed, identity_loaded

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Setup Login Manager
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Setup Flask-Principal
principals = Principal(app)

# Define Roles
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Modelo de usuario
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

# Datos de ejemplo
users = {
    "juan": User(1, "juan", "admin"),
    "maria": User(2, "maria", "user")
}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if str(user.id) == user_id:
            return user
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if hasattr(current_user, 'id'):
        identity.user = current_user
        if current_user.role == 'admin':
            identity.provides.add(RoleNeed('admin'))
        if current_user.role == 'user':
            identity.provides.add(RoleNeed('user'))

@app.route("/login/<username>")
def login(username):
    user = users.get(username)
    if user:
        login_user(user)
        identity_changed.send(app, identity=Identity(user.id))
        return redirect(url_for('dashboard'))
    return "Usuario no encontrado", 404

@app.route("/logout")
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('login_page'))

@app.route("/")
def login_page():
    return render_template('login.html')

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route("/admin")
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return render_template('admin.html', user=current_user)

@app.route("/user")
@login_required
@user_permission.require(http_exception=403)
def user_page():
    return render_template('user.html', user=current_user)

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True)