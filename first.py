from flask import Flask, request, render_template
app = Flask(__name__)
'''
@app.route('/')
def hello_world():
    # Return this to the user who visited this page. The browser will render it.
    return 'Hello World!'
'''
'''
@app.route('/tuna', methods = ['GET', 'POST'])
def tuna():
    # Return this to the user who visited this page. The browser will render it.
    if request.methods == 'GET':
        return 'Hello World! using get'
    if request.methods == 'POST':
        return 'Hello World! using post'
'''
'''
@app.route('/<username>')
def hey(username):
    # Return this to the user who visited this page. The browser will render it.
    return 'Hello {}'.format(username)
'''
@app.route('/')
@app.route('/<name>')
def profile(name=None):
    # Return this to the user who visited this page. The browser will render it.
    return render_template('profile.html', name=name)

@app.route('/shopping')
def shopping():
    food = ["abra", "babra", "zabra"]
    return render_template('shopping.html', food=food)

@app.route('/index')
def index():
    user_story = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]
    return render_template('index.html', user_story=user_story)

if __name__ == '__main__':
    app.run()