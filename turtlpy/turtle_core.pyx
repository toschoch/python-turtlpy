
from libc.stdint cimport int32_t, uint8_t
from libc.stdlib cimport free as cfree
import json

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

def recv_event(background, msg_id):
    cdef uint8_t *c_string = NULL
    cdef Py_ssize_t length = 0

    # get pointer and length from a C function
    c_string = turtlc_recv(background, msg_id, &length)

    try:
        py_bytes_string = c_string[:length]  # Performs a copy of the data
        turtlc_free(c_string, length)
    except:
        cfree(c_string)
        py_bytes_string = ""

    return py_bytes_string

def recv_event_event(background):
    cdef uint8_t *c_string = NULL
    cdef Py_ssize_t length = 0

    # get pointer and length from a C function
    c_string = turtlc_recv_event(background, &length)

    try:
        py_bytes_string = c_string[:length]  # Performs a copy of the data
        turtlc_free(c_string, length)
    except:
        cfree(c_string)
        py_bytes_string = ""

    return py_bytes_string

def lasterr():
    cdef bytes py_string
    cdef char * c_string = turtlc_lasterr()
    try:
        py_string = c_string
        turtlc_free_err(c_string)
    except:
        cfree(c_string)
        py_string = b""

    return py_string