import unittest
from src.blockcipher.modules import transform

class TestTransform(unittest.TestCase):

	def test_64_transform(self):
		# test 64 bit
		input_variable = 'TESTFRED'
		expected = 'TETSFRDE'
		transformed_bytes = transform.shift_rows(input_variable)
		self.assertEqual(transformed_bytes, expected)
	def test_128_transform(self):	
		# test 128 bit
		input_variable = 'TESTFREDTESTFRED'
		expected = 'TESTDFRESTTEREDF'
		transformed_bytes = transform.shift_rows(input_variable)
		self.assertEqual(transformed_bytes, expected)

if __name__ == '__main__':
    unittest.main()