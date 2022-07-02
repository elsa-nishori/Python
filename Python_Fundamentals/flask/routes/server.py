from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return name * num;

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.', 404

if __name__ == "__main__":
    app.run(debug=True)