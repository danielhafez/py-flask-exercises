import BasePost
import datetime


class ExtendedPost(BasePost):
    def __init__(self, userId, id, title, body):
        super().__init__(userId, id, title, body)
        date = datetime.datetime.now()
        self.createdAt = date.strftime("%c")

