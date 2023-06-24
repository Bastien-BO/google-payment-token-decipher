"""
All utility class and function for the decryption process
"""


def int_to_byte_array(capacity: int, value: int) -> bytearray:
    out = bytearray(capacity)
    for elem in range(0, capacity):
        out[elem] = ((value >> (8 * elem)) & 0xFF)
    return out


def to_length_value(*args) -> bytearray:
    out = bytearray()
    for elem in args:
        byte_elem = bytearray(elem, 'utf-8')
        out += int_to_byte_array(4, len(byte_elem))
        out += byte_elem
    return out