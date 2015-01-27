__author__ = 'LarryZ'
'''
tag is dict include tag_id,parent_id,description, name,create_time,create_user,update_user,update_time
'''
from pymongo import MongoClient
from bson.objectid import ObjectId
import simplejson
from bson import json_util

class Tag_Handler:
    '''mongo client handler'''
    OBJECT_NAME='tag'
    mongo_tags=None
    tag_tree_dict=[]

    def __init__(self,mongodb):
        self.mongo_tags=mongodb[self.OBJECT_NAME]

        self.gen_tag_tree()

    def gen_tag_tree(self):
        temp_dict={}
        for tag in self.mongo_tags.find({'parent_id':None}):
            print tag,str(tag['_id']),type(tag['_id'])
            self.add_children(tag)
            self.tag_tree_dict.append(tag)
        print self.tag_tree_dict

    def add_children(self,tag):
        for child_tag in self.mongo_tags.find({'parent_id':tag['_id']}):
            self.add_children(child_tag)
            if not tag.has_key('children'):
                tag['children']=[]
            tag['children'].append(child_tag)

    def add_tag(self,tag):
        if self.valid(tag) is not None:
            return self.valid(tag)
        _id=self.mongo_tags.insert(tag)
        tag['_id']=_id

        return tag
    def remove_attri(self,tag):
        if tag.has_key('children'):
            del tag['children']

    def valid(self, tag):

        if not isinstance(tag,dict):
            return 'tag must been tag'
        if tag['name'] is None:
            return 'tag must has name'
        same_name= self.mongo_tags.find({'name':tag['name']})
        same_name_count=same_name.count()

        if same_name_count == 0 or (same_name_count==1 and tag.has_key('_id') and same_name[0]['_id']==tag['_id']):
            pass
        else:
            return 'tag name not unique'

        if tag.has_key('parent_id'):
            parent_tag=self.mongo_tags.find_one({'_id':tag['parent_id']})
            if parent_tag is None:
                return 'parent_id not exist'
        return None


if __name__ == '__main__':

    test_mongodb=MongoClient('218.244.157.158',port=37017)['test']
    tag_handler=Tag_Handler(test_mongodb)
#tag=tag_handler.mongo_tags.find_one({'_id':ObjectId('54c606e716f9da121aa96ac8')})
#print tag_handler.add_tag({'name':'test3','parent_id':ObjectId('54c606e716f9da121aa96ac1')})
    import json
#tag_handler.gen_tag_tree()
    print tag_handler.mongo_tags.find({'parent_id':None}).count()


