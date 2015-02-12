__author__ = 'LarryZ'
from flask.ext.restful import Resource, request
from bson import ObjectId,json_util

from TaggingSystem import  mongo,api,app


class Item(Resource):
    items_mongo=None
    def __init__(self):
        self.items_mongo=mongo.db.items

    def get(self,_id):
        return self.items_mongo.find_one_or_404({'_id':ObjectId(_id)})


    def delete(self,_id):
        return self.items_mongo.remove({'_id':ObjectId(_id)})

    def valid(self,item):
        if not isinstance(item,dict):
            return 'tag must been tag',400
        if not item.has_key('label'):
            return 'tag must has name',400
        same_name= self.items_mongo.find({'label':item['label']})
        same_name_count=same_name.count()
        if same_name_count == 0 or (same_name_count==1 and item.has_key('_id') and same_name[0]['_id']==item['_id']):
            pass
        else:
            return 'item label not unique',400
        return None


class Items(Item):
    def get(self):
        return self.items_mongo.find({})

    def post(self):
        item= json_util.loads(request.data)
        if  item.has_key('_id'):
            return self.put()
        if self.valid(item) is not None:
            return self.valid(item)
        return self.items_mongo.insert(item)

    def put(self):

        item= json_util.loads(request.data)

        if self.valid(item) is not None:
            return self.valid(item)

        return self.items_mongo.save(item)

    def delete(self):
        return mongo.db.items.remove({})

api.add_resource(Items,"/api/item")
api.add_resource(Item,"/api/item/<_id>")
import uuid

image_mimetypes_suffix_map={
    "image/jpeg":'jpg',
    'image/gif':'gif',
    'image/png':'png'
}


def save_file(request_file):
    if request_file.mimetype not in image_mimetypes_suffix_map.keys():
        return 'not support type {}'.format(request_file.mimetype ),400
    file_name=str(uuid.uuid1())+'.'+image_mimetypes_suffix_map[request_file.mimetype]
    mongo.save_file(file_name, request_file)

    return file_name,200;

import json
@app.route('/api/uploads', methods=['POST'])
def upload_image():
    result=[]
    for request_file_name in request.files:
        file_name,status=save_file(request.files[request_file_name])
        if status==200:
            result.append({'filename':request.files[request_file_name].filename,
                           'location':file_name})

        else:
            return json.dumps({'code':status,'message':file_name}),400;

    return json.dumps(result);


@app.route('/api/uploads/<path:filename>')
def get_upload(filename):
    return mongo.send_file(filename)

if __name__=='__main__':
    app.run(debug=True)
