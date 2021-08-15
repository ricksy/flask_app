from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET','POST'], defaults={'name':'flask'})
@app.route('/<name>', methods=['GET','POST'])
def index(name):
    return '<h1> Hello World from {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run()
