from flask import Flask

app = Flask(__main__)

@app.route('/')
def home_page():
    return "Hello !!!"

if __name__ == '__main__':
    app.run(debug = True)
    