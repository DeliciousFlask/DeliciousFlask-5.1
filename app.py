from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render-curly-braces')
def render_curly_braces():
    return render_template('curly_braces.html')

@app.route('/render-variable')
def render_variable():
    return render_template('render_variable.html', message='I am a rendered variable!')

@app.route('/render-loop')
def render_loop():
    return render_template('render_loop.html')

@app.route('/render-list')
def render_list():
    return render_template('render_list.html', fruits=['apple', 'orange', 'pear'])

@app.route('/render-template-var')
def render_template_var():
    return render_template('render_template_var.html')

@app.route('/render-if')
def render_if():
    return render_template('render_if.html')

if __name__ == '__main__':
    app.run(debug=True)

