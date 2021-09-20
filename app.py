from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/stock', methods = ['POST'])
def save_info():
    infos = list(db.codes.find({},{'_id':False}))


#group 값들을 가져오는 함수
@app.route('/stock', methods=['GET'])
def listing():
    info = db.codes.distinct("group")
    return jsonify({'info' : info})


@app.route('/markets', methods=['GET'])
def lists():
    info_receive = request.args.get('info_give')
    markets = list(db.codes.find({'group': info_receive},{'_id':False}))
    return jsonify(markets)



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)