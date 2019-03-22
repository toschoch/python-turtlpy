import turtlpy.core as core
import json
import logging

log = logging.getLogger(__name__)


def _send_command(msg_id, cmd, *args):
    r = core.send(bytes(json.dumps([msg_id, cmd] + list(args)),'utf-8'))
    log.debug("send command '{}'... ({})".format(cmd, r))
    return r


def start(server, server_v2=None):

    config = {
        'api': {
            'endpoint': server,
        },
        #"openssl_cert_file": "/opt/turtl/resources/app/scripts/resources/cacert.pem"
    }

    if server_v2 is not None:
        config['api']['v6'] = {'endpoint': server_v2}

    if not ping_pong():
        log.info("trying to start turtl core...")
        core.start(config)
        r = core.recv_event(True)
        log.debug("received event {}".format(r))
        return 'e' in r and ['e'] == "messaging:ready"
    else:
        log.info("turtl core is already running...")
        return 0


def login(user, pw, id="login_msg"):
    r = _send_command(id, "user:login", user, pw)
    if r != 0: return False
    r2 = core.recv(True)
    log.debug("login returned: {}".format(r2))
    return r2['e']==0


def logout(clear_cookie=True, id="logout_msg"):
    return _send_command(id, "user:logout", clear_cookie)


def sync_status(id="sync_status_msg"):
    return _send_command(id, "")


def ping_pong(id="ping"):
    r = _send_command(id, "ping")
    if r != 0: return False
    r2 = core.recv(block=True)
    log.debug("ping returned: {}".format(r2))
    return r2['id']=='ping' and r2['e']==0 and r2['d']=='pong'
