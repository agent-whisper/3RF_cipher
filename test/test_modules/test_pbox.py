import unittest
from src.blockcipher.modules import pbox
from src.utilities import bytes as byte

class TestPbox(unittest.TestCase):

	def test_32_permute(self):
		input_variable = b'TEST'
		expected = byte.string2bytes('¢1°2')
		permute_bytes = pbox.permute(input_variable)
		# print(len(input_variable), len(expected))
		self.assertEqual(permute_bytes, expected)

	def test_64_permute(self):
		# test 64 bit
		input_variable = b'TESTFRED'
		expected = byte.string2bytes('¢1°2DQ 8')
		permute_bytes = pbox.permute(input_variable)
		# print(len(input_variable), len(expected))
		self.assertEqual(permute_bytes, expected)

	def test_128_permute(self):
		# test 128 bit
		input_variable = b'TESTFREDTESTFRED'
		expected = byte.string2bytes('¢1°2DQ 8¢1°2DQ 8')
		permute_bytes = pbox.permute(input_variable)
		# print(len(input_variable), len(expected))
		self.assertEqual(permute_bytes, expected)

if __name__ == '__main__':
    unittest.main()