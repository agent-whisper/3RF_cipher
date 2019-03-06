from src.blockcipher.modules import round_functions
from src.utilities import hash
# def sha256(input, numeral='byte'):
#     try:
#         input = input.encode('utf-8')
#     except AttributeError:
#         pass

#     if (numeral == 'byte'):
#         hash_result = hashlib.sha256(input).digest()
#     elif (numeral == 'hex'):
#         hash_result = hashlib.sha256(input).hexdigest()
#     else:
#         print('Numeral type not found; using bytes')
#         hash_result = hashlib.sha256(input).digest()
#     return hash_result

class Feistel():
	@staticmethod
	def encrypt(data_block, ext_key):
		data_block = data_block
		ext_key = hash.sha256(ext_key)
		len_round_key = len(ext_key) // 16

		for round_idx in range (0,16) :
			ext_round_key = ext_key[round_idx*len_round_key:(round_idx+1)*len_round_key]
			round_key = hash.sha256(ext_round_key)
			combination = 0
			for char in round_key :
				combination = (combination + char) % 6

			data_block = round_functions.rf_combination(data_block.decode('utf-8', 'ignore'), round_key.decode('utf-8', 'ignore'), combination)
		return data_block

	@staticmethod
	def decrypt(data_block, ext_key):
		return data_block