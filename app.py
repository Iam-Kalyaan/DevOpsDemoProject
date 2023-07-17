from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi all, this is the Complete CI-CD Demo'
