from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/hello">Say Hello</a>'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)