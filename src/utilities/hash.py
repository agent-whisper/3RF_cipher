import hashlib

def sha256(key_string, numeral='byte'):
    if (numeral == 'byte'):
        hash_result = hashlib.sha256(key_string.encode()).digest()
    elif (numeral == 'hex'):
        hash_result = hashlib.sha256(key_string.encode()).hexdigest()
    else:
        print('Numeral type not found; using bytes')
        hash_result = hashlib.sha256(key_string.encode()).digest()
    return hash_result

def md5(key_string, numeral='byte'):
    if (numeral == 'byte'):
        hash_result = hashlib.md5(key_string.encode()).digest()
    elif (numeral == 'hex'):
        hash_result = hashlib.md5(key_string.encode()).hexdigest()
    else:
        print('Numeral type not found; using bytes')
        hash_result = hashlib.md5(key_string.encode()).digest()
    return hash_result