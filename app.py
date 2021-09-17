from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/stock', methods = ['POST'])
def save_info():
    infos = list(db.codes.find({},{'_id':False}))

	return jsonify({'infos':infos})


@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({},{'_id':False}))

    return jsonify({'all_articles':articles})





if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)