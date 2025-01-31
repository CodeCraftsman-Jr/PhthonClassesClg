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

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        return {"message": "Data received", "data": data}
    return {"message": "Send a POST request with JSON data"}

@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return {"message": f"Item {item_id} updated"}

@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return {"message": f"Item {item_id} deleted"}

if __name__ == '__main__':
    app.run(debug=True)
