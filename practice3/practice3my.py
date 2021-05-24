import struct
import pprint

D_SIZE = 2 + 4 + 4 + 4 + 4 * 3 + 8
C_SIZE = 8 + 4 + 1 * 5
B_SIZE = 8 + 2 + 4 + 4
A_SIZE = B_SIZE + 4 + 4 + 4 + 2

f1 = (b'INMI\xc2+ip\xfe\x12!\xd2\xfb\xbd\x00\x00\x00\x07\x00\x00\x00&>\xd6\xb6&De'
      b'\x00\x00\x00\x04\x00\x00\x00q\x00\x89xxurybd\xbf\xe3\xb1\x12\xbd\xd9X'
      b'\xc6\xa4U\xa5\x90\xd4\xb6\x1e\x99\xc7?\xe9\x0f8\x9e\x87\x88\xfc\xfd\r'
      b'\xc9\xc7[\xc2\xdf\xbcm\xbf\xa1\x03\x86W4@`\x13;P\xb9\xc4\xab\x11\x083'
      b'?\xd5\x1c\xf2\x97\x1f\xda \xa5\xd1\xd1\xdcsmi\xa3\xcf\x00\x00\x00'
      b'-\x00\x00\x00>\x00\x00\x00O\x00\x00\x00`\x8c\xa2\x99\x10Q\xdam'
      b'\xbc\xd4\xf3\x00\x00\x00\x02\x00\x00\x00\x81\xf3}\x90\xb17/\x02m\xa4'
      b'\xdf\x08\xbd[7\xe3\xe4C\xf0\x03\x00=\xb8\xa7L')

f2 = (b'INMI\xa2h\xc2oa\x10\x859\x9e?\x00\x00\x00\x05\x00\x00\x00&\xbdl'
      b'\x07\xfd\x80\x92\x00\x00\x00\x04\x00\x00\x00o\x00\x8futqtl?\xdbW\x85|'
      b'\xd7\x15Lq\xdaz|\xf1\x80\xed\x07\xc6\xbf\xe9JuK\x8d\x82\x8a$%\x1c\xdcfV\xbe_'
      b'\x98\xbf\xe0\xd6\x96\x90\xa6\xb9\xc2\x10\xcb \x8a\xc3N\x0b\x1e\xed?\xc6'
      b's\xd7\x05(!\xe8Uw\x08n+$gQA\x00\x00\x00+\x00\x00\x00<\x00\x00\x00M\x00'
      b'\x00\x00^\xb2\xa6\xc3\x9c\xf4\xa9&\xc1\xdb\x8a\xebT\xa7\x0cVS\x05'
      b'^\x00\x00\x00\x04\x00\x00\x00\x7fOi\xd9Cf\xa0]\xc6\xd1G=\x8a\xd6\x0c\\'
      b'\x8byF\x16\x86[\xc6\xccg')


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset: offset + D_SIZE]
    d_parsed = struct.unpack('>hIIIIIIq', d_bytes)
    d2_bytes = byte_string[d_parsed[2]:d_parsed[2] + d_parsed[1]]
    d2_parsed = struct.unpack('>' + 'I' * d_parsed[1], d2_bytes)
    d4_bytes = byte_string[d_parsed[4]:d_parsed[4] + d_parsed[3] + 12]
    d4_parsed = struct.unpack('>I', d4_bytes)
    return {
        'D1': d_parsed[0],
        'D2': list(d2_parsed),
        'D3': d_parsed[3],
        'D4': list(d4_parsed),
        'D5': d_parsed[5]
    }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>dIbbbbb', byte_string)
    return {
        'C1': c_parsed[0],
        'C2': c_parsed[1],
        'C3': list(c_parsed[2:])
    }


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>qHii', b_bytes)
    b3_bytes = byte_string[b_parsed[3]:b_parsed[3] + b_parsed[2]]
    b3_parsed = struct.unpack('>' + 'I' * b3_parsed[1], b3_bytes)
    return {
        'B1': b_parsed[0],
        'B2': b_parsed[1],
        'B3': list(b3_parsed)
    }


def parse_a(offset, byte_string):
    a1_bytes = byte_string[offset:offset + B_SIZE]
    a1_parsed = parse_b(offset, byte_string)
    a_bytes = byte_string[offset + B_SIZE: offset + A_SIZE]
    a_parsed = struct.unpack('>fhIIH', a_bytes)
    a3_bytes = byte_string[a_bytes[3]: a_bytes[3] + a_bytes[2]]
    a3_parsed = struct.unpack('>I', a3_bytes)
    return {
        'A1': a1_parsed,
        'A2': a_parsed[1],
        'A3': a3_parsed,
        'A4': a_parsed[4]
    }


def f31(byte_string):
    return parse_a(4, byte_string)

print(f31(f1))
