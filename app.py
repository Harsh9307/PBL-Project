
from flask import Flask, render_template




# Create flask app
app = Flask(__name__)

# Add app routes
@app.route('/')

# Create server response
def index():
    return "Hi"

@app.route('/app')

def application():
    return render_template('layout.html')



if __name__ == "__main__":
    app.run()