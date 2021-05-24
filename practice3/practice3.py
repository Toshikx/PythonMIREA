import pprint
import struct

F_SIZE = 5
E_SIZE = 1 + 2 + 4 + 4 + 2 + 8 + 4 + 2  + 4 + 1
D_SIZE = 5
C_SIZE = 8 + 4 + 8 + D_SIZE + 2 + 4 + 4
B_SIZE = 4 + 8 * 4
A_SIZE = 4 + 4 + F_SIZE + 1 + 4 + 2 + 4

f1 = (b'BPUJ\x00\x00\x00\x9cD\xaeU@\xc4\xe1\xeb\x1fk\xa5\r]\x01i\xbb\xe53>L\xf9'
b'\x03\x04\x92\xd6k\xea\xe0\xb3\xc5\xb4w\x99"F\xcd\x1bk\xe2\t/\xbd\x00\x00\x00'
b'\x04\x00 \xbf\xde;\x0f\x8el\xe3L\xd51p \x00\x02\x00\x00\x00(\xab\xa1\xcf'
b'\xbb\xed\x9e\x103\xe3\x1b\x81\x9c3\x86,i\x86D\x9c\x00\x00\x00\x02'
b'\x00J\xbf\xe9\t\xdaj\xaf\x0b\xbc\xf7C\\\x8c\x00\x07\x00\x00\x00N$\x00*\x00'
b'U?\xe5\x8e\x8cj_\xc8Z\x8eH\x9a\x9f\xbf\xd6\x99\x04\x9d~\xa4<\xb4`\xc4'
b'\x9c\xf7\xaaX\x00\x00\x00\x02\x00\x00\x00u\x00\x00\x00y-e<\nH\x86\x1b\x0e'
b'@\x1f\xfc+\xdc\xad\xae\x15%\xce\xce\x8d\x84\xe7\r\x94l1*\xa2H\x95o,')

def parse_f(offset, byte_string):
    f_bytes = byte_string[offset:offset + F_SIZE]
    f_parsed = struct.unpack('>Ib', f_bytes)
    return {'F1': f_parsed[0], 'F2': f_parsed[1]}


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset: offset + E_SIZE]
    e_parsed = struct.unpack('>bhiIHdiHIb', e_bytes)
    e4_bytes = byte_string[e_parsed[4]:e_parsed[4]+e_parsed[3] * 2]
    e4_parsed = struct.unpack('>' + 'H' * e_parsed[3], e4_bytes)
    e7_bytes = byte_string[e_parsed[8]:e_parsed[8]+e_parsed[7]]
    e7_parsed = struct.unpack('>' + 'B' * e_parsed[7], e7_bytes)
    return {'E1': e_parsed[0],
            'E2': e_parsed[1],
            'E3': e_parsed[2],
            'E4': list(e4_parsed),
            'E5': e_parsed[5],
            'E6': e_parsed[6],
            'E7': list(e7_parsed),
            'E8': e_parsed[9]}


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>bHh', d_bytes)
    return {'D1': d_parsed[0],
            'D2': d_parsed[1],
            'D3': d_parsed[2]}

def parse_c(offset, byte_string):
    c123_bytes = byte_string[offset:offset + 20]
    c123_parsed = struct.unpack('>dId', c123_bytes)
    c4_parsed = parse_d(offset + 20, byte_string)
    c56_bytes = byte_string[offset + 20 + D_SIZE:offset + 20 + D_SIZE + 10]
    c56_parsed = struct.unpack('>HII', c56_bytes)
    c6_parsed = struct.unpack('>' + 'H' * c56_parsed[1],byte_string[c56_parsed[2]: c56_parsed[2] + c56_parsed[1] * 2])
    c6_list = [parse_e(addr, byte_string) for addr in c6_parsed]
    return {'C1': c123_parsed[0],
            'C2': c123_parsed[1],
            'C3': c123_parsed[2],
            'C4': c4_parsed,
            'C5': c56_parsed[0],
            'C6': c6_list}

def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>Iqqqq',b_bytes)
    return {
        'B1': parse_c(b_parsed[0], byte_string),
        'B2': list(b_parsed[1:])
    }

def parse_a(offset, byte_string):
    a12_bytes = byte_string[offset:offset + 8]
    a12_parsed = struct.unpack('>Ii',a12_bytes)
    a3_parsed = parse_f(offset + 8, byte_string)
    a45678_bytes = byte_string[offset + 8 + F_SIZE:offset + 8 + F_SIZE + 15]
    a45678_parsed = struct.unpack('>biihi', a45678_bytes)
    return {'A1': parse_b(a12_parsed[0, byte_string]),
            'A2': a12_parsed[1],
            'A3': a3_parsed,
            'A4': a45678_parsed[0],
            'A5': a45678_parsed[1],
            'A6': a45678_parsed[2],
            'A7': a45678_parsed[3],
            'A8': a45678_parsed[4],}

def f31(byte_string):
    return parse_a(4, byte_string)

print(f31(f1))