import unittest
from src.blockcipher.modules import pbox

class TestPbox(unittest.TestCase):

	def test_64_permute(self):
		# test 64 bit
		input_variable = 'TESTFRED'
		expected = '¢1°2DQ 8'
		permute_bytes = pbox.permute(input_variable)
		self.assertEqual(permute_bytes, expected)

	def test_128_permute(self):
		# test 128 bit
		input_variable = 'TESTFREDTESTFRED'
		expected = '¢1°2DQ 8¢1°2DQ 8'
		permute_bytes = pbox.permute(input_variable)
		self.assertEqual(permute_bytes, expected)

if __name__ == '__main__':
    unittest.main()