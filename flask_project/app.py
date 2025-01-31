from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"
@app.route('/vasanth')
def vasanth():
    return f"route node arrived"

@app.route('/hell/<vasanth>')
def hell(vasanth):
    return f"Welcome home, {vasanth}!"

if __name__ == '__main__':
    app.run(debug=True)