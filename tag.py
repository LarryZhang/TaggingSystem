__author__ = 'LarryZ'
'''
tag is dict include tag_id,parent_id,description, name,create_time,create_user,update_user,update_time
'''
from bson.objectid import ObjectId
from bson import json_util

from flask.ext.restful import reqparse, abort, Api, Resource, request
from TaggingSystem import  mongo,api,app


class Tags(Resource):
    '''mongo client handler'''
    mongo_tags=None
    tag_tree_dict=[]
    tag_dict={}

    def __init__(self):
        self.mongo_tags=mongo.db.tag
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('label', type = str, required = False,
            help = 'No task label provided', location = 'json')
        self.parser.add_argument('_id')

        #self.gen_tag_tree()
        super(Tags,self).__init__()

    def get(self):
        self.gen_tag_tree()
        print request.args
        return self.tag_tree_dict

    def get_one(self,_id):
        return self.mongo_tags.find_one({'_id':ObjectId(_id)});

    def post(self):
        args = json_util.loads(request.data)
        if args.has_key('_id'):
            return self.put()

        return self.add_tag(args)

    def put(self):
        tag=json_util.loads(request.data)
        if not tag.has_key('_id'):
            return self.post()
        if self.valid(tag) is not None:
            return self.valid(tag)
        if tag.has_key('parent_id') and self.is_ancestor(str(tag['_id']),tag['parent_id']):
            return 'can not set parent to its posterior'
        return self.mongo_tags.save(tag)

    def is_ancestor(self,ancestor,posterior):
        """return if ancestor is the posterior 's ancestor"""
        if ancestor==posterior:
            return True
        child=self.mongo_tags.find_one({'_id':ObjectId(posterior)})
        if child.has_key('parent_id') and child['parent_id']==ancestor :
            return True
        if not child.has_key('parent_id'):
            return False
        else:
            return self.is_ancestor(ancestor,child['parent_id'])

    def delete(self):
        return self.mongo_tags.remove({})
        tag=self.mongo_tags.find_one({'_id':ObjectId(_id)})
        if tag is not None:
            for child in self.mongo_tags.find({'parent_id':_id}):
                self.delete(str(child['_id']))
            self.mongo_tags.remove({'_id':ObjectId(child[_id])})

    def gen_tag_tree(self):
        self.tag_tree_dict=[]
        self.tag_dict={}
        print self.mongo_tags.find().count()
        for tag in self.mongo_tags.find({'parent_id':None}):
            print tag,str(tag['_id']),type(tag['_id'])
            tag['level']=0
            self.add_children(tag,1)
            self.tag_tree_dict.append(tag)
            self.tag_dict[str(tag['_id'])]=tag
        print self.tag_dict

    def get_ancestor(self,_id):
        result=[]
        tag=self.mongo_tags.find_one({'_id':ObjectId(_id)})
        while tag.has_key('parent_id'):
            result.append(tag['parent_id'])
            tag=self.mongo_tags.find_one({'_id':ObjectId(_id)})
        return result

    def add_children(self,tag,level):
        print str(tag['_id'])
        for child_tag in self.mongo_tags.find({'parent_id':str(tag['_id'])}):
            child_tag['level']=level;
            self.add_children(child_tag,level+1)
            if not tag.has_key('children'):
                tag['children']=[]
            tag['children'].append(child_tag)
            self.tag_dict[str(child_tag['_id'])]=child_tag

    def add_tag(self,tag):
        if self.valid(tag) is not None:
            return self.valid(tag)

        _id=self.mongo_tags.insert(tag)

        return tag
    def remove_attri(self,tag):
        if tag.has_key('children'):
            del tag['children']

    def valid(self, tag):

        if not isinstance(tag,dict):
            return 'tag must been tag',400
        if not tag.has_key('label'):
            return 'tag must has name',400
        same_name= self.mongo_tags.find({'label':tag['label']})
        same_name_count=same_name.count()

        if same_name_count == 0 or (same_name_count==1 and tag.has_key('_id') and same_name[0]['_id']==tag['_id']):
            pass
        else:
            return 'tag label not unique',400

        if tag.has_key('parent_id'):
            parent_tag=self.mongo_tags.find_one({'_id':ObjectId(tag['parent_id'])})
            if parent_tag is None:
                return 'parent_id not exist'
        return None

class Tag(Tags):
    def get(self,_id):
        return self.mongo_tags.find_one_or_404({'_id':ObjectId(_id)});
    def delete(self,_id):
        return self.mongo_tags.remove({'_id':ObjectId(_id)})
api.add_resource(Tags,"/api/tag")
api.add_resource(Tag,"/api/tag/<_id>")




if __name__ == '__main__':
    app.run(debug=True)
    #test_mongodb=MongoClient('218.244.157.158',port=37017)['test']
    #tag_handler=Tag(test_mongodb)
#tag=tag_handler.mongo_tags.find_one({'_id':ObjectId('54c606e716f9da121aa96ac8')})
#print tag_handler.add_tag({'name':'test3','parent_id':ObjectId('54c606e716f9da121aa96ac1')})
    import json
#tag_handler.gen_tag_tree()
    #print tag_handler.mongo_tags.find({'parent_id':None}).count()


