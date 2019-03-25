Turtl Note Client
===============================
[![Build Status](https://drone.github.dietzi.mywire.org/api/badges/toschoch/python-turtlpy/status.svg)](https://drone.github.dietzi.mywire.org/toschoch/python-turtlpy)

author: Tobias Schoch


Overview
--------

Python client for the Turtl Note App System. This is basically a wrapper around the turtl-core. Useful for backing up or building interfaces to other note taking apps.


Change-Log
----------
##### 0.7.0
* included build status into readme
* added drone pipeline
* added minimal tests
* working add, delete for Text, Bookmark and Password
* some improvments on the models
* some first data models
* added sync incoming command
* succeded login
* uses static library of turtl_core, complete procedual interface
* first roughly working version of import
* update readme
* project skeleton

##### 0.0.1
* initial version


Installation
------------
Installation from source requires the compilation of the core c-extension.
The turtl core-rs library is only available for gnu compilers (gcc)

To install use pip:

    pip install https://github.com/toschoch/python-turtlpy.git


Or clone the repo:

    git clone https://github.com/toschoch/python-turtlpy.git
    python setup.py install


    
Usage
-----

see [tests](tests/test_client.py)


```python
    with TurtlClient("http://<server-url>", "<username>", "<password>") as client:
        # user profile
        print(client.user)

        # boards
        print(client.boards)

        # spaces
        print(client.spaces)

        # find notes
        client.find_notes(space=client.get_space("Personal"))

        # add note
        # boards and spaces have .create_password .create_text_note and
        # .create_bookmark methods
        note = client.get_board("Passwords").create_password("title",text="text",
                username="user", password="pw", tags=["tag1"])
        client.add_note(note)

        # delete note
        client.delete_note(note)
```