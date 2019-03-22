
from libc.stdint cimport int32_t, uint8_t
import json
import logging

log = logging.getLogger(__name__)

cdef extern:
    extern int32_t turtlc_start(const char*, uint8_t)
    extern int32_t turtlc_send(const uint8_t*, Py_ssize_t)
    extern const uint8_t* turtlc_recv(uint8_t, const char*, Py_ssize_t*)
    extern const uint8_t* turtlc_recv_event(uint8_t, Py_ssize_t*)
    extern int32_t turtlc_free(const uint8_t*, Py_ssize_t)
    extern char* turtlc_lasterr()
    extern int32_t turtlc_free_err(char*)

def start(config, daemon=1):
    return turtlc_start(bytes(json.dumps(config), 'utf-8'), daemon)

def send(msg):
    return turtlc_send(msg, len(msg))

def recv(block=False):
    cdef uint8_t *c_string = NULL
    cdef Py_ssize_t length = 0

    # get pointer and length from a C function
    c_string = turtlc_recv(not block, NULL, &length)

    if c_string == NULL:
        if length>0:
            return lasterr()
        return {}

    try:
        py_bytes_string = c_string[:length]  # Performs a copy of the data
    finally:
        turtlc_free(c_string, length)

    return json.loads(py_bytes_string)

def recv_event(block=False):
    cdef uint8_t *c_string = NULL
    cdef Py_ssize_t length = 0

    # get pointer and length from a C function
    c_string = turtlc_recv_event(not block, &length)

    if c_string == NULL:
        if length>0:
            return lasterr()
        return {}

    try:
        py_bytes_string = c_string[:length]  # Performs a copy of the data
    finally:
        turtlc_free(c_string, length)

    return json.loads(py_bytes_string)

def lasterr():
    cdef bytes py_string
    cdef char * c_string = turtlc_lasterr()

    if c_string == NULL:
        return {}

    try:
        py_string = c_string
    finally:
        turtlc_free_err(c_string)

    return py_string