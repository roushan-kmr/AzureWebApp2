from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["get"])
def hello_world():
    return render_template('index.html')
    #return "<p>Hello, World!</p>"

@app.route('/products', methods=["get"])
def products():
    return '<h2>this is products page</h2>'

if __name__ == "__main__":
    app.run(debug=True, port=80)