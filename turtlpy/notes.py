

import logging

log = logging.getLogger(__name__)


class Note(object):

    def __init__(self,
                 title,
                 text,
                 type,
                 tags=[],
                 has_file=False,
                 file=None,
                 username=None,
                 password=None,
                 url=None,
                 body=None,
                 id=None,
                 keys=None,
                 user=None, user_id=None,
                 space=None, space_id=None,
                 board=None, board_id=None):

        assert space_id is not None or board_id is not None

        if space is not None:
            self.space_id = space.id
        else:
            self.space_id = space_id

        if board is not None:
            self.board_id = board.id
        else:
            self.board_id = board_id

        if user is not None:
            self.user_id = user.id
        else:
            self.user_id = user_id

        self.title = title
        self.text = text
        self.tags = tags
        self.type = type

        self.has_file = has_file,
        self.file = file

        self.username = username
        self.password = password

        self.url = url

        self.body = body
        self.id = id
        self.keys = keys

    def __eq__(self, other):
        return self.title == other

    def __str__(self):
        return {k:v for k,v in self.__dict__.items() if v is not None}.__str__()
