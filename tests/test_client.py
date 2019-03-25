from turtlpy.client import TurtlClient

import logging

log = logging.getLogger(__name__)

def test_instantiate():

    with TurtlClient("https://apiv3.turtlapp.com","testuser@gmail.com","test") as client:

        board = client.get_board("Personal")

        pw = client.add_note(board.create_password("test pw", "don't know", "user", "password", tags=["test"]))
        link = client.add_note(board.create_bookmark("test bookmark", "text", "https", tags=['test']))
        text = client.add_note(board.create_text_note("test text",r"$E=m\cdot c^2$", tags=['test','formula']))

        test_notes = client.find_notes({"tags":["test"]})
        for note in test_notes:
            client.delete_note(note)
