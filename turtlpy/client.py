import logging
import time, shutil, os

from . import commands as cmd
from .users import User
from .boards import Board
from .spaces import Space
from .notes import Note

log = logging.getLogger(__name__)


class TurtlClient(object):

    def __init__(self, server, username, pw, server_v2=None, clear_local=False):

        if clear_local:
            log.info("clear local data...")
            shutil.rmtree(os.path.expanduser('~/.config/turtlpy'))

        success = cmd.start(server, server_v2)
        assert success
        log.info("turtl core started...")

        success, resp_login = cmd.login(username, pw)
        assert success
        log.info("user logged in...")

        log.info("start sync...")
        success, resp_sync_start = cmd.sync_start()
        assert success

        success, resp_sync_status = cmd.sync_status()
        assert success and resp_sync_status['d']

        log.info("load user profile...")
        success, resp_profile_load = cmd.profile_load()
        assert success

        self.user = User(**resp_profile_load['d']['user'])
        self.boards={b.title:b for b in map(lambda e: Board(**e), resp_profile_load['d']['boards'])}
        self.spaces={s.title:s for s in map(lambda e: Space(**e), resp_profile_load['d']['spaces'])}

    def get_board(self, key) -> Board:
        return self.boards[key]

    def get_space(self, key) -> Space:
        return self.spaces[key]


    def find_notes(self, query={}, space_name=None):
        if space_name is None:
            query['space_id'] = self.user.settings['default_space']
        else:
            query['space_id'] = self.get_space(space_name).id
        success, resp_find = cmd.profile_find_notes(query)

        if not success:
            msg = "{}".format(resp_find['d'])
            log.error(msg)
            raise Exception(msg)

        #return resp_find['d']['notes']
        return list(map(Note.from_dict, resp_find['d']['notes']))


    @staticmethod
    def logout():
        log.info("get pending tasks...")
        success, resp_sync_pending = cmd.sync_get_pending()
        assert success

        while len(resp_sync_pending['d']) > 0:
            log.info("pending tasks ({})".format(len(resp_sync_pending['d'])))
            time.sleep(1)
            success, resp_sync_pending = cmd.sync_get_pending()

        log.info("shutdown sync...")
        success, resp_sync_stop = cmd.sync_stop()
        assert success

        log.info("logout...")
        success, resp_logout = cmd.logout()
        assert success

        log.info("shutdown core...")
        success = cmd.stop()
        assert success

    @staticmethod
    def add_note(note: Note):
        log.info("add new note '{}'...".format(note.title))
        log.debug("{}".format(note.to_dict()))
        success, resp_profile_sync_model = cmd.profile_sync_model("add", "note", note.to_dict())
        if not success:
            msg = "{}".format(resp_profile_sync_model['d'])
            log.error(msg)
            raise Exception(msg)
        return Note.from_dict(resp_profile_sync_model['d'])


    @staticmethod
    def delete_note(note: Note):
        log.info("delete note '{}'... ({})".format(note.title, note.id))
        success, resp_profile_sync_model = cmd.profile_sync_model("delete", "note", {'id':note.id})
        if not success:
            msg = "{}".format(resp_profile_sync_model['d'])
            log.error(msg)
            raise Exception(msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logout()