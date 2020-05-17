class BasePost():
    def __init__(self, post):
        self.userId = post.get("userId")
        self.id = post.get("id")
        self.title = post.get("title")
        self.body = post.get("body")



