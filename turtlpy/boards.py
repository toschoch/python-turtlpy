import logging
from .common import Model
from .notes import TextNote, Bookmark, Password

log = logging.getLogger(__name__)


class Board(Model):

    def __init__(self, body, id, keys, space_id, title, user_id):
        self.body = body
        self.id = id
        self.keys = keys
        self.space_id = space_id
        self.title = title
        self.user_id = user_id

    def create_text_note(self, title, text, tags=[], has_file=False, file=None):
        return TextNote(title=title, text=text, tags=tags, has_file=has_file, file=file,
                        space_id=self.space_id, user_id=self.user_id, board_id=self.id)

    def create_password(self, title, text, username, password, tags=[]):
        return Password(title=title, text=text, username=username, password=password, tags=tags,
                        space_id=self.space_id, user_id=self.user_id, board_id=self.id)

    def create_bookmark(self, title, text, url, tags=[]):
        return Bookmark(title=title, text=text, tags=tags, url=url,
                        space_id=self.space_id, user_id=self.user_id, board_id=self.id)

