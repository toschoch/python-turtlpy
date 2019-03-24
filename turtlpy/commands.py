import turtlpy.core as core
import json
import logging
import os

log = logging.getLogger(__name__)


def _send_command(msg_id, cmd, *args):
    r = core.send(bytes(json.dumps([msg_id, cmd] + list(args)),'utf-8'))
    log.debug("send command '{}'... ({})".format(cmd, r))
    return r


def _check_command_answer(r, id):
    if r != 0: return False, {}
    r2 = core.recv(True)
    log.debug("command returned: {}".format(r2))
    return (r2['id'] == id and r2['e'] == 0), r2


def start(server, server_v2=None):

    if server_v2 is not None:
        server_v2 = "{}/v2".format(server.rstrip("/"))

    config = {
        'api': {
            'endpoint': server,

            'v6': {
                'endpoint': server_v2
            }
        },
        'data_folder': os.path.expanduser("~/.config/turtlpy")
    }


    if not ping_pong():
        log.info("trying to start turtl core...")
        core.start(config)
        r = core.recv_event(True)
        log.debug("received event {}".format(r))
        return 'e' in r and ['e'] == "messaging:ready"
    else:
        log.info("turtl core is already running...")
        return 0


def login(user, pw, id="login"):
    r = _send_command(id, "user:login", user, pw)
    return _check_command_answer(r, id)


def login_from_token(token, id="login_from_token"):
    r = _send_command(id, "user:login-from-token", token)
    return _check_command_answer(r, id)


def login_from_saved(user_id, key, id="login_from_saved"):
    r = _send_command(id, "user:login-from-saved", user_id, key)
    return _check_command_answer(r, id)


def user_resend_confirmation(id="user_resend_confirmation"):
    r = _send_command(id, "user:resend-confirmation")
    return _check_command_answer(r, id)


def get_login_token(sure, id="get_login_token"):
    r = _send_command(id, "user:get-login-token", sure)
    return _check_command_answer(r, id)


def save_login(id="save_login"):
    r = _send_command(id, "user:save-login")
    return _check_command_answer(r, id)


def logout(clear_cookie=True, id="logout"):
    r = _send_command(id, "user:logout", clear_cookie)
    return _check_command_answer(r, id)


def app_connected(id="app_connected"):
    r = _send_command(id, "app:connected")
    return _check_command_answer(r, id)


def stop(id="app_shutdown"):
    r = _send_command(id, "app:shutdown")
    return _check_command_answer(r, id)


def sync_start(id="sync_start"):
    r = _send_command(id, "sync:start")
    return _check_command_answer(r, id)


def sync_status(id="sync_status"):
    r = _send_command(id, "sync:status")
    return _check_command_answer(r, id)


def sync_stop(id="sync_stop"):
    r = _send_command(id, "sync:shutdown")
    return _check_command_answer(r, id)


def sync_shutdown(id="sync_shutdown"):
    r = _send_command(id, "sync:shutdown")
    return _check_command_answer(r, id)


def sync_pause(id="sync_pause"):
    r = _send_command(id, "sync:pause")
    return _check_command_answer(r, id)


def sync_resume(id="sync_resume"):
    r = _send_command(id, "sync:resume")
    return _check_command_answer(r, id)


def sync_incoming(id="sync_incoming"):
    r = _send_command(id, "sync:incoming")
    return _check_command_answer(r, id)


def profile_load(id="profile_load"):
    r = _send_command(id, "profile:load")
    return _check_command_answer(r, id)


def profile_get_notes(note_ids, id="profile_get_notes"):
    r = _send_command(id, "profile:get-notes", note_ids)
    return _check_command_answer(r, id)


def profile_find_notes(query, id="profile_find_notes"):
    r = _send_command(id, "profile:find-notes", query)
    return _check_command_answer(r, id)


def profile_sync_model(sync_action, sync_type, sync_record, id="profile_sync_model"):
    r = _send_command(id, "profile:sync:model", sync_action, sync_type, sync_record)
    return _check_command_answer(r, id)


def ping_pong(id="ping"):
    r = _send_command(id, "ping")
    success, resp = _check_command_answer(r, id)
    return success and resp['d']=='pong'
