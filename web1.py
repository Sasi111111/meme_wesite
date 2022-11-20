from flask import Flask
import requests
app = Flask(__name__)
@app.route('/')
def function():
    return "this is new website"


if __name__ == '__main__' :
    app.run()