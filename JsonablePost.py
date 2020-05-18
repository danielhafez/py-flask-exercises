from ExtendedPost import ExtendedPost
import json

class JsonablePost(ExtendedPost):

    def __init__(self, dict_obj):
        super().__init__(dict_obj)

    def format_to_json(self):
        jsonObj = json.dumps(self.__dict__)
        return jsonObj

