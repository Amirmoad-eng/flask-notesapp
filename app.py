from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'کیرم تو اکیپی که توش صدره'

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run()