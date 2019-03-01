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

def xor_byte(byte_arr_a, byte_arr_b):
    xor_result = b''
    block_len = (len(byte_arr_a) if len(byte_arr_a) <= len(byte_arr_b) else len(byte_arr_b))
    for i in range(0, block_len):
        c = chr(byte_arr_a[i] ^ byte_arr_b[i])
        xor_result += bytes(c, 'utf-8')
    return xor_result

def increment(byte_string):
    temp = byte_string
    idx = len(temp) - 1
    while (idx >= 0):
        if ((temp[idx]) < 255):
            temp = temp[:idx] + bytes([temp[idx]+1]) + temp[idx+1:]
            return temp
        else:
            temp = temp[:idx] + bytes([0]) + temp[idx+1:]
            idx -=1
    return temp
        