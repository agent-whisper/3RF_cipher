from src.utilities import hash, bytes

def generate_round_keys(ext_key, division_val):
    ext_key = hash.sha256(ext_key)
    round_keys = []
    for key_parts in bytes.generate_slices(ext_key, slice_length=division_val):
        round_keys.append(hash.sha256(key_parts))
    return round_keys