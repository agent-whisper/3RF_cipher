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

    def test_add_by_one(self):
        case_1 = bytes('{}{}{}'.format(chr(65), chr(255), chr(255)), 'utf-8')
        case_2 = bytes('{}{}{}'.format(chr(255), chr(255), chr(255)), 'utf-8')
        case_3 = bytes('{}{}{}'.format(chr(65), chr(66), chr(67)), 'utf-8')
        case_4 = bytes('{}{}{}'.format(chr(255), chr(254), chr(255)), 'utf-8')

        ans_1 = bytes('{}{}{}'.format(chr(66), chr(0), chr(0)), 'utf-8')
        ans_2 = bytes('{}{}{}'.format(chr(0), chr(0), chr(0)), 'utf-8')
        ans_3 = bytes('{}{}{}'.format(chr(65), chr(66), chr(68)), 'utf-8')
        ans_4 = bytes('{}{}{}'.format(chr(255), chr(255), chr(0)), 'utf-8')

        case_1 = b.increment(case_1, 'utf-8')
        self.assertEqual(ans_1, case_1)
        case_2 = b.increment(case_2, 'utf-8')
        self.assertEqual(ans_2, case_2)
        case_3 = b.increment(case_3, 'utf-8')
        self.assertEqual(ans_3, case_3)
        case_4 = b.increment(case_4, 'utf-8')
        self.assertEqual(ans_4, case_4)