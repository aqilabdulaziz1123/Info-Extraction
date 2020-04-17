from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from KMP import knp,solvemany

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/query',methods=['POST'])
@cross_origin()
def pattern_matching():
    datas = request.get_json()
    # print(datas['files')
    files = []
    for file in datas['files']:
        files.append(file)
    key = datas['key']
    hasil = solvemany(files,key)
    # print(datas.files)
    # print(datas)
    # print(datas)
    return jsonify({'data' : hasil}),200
    # return "hai"