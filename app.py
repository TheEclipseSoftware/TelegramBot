from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the homepage."""
    return "Welcome to the Flask App!"

@app.route('/check')
def check_status():
    """Provides a simple status check endpoint."""
    return "Flask app is running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
