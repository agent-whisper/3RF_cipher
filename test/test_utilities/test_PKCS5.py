import unittest

from src.utilities.padding import PCKS5

class TestBytesMethods(unittest.TestCase):
    def test_insert_padding(self):
        case_1_byte = b'123'
        case_1_tgt_len = 8
        case_2_byte = b'12345678'
        case_2_tgt_len = 8
        case_3_byte = b'1234567'
        case_3_tgt_len = 5

        ans_1 = [(case_1_byte + bytes([5]) * 5), b'', True]
        ans_2 = [case_2_byte, bytes([8]) * 8, True]
        ans_3 = [case_3_byte, b'', False]

        result_1 = PCKS5.insert_padding(case_1_byte, case_1_tgt_len)
        self.assertListEqual(ans_1, result_1)

        result_2 = PCKS5.insert_padding(case_2_byte, case_2_tgt_len)
        self.assertListEqual(ans_2, result_2)

        result_3 = PCKS5.insert_padding(case_3_byte, case_3_tgt_len)
        self.assertListEqual(ans_3, result_3)
    
    def test_remove_padding(self):
        case_1 = b'abc' + bytes([5]) * 5
        case_2 = b'abcdefgh' + bytes([8]) * 8
        case_3 = b'abcd' + bytes([4, 6, 4, 4])
        case_4 = b'abcdefg' + bytes([8])
        case_5 = b'abcdef' + bytes([10])

        ans_1 = b'abc'
        ans_2 = b'abcdefgh'
        ans_3 = b'abcd' + bytes([4, 6, 4, 4])
        ans_4 = b'abcdefg' + bytes([8])
        ans_5 = b'abcdef' + bytes([10])

        self.assertEqual(ans_1, PCKS5.remove_padding(case_1))
        self.assertEqual(ans_2, PCKS5.remove_padding(case_2))
        self.assertEqual(ans_3, PCKS5.remove_padding(case_3))
        self.assertEqual(ans_4, PCKS5.remove_padding(case_4))
        self.assertEqual(ans_5, PCKS5.remove_padding(case_5))