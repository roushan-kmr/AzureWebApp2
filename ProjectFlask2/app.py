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
    response = []
    for key, value in data.items():
        temp = value
        temp["id"] = key
        response.append(temp)
    return response

@app.route('/todos/<int:id>',methods=["get"])
def get_todo(id):
    if id in data:
        temp = data[id]
        temp["id"] = id
        return temp
    else:
        return {
            "error":"id does not exist"
        }, 404


    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
