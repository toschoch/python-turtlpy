from .common import Model
from .notes import TextNote, Password, Bookmark
import logging

log = logging.getLogger(__name__)


class Space(Model):

    def __init__(self, body, id, color, invites, members, title, user_id):
        self.body = body
        self.id = id
        self.color = color
        self.invites = invites
        self.members = members
        self.title = title
        self.user_id = user_id

    def create_text_note(self, title, text, tags=[], has_file=False, file=None):
        return TextNote(title, text, tags, has_file, file,
                        space_id=self.id, user_id=self.user_id)

    def create_password(self, title, text, username, password, tags=[]):
        return Password(title, text, username, password, tags,
                        space_id=self.id, user_id=self.user_id)

    def create_bookmark(self, title, text, url, tags=[]):
        return Bookmark(title, text, tags, url,
                        space_id=self.id, user_id=self.user_id)

