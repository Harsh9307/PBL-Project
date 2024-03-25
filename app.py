# Example web interface (using Flask)
from flask import Flask, request, render_template ,request,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import bcrypt
app = Flask(__name__)
############################################# DATABASE #########################################
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db=SQLAlchemy(app)
app.secret_key='secret_key'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,username):
        self.username = username
        self.email = email
        self.password = bcrypt.haspw(password.encode('utf-8'),bcrypt.getsalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()



############################################# DATABASE #########################################


@app.route('/')
def index():
    return render_template('landing.html')

# @app.route('/user/dashboard/<user_id>')
# def user_dashboard():
#     # Check if user is logged in
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     # Get user ID from session
#     user_id = session['user_id']
#     # Retrieve user's violations based on user ID
#     violations = user_violations.get(user_id, [])
#     # Calculate total number of violations
#     total_violations = len(violations)

#     # Calculate total amount of fines
#     total_fines = sum(violation["fee"] for violation in violations)

#     return render_template('user_dashboard.html', user_id=user_id, violations=violations, total_violations=total_violations, total_fines=total_fines)

@app.route('/police/dashboard')
def police_dashboard():
    return "Police Dashboard - Manage Violations"


@app.route('/upload', methods=['POST'])
def upload():
    # Handle file upload and process image
    return "Image uploaded and processed successfully!"

@app.route('/user/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        

        new_user = User(username=username, email=email, password=password)
        print(new_user.username)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/user/login')
    return render_template("user_login.html")

@app.route('/user/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)

        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            print("User authenticated successfully:", user.username)
            session['username']=user.username
            session['email']=user.email
            session['password']=user.password
            print("Session:", session)
            return redirect('/user/user_dashboard')
        else:
            print("Invalid username or password")
            return render_template("user_login.html",error="Invalid User")

    return render_template("user_login.html")

@app.route('/user/user_dashboard',methods=['GET','POST'])
def user_dashboard():
    print("Session:", session)
    if 'username' in session:
        print("Username in session:", session['username'])
        user = User.query.filter_by(username=session['username']).first()
        return render_template("user_dashboard.html",user=user)
    return redirect('/user/login')

@app.route('/user/profile')
def profile():
    # Handle file upload and process image
    return render_template("user_profile.html")


if __name__ == '__main__':
    app.run(debug=True)
