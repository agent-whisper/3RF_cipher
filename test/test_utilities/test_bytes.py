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

    def test_xor_byte(self):
        self.assertEqual(bytes([0, 0, 0]), b.xor_byte(b'abc', b'abc'))
        self.assertEqual(b'@CB', b.xor_byte(b'ABC', bytes([1, 1, 1])))
        self.assertEqual(b'@@@@', b.xor_byte(b'ABCDEF', bytes([1, 2, 3, 4])))
        self.assertEqual(b'@FKTe', b.xor_byte(b'ABCDEF', bytes([1, 4, 8, 16, 32, 64, 128])))

    def test_add_by_one(self):
        case_1 = bytes([65, 255, 255])
        case_2 = bytes([255, 255, 255])
        case_3 = bytes([65, 66, 67])
        case_4 = bytes([255, 254, 255])

        ans_1 = bytes([66, 0, 0])
        ans_2 = bytes([0, 0, 0])
        ans_3 = bytes([65, 66, 68])
        ans_4 = bytes([255, 255, 0])

        case_1 = b.increment(case_1)
        self.assertEqual(ans_1, case_1)
        case_2 = b.increment(case_2)
        self.assertEqual(ans_2, case_2)
        case_3 = b.increment(case_3)
        self.assertEqual(ans_3, case_3)
        case_4 = b.increment(case_4)
        self.assertEqual(ans_4, case_4)