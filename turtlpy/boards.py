import logging

log = logging.getLogger(__name__)


class Board(object):

    def __init__(self, body, id, keys, space_id, title, user_id):
        self.body = body
        self.id = id
        self.keys = keys
        self.space_id = space_id
        self.title = title
        self.user_id = user_id

    def __eq__(self, other):
        return self.title == other
