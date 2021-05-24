import struct

D_SIZE = 2 + 4 + 4 + 4 + 4 * 3 + 8
C_SIZE = 8 + 4 + 1 * 5
B_SIZE = 8 + 2 + 4 + 4
A_SIZE = B_SIZE + 4 + 4 + 4 + 2

def parse_d(offset, byte_string):
    d_bytes = byte_string[offset: offset + D_SIZE]
    d_parsed = struct.unpack('>hIIIIIIq', d_bytes)
    d2_bytes = byte_string[d_parsed[2]:d_parsed[2]+d_parsed[1]]
    d2_parsed = struct.unpack('>' * 'I' * d_parsed[1], d2_bytes)
    return {
        'D1': d_parsed[0],
        'D2': list(d2_parsed),
        'D3': d_parsed[3],
        'D4':

    }