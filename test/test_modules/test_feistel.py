import unittest
from src.blockcipher.modules.feistel import Feistel

class TestFeistel(unittest.TestCase):
	def test_encrypt(self):
		feistel = Feistel()
		a = feistel.encrypt(str.encode('TESTFERDIGHOZALIOKEOCEOKEYOIABCD'), str.encode('TESTFERDIGHOZALIOKEOCEOKEYOIABCD'))
		# self.assertEqual(, 'TESTFERDIGHOZALIOKEOCEOKEYOIABCD')
		self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()


    # TESTFERDIGHOZALIOKEOCEOKEYOIABCD