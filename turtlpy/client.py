import logging

log = logging.getLogger(__name__)

to_dict = lambda o: {k:v for k,v in o.__dict__.items() if v is not None}