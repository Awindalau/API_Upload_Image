# 6C/19090023/Muchammad Nachirul Ichsan
# 6C/19090063/Arwinda Laurisma

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

#curl -X POST -F file=@"/home/san/Documents/Web Services/upload/test.txt" http://localhost:4063/api/upload
@app.route("/api/upload", methods=['POST','PUT'])
def upload():
    file = request.files['file']
    filename=secure_filename(file.filename)   
    return jsonify({
    'msg': 'File Berhasil Ditambahkan',
    'file': filename,
    })

if __name__=="__main__":
    app.run(port=4063, debug=True)