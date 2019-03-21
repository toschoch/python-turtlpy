
from libc.stdint cimport int32_t, uint8_t

cdef extern:
    extern int32_t turtlc_start(const char*, uint8_t)

def turtlc_start(unsigned char[:] config):
    return turtlc_start(config, 1)