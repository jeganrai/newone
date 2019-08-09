from flask import Flask,render_template
import requests
import json

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ram/')
def iram():
    return render_template('ram.html')



if __name__ == '__main__':
    app.run()
