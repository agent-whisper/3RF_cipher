import unittest
from src.blockcipher.modules.feistel import Feistel

class TestFeistel(unittest.TestCase):
	def test_encrypt_decrypt(self):
		feistel = Feistel()
		block = b'TESTMYNAMEISMOKHAMADFERDIGHOZALI'
		key = b'FARIZTUMBUANTHISISOKE'
		cipher = feistel.encrypt(block, key)
		# print("a",len(cipher))
		print('-----------------------------------------')
		plain_block = feistel.decrypt(cipher, key)
		self.assertEqual(block, plain_block)


if __name__ == '__main__':
    unittest.main()