__author__ = '708kaige'
# coding:utf-8

from flask import Flask, render_template,request,make_response
from interpreter import interpreter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/run', methods=['POST'])
def run_python_code():
    script_text = request.form['script']
    inter_preter = interpreter()
    result = inter_preter.call_python(script_text)
    return result

@app.route('/download', methods=['POST'])
def download_file():
    script_text = request.form['script']
    file_name = request.form['file_name'] + '.py'

    make_file(file_name, script_text)
    python_file = read_file(file_name)

    response = make_response(python_file)
    response.headers["Content-type"] = 'application/force-download'
    response.headers['Content-Disposition'] = "attachment; filename=" + file_name

    return response

def make_file(file_name, sorce):
    f = open(file_name, 'w')
    f.write(sorce)
    f.close()

def read_file(file_name):
    f = open(file_name, 'r')
    r = f.read()
    f.close()
    return r

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['DEBUG'] = True