__author__ = 'naoya-kaige'
from flask import send_file

class download_script:

    @classmethod
    def make_file(self,sorce,file_name):
        file = open(file_name+'.py','w')
        file.write(sorce)
        file.close()
        return send_file(file_name,mimetype='text/x-python')