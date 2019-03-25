from .common import Model
import logging

log = logging.getLogger(__name__)

class User(Model):

    def __init__(self,
                 username,
                 privkey,
                 pubkey,
                 settings,
                 id,
                 confirmed=False,
                 body=None):

        self.username = username
        self.privkey = privkey
        self.pubkey = pubkey
        self.settings = settings
        self.body = body
        self.id = id
        self.confirmed = confirmed
