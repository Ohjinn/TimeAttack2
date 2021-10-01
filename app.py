from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import time

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    print('clicked')
    idx = request.form['idx']
    title = request.form['title_give']
    comment = request.form['comment_give']
    nowTime = time.strftime('%Y.%m.%d %X')
    doc = {
        'idx' : idx,
        'title' : title,
        'comment' : comment,
        'reg_date' : nowTime
    }
    db.posts.insert_one(doc)
    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    posts = list(db.posts.find({}, {'_id' : False}))
    return jsonify({'all_posts' : posts})


@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)