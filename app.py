from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Docker!"

if __name__ == "__main__":
    # Host 0.0.0.0 makes the app accessible from outside the container
    app.run(host='0.0.0.0', port=5000)
