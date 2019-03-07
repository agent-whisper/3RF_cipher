from src.utilities import file as fl, bytes as by, hash as hs
from src.utilities.padding import PCKS5
from  src.blockcipher.modules.feistel import Feistel

class ElectronicCodeBook():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=32, check_next_exist=True)

        ciphertext_blocks = []
        for pb, has_next in plaintext_blocks:
            padding_block = b''
            if not has_next:
                padding_result = PCKS5.insert_padding(pb, 32)
                pb = padding_result[0]
                padding_block = padding_result[1]
            ciphertext_blocks.append(Feistel.encrypt(pb, ext_key))
            if padding_block != b'':
                ciphertext_blocks.append(Feistel.encrypt(padding_block, ext_key))
            
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext

    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=32)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            plaintext_blocks.append(Feistel.decrypt(cb, ext_key))
        plaintext = by.merge_bytes(plaintext_blocks)
        plaintext = PCKS5.remove_padding(plaintext)
        return plaintext



class CipherBlockChaining():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=32, check_next_exist=True)
        block_chain = hs.sha256(ext_key)
        
        ciphertext_blocks = []
        for pb, has_next in plaintext_blocks:
            padding_block = b''
            if not has_next:
                padding_result = PCKS5.insert_padding(pb, 32)
                pb = padding_result[0]
                padding_block = padding_result[1]
            pb_xor = by.xor_byte(pb, block_chain)
            cb = Feistel.encrypt(pb_xor, ext_key)
            block_chain = cb
            ciphertext_blocks.append(cb)

            if (padding_block != b''):
                pb_xor = by.xor_byte(padding_block, block_chain)
                cb = Feistel.encrypt(pb_xor, ext_key)
                block_chain = cb
                ciphertext_blocks.append(cb)
            
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=32)
        block_chain = hs.sha256(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            pb_xor = Feistel.decrypt(cb, ext_key)
            pb = by.xor_byte(pb_xor, block_chain)
            block_chain = cb
            plaintext_blocks.append(pb)
        plaintext = by.merge_bytes(plaintext_blocks)
        plaintext = PCKS5.remove_padding(plaintext)
        return plaintext

class CipherFeedback():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename, byte_unit=1):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=byte_unit, check_next_exist=True)
        feedback = hs.sha256(ext_key)

        ciphertext_blocks = []
        for pb, has_next in plaintext_blocks:
            padding_block = b''
            if not has_next and byte_unit > 1:
                padding_result = PCKS5.insert_padding(pb, byte_unit)
                pb = padding_result[0]
                padding_block = padding_result[1]
            xor_key = Feistel.encrypt(feedback, ext_key)
            cb = by.xor_byte(pb, xor_key[0:byte_unit])
            ciphertext_blocks.append(cb)
            feedback = feedback[byte_unit:] + cb

            if padding_block != b'':
                xor_key = Feistel.encrypt(feedback, ext_key)
                cb = by.xor_byte(padding_block, xor_key[0:byte_unit])
                ciphertext_blocks.append(cb)
                feedback = feedback[byte_unit:] + cb
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename, byte_unit=1):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=byte_unit)
        feedback = hs.sha256(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            xor_key = Feistel.encrypt(feedback, ext_key)
            pb = by.xor_byte(cb, xor_key[0:byte_unit])
            plaintext_blocks.append(pb)
            feedback = feedback[byte_unit:] + cb
        plaintext = by.merge_bytes(plaintext_blocks)
        plaintext = PCKS5.remove_padding(plaintext)
        return plaintext



class OutputFeedback():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename, byte_unit=1):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=32, check_next_exist=True)
        feedback = hs.sha256(ext_key)

        ciphertext_blocks = []
        for pb, has_next in plaintext_blocks:
            padding_block = b''
            if not has_next:
                padding_result = PCKS5.insert_padding(pb, 32)
                pb = padding_result[0]
                padding_block = padding_result[1]

            for i in range(0, len(pb), byte_unit):
                xor_key = Feistel.encrypt(feedback, ext_key)
                cb = by.xor_byte(pb[i:i+byte_unit], xor_key[0:byte_unit])
                ciphertext_blocks.append(cb)
                feedback = feedback[byte_unit:] + xor_key[0:byte_unit]

            if padding_block != b'':
                for i in range(0, len(padding_block), byte_unit):
                    xor_key = Feistel.encrypt(feedback, ext_key)
                    cb = by.xor_byte(padding_block[i:i+byte_unit], xor_key[0:byte_unit])
                    ciphertext_blocks.append(cb)
                    feedback = feedback[byte_unit:] + xor_key[0:byte_unit]

        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename, byte_unit=1):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=32)
        feedback = hs.sha256(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            for i in range(0, len(cb), byte_unit):
                xor_key = Feistel.encrypt(feedback, ext_key)
                pb = by.xor_byte(cb[i:i+byte_unit], xor_key[0:byte_unit])
                plaintext_blocks.append(pb)
                feedback = feedback[byte_unit:] + xor_key[0:byte_unit]
        plaintext = by.merge_bytes(plaintext_blocks)
        plaintext = PCKS5.remove_padding(plaintext)
        return plaintext



class CounterMode():
    @staticmethod
    def encrypt(filedir, ext_key, output_filename):
        plaintext = fl.read_byte(filedir)
        plaintext_blocks = by.generate_slices(plaintext, slice_length=32, check_next_exist=True)
        counter_block = hs.sha256(ext_key)

        ciphertext_blocks = []
        for pb, has_next in plaintext_blocks:
            padding_block = b''
            if not has_next:
                padding_result = PCKS5.insert_padding(pb, 32)
                pb = padding_result[0]
                padding_block = padding_result[1]

            xor_key = Feistel.encrypt(counter_block, ext_key)
            cb = by.xor_byte(xor_key, pb)
            ciphertext_blocks.append(cb)
            counter_block = by.increment(counter_block)

            if padding_block != b'':
                xor_key = Feistel.encrypt(counter_block, ext_key)
                cb = by.xor_byte(xor_key, padding_block)
                ciphertext_blocks.append(cb)
                counter_block = by.increment(counter_block)
        ciphertext = by.merge_bytes(ciphertext_blocks)
        return ciphertext 
    
    @staticmethod
    def decrypt(filedir, ext_key, output_filename):
        ciphertext = fl.read_byte(filedir)
        ciphertext_blocks = by.generate_slices(ciphertext, slice_length=32)
        counter_block = hs.sha256(ext_key)

        plaintext_blocks = []
        for cb in ciphertext_blocks:
            xor_key = Feistel.encrypt(counter_block, ext_key)
            pb = by.xor_byte(xor_key, cb)
            plaintext_blocks.append(pb)
            counter_block = by.increment(counter_block)
        plaintext = by.merge_bytes(plaintext_blocks)
        plaintext = PCKS5.remove_padding(plaintext)
        return plaintext