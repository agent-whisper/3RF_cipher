from src.utilities import file as fl, bytes as by, hash as hs
from  src.blockcipher.modules.feistel import Feistel

class ElectronicCodeBook():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=16)

        ciphertext_blocks = []
        for pb in plaintext_blocks:
            ciphertext_blocks.append(Feistel.encrypt(pb, ext_key))
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext 

    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=16)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            plaintext_blocks.append(Feistel.decrypt(cb, ext_key))
        plaintext = by.merge_bytes(plaintext_blocks)
        return plaintext



class CipherBlockChaining():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=16)
        block_chain = hs.md5(ext_key)
        
        ciphertext_blocks = []
        for pb in plaintext_blocks:
            pb_xor = by.xor_byte(pb, block_chain)
            cb = Feistel.encrypt(pb_xor, ext_key)
            block_chain = cb
            ciphertext_blocks.append(cb)
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=16)
        block_chain = hs.md5(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            pb_xor = Feistel.decrypt(cb, ext_key)
            pb = by.xor_byte(pb_xor, block_chain)
            block_chain = cb
            plaintext_blocks.append(pb)
        plaintext = by.merge_bytes(plaintext_blocks)
        return plaintext



class CipherFeedback():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename, byte_unit=1):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=16)
        feedback = hs.md5(ext_key)

        ciphertext_blocks = []
        for pb in plaintext_blocks:
            for i in range(0, len(pb), byte_unit):
                xor_key = Feistel.encrypt(feedback, ext_key)
                cb = by.xor_byte(pb[i:i+byte_unit], xor_key[0:byte_unit])
                ciphertext_blocks.append(cb)
                feedback = feedback[byte_unit:] + cb
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename, byte_unit=1):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=16)
        feedback = hs.md5(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            for i in range(0, len(cb), byte_unit):
                xor_key = Feistel.decrypt(feedback, ext_key)
                pb = by.xor_byte(cb[i:i+byte_unit], xor_key[0:byte_unit])
                plaintext_blocks.append(pb)
                feedback = feedback[byte_unit:] + cb
        plaintext = by.merge_bytes(plaintext_blocks)
        return plaintext



class OutputFeedback():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename, byte_unit=1):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=16)
        feedback = hs.md5(ext_key)

        ciphertext_blocks = []
        for pb in plaintext_blocks:
            for i in range(0, len(pb), byte_unit):
                xor_key = Feistel.encrypt(feedback, ext_key)
                cb = by.xor_byte(pb[i:i+byte_unit], xor_key[0:byte_unit])
                ciphertext_blocks.append(cb)
                feedback = feedback[byte_unit:] + xor_key[0:byte_unit]
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename, byte_unit=1):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=16)
        feedback = hs.md5(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            for i in range(0, len(cb), byte_unit):
                xor_key = Feistel.decrypt(feedback, ext_key)
                pb = by.xor_byte(cb[i:i+byte_unit], xor_key[0:byte_unit])
                plaintext_blocks.append(pb)
                feedback = feedback[byte_unit:] + xor_key[0:byte_unit]
        plaintext = by.merge_bytes(plaintext_blocks)
        return plaintext



class CounterMode():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=16)
        counter_block = hs.md5(ext_key)

        ciphertext_blocks = []
        for pb in plaintext_blocks:
            xor_key = Feistel.encrypt(counter_block, ext_key)
            cb = by.xor_byte(xor_key, pb)
            ciphertext_blocks.append(cb)
            counter_block = by.increment(counter_block)
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext 
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=16)
        counter_block = hs.md5(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            xor_key = Feistel.decrypt(counter_block, ext_key)
            pb = by.xor_byte(xor_key, cb)
            plaintext_blocks.append(Feistel.encrypt(pb, ext_key))
            counter_block = by.increment(counter_block)
        plaintext = by.merge_bytes(plaintext_blocks)
        return plaintext