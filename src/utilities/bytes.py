def generate_slices(data, slice_length=8, pad_char='x'):
    block_num = 0
    offset = 0
    while (offset < len(data)):
        yield(data[offset : offset+slice_length])
        block_num += 1
        offset = block_num * slice_length

def merge_bytes(byte_arr):
    result = bytes('', 'utf-8')
    for b in byte_arr:
        result += b
    return result

def xor(byte_a, byte_b):
    xor_result = b''
    block_len = (len(byte_a) if len(byte_a) <= len(byte_b) else len(byte_b))
    for i in range(0, block_len):
        c = chr(byte_a[i] ^ byte_b[i])
        xor_result += bytes(c, 'utf-8')
    return xor_result