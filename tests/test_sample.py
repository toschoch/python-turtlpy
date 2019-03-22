from turtlpy import client
from turtlpy import core
import pytest
import logging

log = logging.getLogger(__name__)

@pytest.fixture()
def turtl():
    client.start("https://apiv3.turtlapp.com")
    yield "resource"

def test_login(turtl):
    assert not client.login("tobias.schoch@vtxmail.ch","asdfa")

def test_ping_pong(turtl):
    assert client.ping_pong()

def test_app(turtl):
    pass
    #client._send_command("app","user:login","tobias.schoch@vtxmail.ch","&Roma0809&")
    #log.info(core.recv(block=True))
    #log.info(core.recv_event())