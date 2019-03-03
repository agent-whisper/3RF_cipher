import unittest
from src.blockcipher.modules import pbox

class TestPbox(unittest.TestCase):

	def test_permute(self):
		# test 32 bit
		input_variable = 'TEST'
		expected = '¢1°2'
		permute_bytes = pbox.permute(input_variable)
		self.assertEqual(permute_bytes, expected)

		input_variable = 'TESTFRED'
		expected = '¢1°2DQ 8'
		permute_bytes = pbox.permute(input_variable)
		self.assertEqual(permute_bytes, expected)
		# self.assertEqual(True, True)
        
# 	def test_bytes2bits(self) :
# 		input_variable = "FERDI"
# 		expected = '0100011001000101010100100100010001001001'
# 		self.assertEqual(pbox.bytes2bits(input_variable), expected)

# 	def test_bits2bytes(self) :
# 		input_variable = '0100011001000101010100100100010001001001'
# 		expected = "FERDI"
		
# 		self.assertEqual(pbox.bits2bytes(input_variable), expected)

# 	def test_expand_bits(self) :
# 		expand_bits = '01000110010001010101001001000100'
# 		self.assertEqual(len(pbox.expand_bits(expand_bits)), 48)


# if __name__ == '__main__':
#     unittest.main()