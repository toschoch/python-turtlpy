import logging

log = logging.getLogger(__name__)


class Space(object):

    def __init__(self, body, id, color, invites, members, title, user_id):
        self.body = body
        self.id = id
        self.color = color
        self.invites = invites
        self.members = members
        self.title = title
        self.user_id = user_id

    def __eq__(self, other):
        return self.title == other

    def __str__(self):
        return self.__dict__.__str__()
