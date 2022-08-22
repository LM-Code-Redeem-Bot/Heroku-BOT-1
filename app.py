from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def database():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
