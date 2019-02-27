import unittest

import src.utilities.bytes as b

class TestBytesMethods(unittest.TestCase):
    def setUp(self):
        self.sample_data = bytes('abcdefghijklmnopqrstuvwxyz', 'utf-8')
        self.correct_slice_result = [
            bytes('abcdefgh', 'utf-8'),
            bytes('ijklmnop', 'utf-8'),
            bytes('qrstuvwx', 'utf-8'),
            bytes('yz', 'utf-8'),
        ]

    def test_generate_slices(self):
        result = []
        for d in b.generate_slices(self.sample_data):
            result.append(d)
        self.assertSequenceEqual(result, self.correct_slice_result)
    
    def test_merge_bytes(self):
        result = b.merge_bytes(self.correct_slice_result)
        self.assertEqual(result, self.sample_data)

