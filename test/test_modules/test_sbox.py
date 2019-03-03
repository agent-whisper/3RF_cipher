import unittest
from src.blockcipher.modules import sbox

class TestSbox(unittest.TestCase):

	def test_subtitute(self):
		self.assertEqual(sbox.substitute('fariz'), '3ï@ùÚ')

if __name__ == '__main__':
    unittest.main()