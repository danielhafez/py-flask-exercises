from BasePost import BasePost
import datetime


class ExtendedPost(BasePost):
    def __init__(self, post):
        super().__init__(post)
        self.createdAt = datetime.datetime.now().strftime("%c")
