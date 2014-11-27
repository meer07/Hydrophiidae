__author__ = '708kaige'
import subprocess
from flask import jsonify

class interpreter:
    def __init__(self):
        pass

    def call_python(self,sorce):
        cmd = ['python', '-c', sorce]
        output = subprocess.check_output(cmd)
        print output
        return jsonify(result=output)