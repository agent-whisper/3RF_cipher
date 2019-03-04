class PCKS5():
    @staticmethod
    def insert_padding(datablock, target_len):
        required_pad_count = target_len - len(datablock)
        if required_pad_count > 0:
            padding = bytes([required_pad_count]) * required_pad_count
            return [(datablock + padding), True]
        elif (required_pad_count == 0):
            padding = bytes([target_len]) * target_len
            return [datablock, padding, True]
        else:
            return [datablock, False]

    @staticmethod
    def remove_padding(complete_data):
        datablock_len = len(complete_data)
        padding_count = complete_data[-1:][0]
        if (padding_count < datablock_len and padding_count > 0):
            for i in range(0, padding_count):
                if (complete_data[datablock_len-i-1] != padding_count):
                    return complete_data
            return complete_data[:-1*padding_count]
        else:
            return complete_data
        