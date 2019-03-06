import unittest
from src.blockcipher.modules import transform

class TestTransform(unittest.TestCase):

	def test_32_transform(self):
		# test 64 bit
		input_variable = b'TEST'
		expected = b'TETS'
		transformed_bytes = transform.shift_rows(input_variable)
		self.assertEqual(transformed_bytes, expected)

	def test_64_transform(self):
		# test 64 bit
		input_variable = b'TESTFRED'
		expected = b'TETSFRDE'
		transformed_bytes = transform.shift_rows(input_variable)
		self.assertEqual(transformed_bytes, expected)

	def test_128_transform(self):	
		# test 128 bit
		input_variable = b'TESTFREDTESTFRED'
		expected = b'TESTDFRESTTEREDF'
		transformed_bytes = transform.shift_rows(input_variable)
		self.assertEqual(transformed_bytes, expected)

if __name__ == '__main__':
    unittest.main()