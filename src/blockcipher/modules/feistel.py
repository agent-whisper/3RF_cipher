from src.blockcipher.modules import round_functions
from src.utilities import hash
from src.blockcipher.key import scheduling

class Feistel():
	@staticmethod
	def encrypt(data_block, ext_key):
		round_keys = scheduling.generate_round_keys(ext_key, 2)

		for round_idx in range (0,16) :
			combination = 0
			for char in round_keys[round_idx] :
				combination = (combination + char) % 6
			data_block = round_functions.rf_combination(data_block, round_keys[round_idx], combination)
		return data_block

	@staticmethod
	def decrypt(data_block, ext_key):
		round_keys = scheduling.generate_round_keys(ext_key, 2)

		for round_idx in range (15,-1,-1) :
			combination = 0
			for char in round_keys[round_idx] :
				combination = (combination + char) % 6
			data_block = round_functions.rf_inv_combination(data_block, round_keys[round_idx], combination)
		return data_block