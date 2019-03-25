from .common import Model
import logging

log = logging.getLogger(__name__)


class Note(Model):

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
                 mod=None,
                 user=None, user_id=None,
                 space=None, space_id=None,
                 board=None, board_id=None):

        assert space_id is not None or space is not None
        assert user_id is not None or user is not None

        if space is not None:
            self.space_id = space.id
        else:
            self.space_id = space_id

        if board is not None:
            self.board_id = board.id
        else:
            self.board_id = board_id

        if user is not None:
            self.user_id = str(user.id)
        else:
            self.user_id = str(user_id)

        self.title = title
        self.text = text
        self.tags = tags
        self.type = type

        self.has_file = has_file
        self.file = file

        self.username = username
        self.password = password

        self.url = url

        self.body = body
        self.id = id
        self.keys = keys
        self.mod = mod

    @staticmethod
    def from_dict(d):
        if d['type'] == 'text':
            return TextNote(**d)
        elif d['type'] == 'password':
            return Password(**d)
        elif d['type'] == 'bookmark':
            return Bookmark(**d)
        else:
            return Note(**d)

class TextNote(Note):

    def __init__(self,
                 title,
                 text,
                 tags=[],
                 has_file=False,
                 file=None,
                 user=None, user_id=None,
                 space=None, space_id=None,
                 board=None, board_id=None, **kwargs):
        super(TextNote, self).__init__(title=title, text=text,
                                       type=kwargs.pop("type","text"),
                                       tags=tags,
                                       has_file=has_file, file=file,
                                       user=user, user_id=user_id,
                                       space=space, space_id=space_id,
                                       board=board, board_id=board_id, **kwargs)

class Bookmark(Note):

    def __init__(self,
                 title,
                 text,
                 url,
                 tags=[],
                 user=None, user_id=None,
                 space=None, space_id=None,
                 board=None, board_id=None, **kwargs):
        super(Bookmark, self).__init__(title=title, text=text,
                                       type=kwargs.pop("type","link"),
                                       tags=tags, url=url,
                                       user=user, user_id=user_id,
                                       space=space, space_id=space_id,
                                       board=board, board_id=board_id, **kwargs)

class Password(Note):

    def __init__(self,
                 title,
                 text,
                 username=None,
                 password=None,
                 tags=[],
                 user=None, user_id=None,
                 space=None, space_id=None,
                 board=None, board_id=None, **kwargs):
        super(Password, self).__init__(title=title, text=text, username=username, password=password,
                                       type=kwargs.pop("type","password"),
                                       tags=tags,
                                       user=user, user_id=user_id,
                                       space=space, space_id=space_id,
                                       board=board, board_id=board_id, **kwargs)


