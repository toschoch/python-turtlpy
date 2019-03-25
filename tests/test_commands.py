from turtlpy import commands as client
import pytest
import logging

log = logging.getLogger(__name__)

@pytest.fixture()
def turtl():
    client.start("https://apiv3.turtlapp.com")
    yield "resource"

def test_ping_pong(turtl):
    assert client.ping_pong()
