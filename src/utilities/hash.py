import hashlib

def sha256(input, numeral='byte'):
    try:
        input = input.encode('utf-8')
    except AttributeError:
        pass

    if (numeral == 'byte'):
        hash_result = hashlib.sha256(input).digest()
    elif (numeral == 'hex'):
        hash_result = hashlib.sha256(input).hexdigest()
    else:
        print('Numeral type not found; using bytes')
        hash_result = hashlib.sha256(input).digest()
    return hash_result

def md5(input, numeral='byte'):
    try:
        input = input.encode('utf-8')
    except AttributeError:
        pass
        
    if (numeral == 'byte'):
        hash_result = hashlib.md5(input).digest()
    elif (numeral == 'hex'):
        hash_result = hashlib.md5(input).hexdigest()
    else:
        print('Numeral type not found; using bytes')
        hash_result = hashlib.md5(input).digest()
    return hash_result