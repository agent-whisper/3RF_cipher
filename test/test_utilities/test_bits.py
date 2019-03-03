import unittest

import src.utilities.bits as bits

class TestBitsMethods(unittest.TestCase):
	def test_bytes2bits(self) :
		input_variable = "FERDI"
		expected = '0100011001000101010100100100010001001001'
		self.assertEqual(bits.bytes2bits(input_variable), expected)

	def test_bits2bytes(self) :
		input_variable = '0100011001000101010100100100010001001001'
		expected = "FERDI"
		
		self.assertEqual(bits.bits2bytes(input_variable), expected)