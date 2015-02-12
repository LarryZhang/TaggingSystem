import os
from flask import Flask
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://218.244.157.158:37017/rest";

app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS



print __name__
if __name__=='__main__':
    app.run(debug=True)
