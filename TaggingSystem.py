from flask import Flask
from Tag_handler import Tag_Handler
app = Flask(__name__)
from pymongo import MongoClient

test_mongodb=MongoClient('218.244.157.158',port=37017)['test']
tag_handler=Tag_Handler(test_mongodb)
from bson.json_util import dumps

@app.route('/')
def hello_world():

    return dumps(tag_handler.tag_tree_dict)


if __name__ == '__main__':
    app.run()

