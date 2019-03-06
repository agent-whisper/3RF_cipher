import unittest
from src.blockcipher.modules import sbox

class TestSbox(unittest.TestCase):

	def test_subtitute(self):
		input_variable = b'@FKTe'
		expected = b'\tZ\xb3 Mo'
		print(len(input_variable), len(expected))
		self.assertEqual(sbox.substitute(input_variable), expected)

if __name__ == '__main__':
    unittest.main()