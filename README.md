Turtl Note Client
===============================
author: Tobias Schoch

Overview
--------

Python client for the Turtl Note App System. This is basically a wrapper around the turtl-core. Useful for backing up or building interfaces to other note taking apps.


Change-Log
----------
##### 0.0.1
* initial version


Installation
------------

To install use pip:

    pip install https://github.com/toschoch/python-turtlpy.git


Or clone the repo:

    git clone https://github.com/toschoch/python-turtlpy.git
    python setup.py install


    
Usage
-----

```python
    with TurtlClient("http://<server-url>", "<username>", "<password>") as client:
        # user profile
        print(client.user)

        # boards
        print(client.boards)

        # spaces
        print(client.spaces)

        # ensure synced
        client.sync()
```