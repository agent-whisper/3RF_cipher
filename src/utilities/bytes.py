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