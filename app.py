# Example web interface (using Flask)
from flask import Flask, request, render_template ,request,redirect,url_for

app = Flask(__name__)

# Dummy database
USERS = {
    'user1': {'password': 'pass1', 'role': 'user'},
    'police1': {'password': 'pass2', 'role': 'police'}
}
POLICE_DATABASE = {}

@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/police/login')
def police_login():
    return render_template('police_login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = USERS.get(username)
        if user and user['password'] == password:
            if user['role'] == 'user':
                return redirect(url_for('user_dashboard'))
            elif user['role'] == 'police':
                return redirect(url_for('police_dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)
    return render_template('police_login.html')

@app.route('/police/signup', methods=['GET', 'POST'])
def police_signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        badge_number = request.form.get('badge_number')
        
        # Validate the data (you can add more validation as needed)
        if not username or not password or not email or not badge_number:
            return "All fields are required. Please fill out all fields."
        
        if username in POLICE_DATABASE:
            return "Username already exists. Please choose a different username."
        
        # Add the new police officer to the database
        POLICE_DATABASE[username] = {
            'password': password,
            'email': email,
            'badge_number': badge_number
        }
        
        return redirect(url_for('police_login'))  # Redirect to login page after signup
    
    return render_template('police_signup.html')

@app.route('/user/dashboard')
def user_dashboard():
    return "User Dashboard - Pay Challans"

@app.route('/police/dashboard')
def police_dashboard():
    return "Police Dashboard - Manage Violations"


@app.route('/upload', methods=['POST'])
def upload():
    # Handle file upload and process image
    return "Image uploaded and processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
