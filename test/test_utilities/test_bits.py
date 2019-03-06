import unittest

from src.utilities import bits

class TestBitsMethods(unittest.TestCase):
	def test_bytes2bits(self) :
		input_variable = b'FERDI'
		expected = '0100011001000101010100100100010001001001'
		self.assertEqual(bits.bytes2bits(input_variable), expected)

	def test_bits2bytes(self) :
		input_variable = '0100011001000101010100100100010001001001'
		expected = b'FERDI'
		self.assertEqual(bits.bits2bytes(input_variable), expected)