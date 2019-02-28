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
            pb_xor = by.xor(pb, block_chain)
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

        plaintext_block = []
        for cb in ciphertext_blocks:
            pb_xor = Feistel.decrypt(cb, ext_key)
            block_chain = cb
            pb = by.xor(pb_xor, block_chain)
            plaintext_block.append(pb)
        plaintext = by.merge_bytes(plaintext_block)
        print(plaintext)
        return plaintext

class CipherFeedback():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        pass
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        pass



class OutputFeedback():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        pass
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        pass



class CounterMode():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        pass
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        pass