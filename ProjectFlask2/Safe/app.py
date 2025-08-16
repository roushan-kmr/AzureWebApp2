from flask import Flask

app = Flask(__name__)

data = {
    1:{"task":"Learn Python", "done":False},
    2:{"task":"Learn API", "done":False}
}


@app.route('/')
def index():
    return "Hellow World"

@app.route('/todos', methods=["get"])
def get_todos():
    response = data
    return response

if __name__ == "__main__":
    app.run(debug=True)
    
