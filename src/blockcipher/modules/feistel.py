from src.blockcipher.modules import round_functions
from src.utilities import hash


class Feistel():
	@staticmethod
	def encrypt(data_block, ext_key):
		ext_key = hash.sha256(ext_key)
		len_round_key = len(ext_key) // 16

		for round_idx in range (0,16) :
			ext_round_key = ext_key[round_idx*len_round_key:(round_idx+1)*len_round_key]
			round_key = hash.sha256(ext_round_key)
			combination = 0
			for char in round_key :
				combination = (combination + char) % 6
			data_block = round_functions.rf_combination(data_block, round_key, combination)
		return data_block

	@staticmethod
	def decrypt(data_block, ext_key):
		ext_key = hash.sha256(ext_key)
		len_round_key = len(ext_key) // 16

		for round_idx in range (15,-1,-1) :
			ext_round_key = ext_key[round_idx*len_round_key:(round_idx+1)*len_round_key]
			round_key = hash.sha256(ext_round_key)
			combination = 0
			for char in round_key :
				combination = (combination + char) % 6
			data_block = round_functions.rf_inv_combination(data_block, round_key, combination)
		return data_block