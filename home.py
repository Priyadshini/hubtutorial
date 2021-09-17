from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Hello !!! \n Welcome to home pagngae"


@app.route('/login')
def login():
    return "<h1>this is login page </h1>"


if __name__ == '__main__':
    app.run(debug = True)
    
