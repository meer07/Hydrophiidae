__author__ = '708kaige'
# coding:utf-8

from flask import Flask, render_template,request
from interpreter import interpreter
from download_script import download_script
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

@app.route('/download',methods=['POST'])
def download_file():
    script_text = request.form['script']
    file_name = request.form['file_name']
    return download_script.make_file(script_text,file_name)

if __name__ == '__main__':
    app.run()