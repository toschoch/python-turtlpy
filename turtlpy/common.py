#!/usr/bin/python
# -*- coding: UTF-8 -*-
# created: 25.03.2019
# author:  TOS

import logging

log = logging.getLogger(__name__)

convert_to_dict = lambda o: {k:v for k,v in o.__dict__.items() if v is not None}

class Model(object):

    def to_dict(self):
        return convert_to_dict(self)

    def __repr__(self):
        d = self.to_dict()
        return "{type}({args})".format(type=self.__class__.__name__,
                                       args=", ".join(map(lambda it:'{}="{}"'.format(*it), d.items())))
