from flask import Flask, request, jsonify, redirect, url_for, session

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mySecretKey!'

#@app.route('/', methods=['GET','POST'], defaults={'name':'flask'})
@app.route('/')
def index():
    if 'name' in session:  
        name = session['name']
    else:
        name = "unknown"
    return '<h1> Hello World from {}!</h1>'.format(name)


@app.route('/query')
def query():
    name =request.args.get('name')
    loc = request.args.get('loc')
    return '<h1> you are {} from {}</h1>'.format(name, loc)

@app.route('/home/<name>')
def home(name):
    session['name'] = name
    return '<h1> you are {} from {}</h1>'.format(name,request.args.get('loc'))



@app.route('/theform', methods=['GET','POSt'])
def theform():
    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                  <input type="text" name="name">
                  <input type="text" name="location">
                <input type="submit" value="Enter">
                 </form>'''
    else:
        name=request.form['name']
        location=request.form['location']
        #return '<h1>hello {} you are from {}</h1>'.format(name,location)
        return redirect(url_for('home',name=name,loc=location))

'''
@app.route('/process', methods=['POST'])
def process():
    name=request.form['name']
    location=request.form['location']
    return '<h1>hello {} you are from {}</h1>'.format(name,location)
'''
@app.route('/processjson', methods=['POST'])
def processjson():
    data=request.get_json()
    name = data['name']
    location = data['location']
    randomList = data['randomList']
    return jsonify({'result':'success', 'Name': name, 'Location': location, 'RandomElement': randomList[1]})


if __name__ == '__main__':
    app.run(debug=True)
