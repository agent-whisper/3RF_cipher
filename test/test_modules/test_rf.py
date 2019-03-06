import unittest
from src.blockcipher.modules import round_functions
from src.utilities import bytes

class TestRF(unittest.TestCase):

	def test_32_rf_a(self):
		# test 32 bit
		block = b'TESTFREDTESTFREDTESTFREDTESTFRED'
		key = b'FREDTESTFREDTEST'
		expected = b'X\xfa\xb2Y\xa7\xc9\xcc\xa4\x07\x10\xb6\x05\xdf\xa3\xdfG'
		cipher_block = round_functions.rf_a(block[:len(block)//2], block[len(block)//2:], key)
		# print('32 bit : ',cipher_block)
		# self.assertEqual(True, True)
		self.assertEqual(cipher_block, expected)

	def test_16_rf_a(self):
		# test 16 bit
		block = b'TESTFREDTESTFRED'
		key = b'FARIZTES'
		expected = b'[\x98\x96\xf8\xe7\x89Y\x92'
		cipher_block = round_functions.rf_a(block[:len(block)//2], block[len(block)//2:], key)
		# print('16 bit : ',cipher_block)
		# self.assertEqual(True, True)
		self.assertEqual(cipher_block, expected)

	def test_32_rf_b(self):
		# test 32 bit
		block = b'TESTFREDTESTFREDTESTFREDTESTFRED'
		key = b'FREDTESTFREDTEST'
		expected = b'X\xfa\xb2YJ\xed\xa4IX\xfa\xb2YJ\xed\xa4I'
		cipher_block = round_functions.rf_b(block[:len(block)//2], block[len(block)//2:], key)
		# print('32 bit : ',cipher_block)
		# self.assertEqual(True, True)
		self.assertEqual(cipher_block, expected)

	def test_16_rf_b(self):
		# test 16 bit
		block = b'TESTFREDTESTFRED'
		key = b'FARIZTES'
		expected = b'`\x88\x96\xf9\xc4\xabq\x93'
		cipher_block = round_functions.rf_b(block[:len(block)//2], block[len(block)//2:], key)
		# print('16 bit : ',cipher_block)
		# self.assertEqual(True, True)
		self.assertEqual(cipher_block, expected)

	def test_32_rf_c(self):
		# test 32 bit
		block = b'TESTFREDTESTFREDTESTFREDTESTFRED'
		key = b'FREDTESTFREDTEST'
		expected = b'\xb2%C^`0en2g[f \x14\x15V'
		cipher_block = round_functions.rf_c(block[:len(block)//2], block[len(block)//2:], key)
		# print('32 bit : ',cipher_block)
		# self.assertEqual(True, True)
		self.assertEqual(cipher_block, expected)

	def test_16_rf_c(self):
		# test 16 bit
		block = b'TESTFREDTESTFRED'
		key = b'FARIZTES'
		expected = b'$Ek^f:u^'
		cipher_block = round_functions.rf_c(block[:len(block)//2], block[len(block)//2:], key)
		# print('16 bit : ',cipher_block)
		# self.assertEqual(True, True)
		self.assertEqual(cipher_block, expected)

	def test_256_rf_combination(self):
		block = b'TESTFREDTESTFREDTESTFREDTESTFREDFARIZTESFARIZTEZFARIZTESFARIZTEZ'
		key = b'FARIZTESFARIZTEZFARIZTESFARIZTEZTESTFREDTESTFREDTESTFREDTESTFRED'
		expected = b'\x0cAjk\x1ep\x15\t\xe2e\x02) tEbJ\xa9\xa6vX\xbe\xb0fJ\xa9\xa6vX\xbe\xb0fFARIZTESFARIZTEZ\x942\xbd\xd0\x86%\xab\xc0\x942\xbd\xd0\x86%\xab\xc0'
		cipher_block = round_functions.rf_combination(block, key, 0)
		self.assertEqual(cipher_block, expected)
		for i in range (0,5) :
			plain_block = round_functions.rf_combination(expected, key, i)
			self.assertEqual(True, True)

	def test_256_rf_inv_combination(self):	
		block = b'TESTFREDTESTFREDTESTFREDTESTFREDFARIZTESFARIZTEZFARIZTESFARIZTEZ'
		key = b'FARIZTESFARIZTEZFARIZTESFARIZTEZTESTFREDTESTFREDTESTFREDTESTFRED'
		cipher_block = round_functions.rf_combination(block, key, 0)
		plain_block = round_functions.rf_inv_combination(cipher_block, key, 0)
		self.assertEqual(block, plain_block)
		for i in range (0,6) :
			cipher_block = round_functions.rf_combination(block, key, i)
			plain_block = round_functions.rf_inv_combination(cipher_block, key, i)
			self.assertEqual(block, plain_block)

if __name__ == '__main__':
    unittest.main()