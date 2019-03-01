import os
import tkinter as tk
import tkinter.filedialog as tkfd

from src.blockcipher.operation.modes import ElectronicCodeBook, CipherFeedback, \
    CipherBlockChaining, OutputFeedback, CounterMode
import src.utilities.hash as hs
import src.utilities.file as fl

class Form(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.AVAILABLE_MODES = {
            'Electronic Code Book' : 'ecb',
            'Cipher Block Chaining' : 'cbc',
            'Cipher Feedback' : 'cfb',
            'Output Feedback' : 'ofb',
            'Counter Mode' : 'cm',
        }
        self.ENCRYPT_OUTPUT = 'ENCRYPT_OUTPUT'
        self.DECRYPT_OUTPUT = 'DECRYPT_OUTPUT'

class EncryptionForm(Form):
    def __init__(self, master):
        Form.__init__(self, master)

        self.cipher_type = 'encrypt'
        title = tk.Label(self, text='Enkripsi', font='none 18 bold')
        title.grid(column=0, columnspan=2, pady=20, sticky=tk.W+tk.E)

        create_input_frame(self, 1, columnspan=2)

        return_button = tk.Button(self, text='Kembali', command=lambda: master.open_main_menu())
        return_button.grid(row=2, column=1, pady=50, sticky=tk.W)
        

class DecryptionForm(Form):
    def __init__(self, master):
        Form.__init__(self, master)
        
        self.cipher_type = 'decrypt'
        title = tk.Label(self, text='Dekripsi', font='none 18 bold')
        title.grid(column=0, columnspan=2, pady=20, sticky=tk.W+tk.E)

        create_input_frame(self, 1, columnspan=2)

        return_button = tk.Button(self, text='Kembali', command=lambda: master.open_main_menu())
        return_button.grid(row=2, column=1, pady=50, sticky=tk.W)


DEFAULT_PADY = 7
def create_input_frame(master, row, column=0, columnspan=1):
    input_frame = tk.Frame(master)
    input_frame.grid(row=row, column=column, columnspan=columnspan, pady=DEFAULT_PADY, sticky=tk.W+tk.E)

    # File selection
    filedir = tk.StringVar()
    filedir.set('')
    tk.Label(master=input_frame, text='Direktori Berkas:').grid(columnspan=2, sticky=tk.W)
    filedir_label = tk.Label(master=input_frame, textvariable=filedir)
    filedir_label.grid(columnspan=2, pady=DEFAULT_PADY, sticky=tk.W)
    pick_file_button = tk.Button(
        master=input_frame,
        text='Pilih Berkas',
        command=lambda: filedir.set(tkfd.askopenfilename()),
    )
    pick_file_button.grid(column=0, sticky=tk.W)

    # Key entry
    key_label = tk.Label(master=input_frame, text='Key:')
    key_label.grid(row=5, pady=DEFAULT_PADY, sticky=tk.W)
    key_entry = tk.Entry(master=input_frame)
    key_entry.grid(row=5, pady=DEFAULT_PADY, column=1)

    # Output filename entry
    output_filename = tk.Label(master=input_frame, text='Nama Berkas Keluaran:')
    output_filename.grid(row=6, pady=DEFAULT_PADY, sticky=tk.W)
    output_filename_entry = tk.Entry(master=input_frame)
    output_filename_entry.grid(row=6, pady=DEFAULT_PADY, column=1)

    # Operation mode selection
    operation_mode = tk.StringVar()
    operation_mode.set('')
    op_mode_label = tk.Label(master=input_frame, text='Mode Operasi:')
    op_mode_label.grid(columnspan=2, pady=5, sticky=tk.W)
    for label in master.AVAILABLE_MODES:
        rb = tk.Radiobutton(
            master=input_frame,
            text=label,
            variable=operation_mode,
            value=master.AVAILABLE_MODES[label],
        )
        rb.grid(column=0, sticky=tk.W)
    
    if master.cipher_type == 'encrypt':
        execute_button = tk.Button(master, text='Mulai Enkripsi', \
            command=lambda: encrypt(filedir.get(), key_entry.get(), \
                '{}/{}'.format(master.ENCRYPT_OUTPUT, output_filename_entry.get()), operation_mode.get()))
    else:
        execute_button = tk.Button(master, text='Mulai Dekripsi', \
            command=lambda: decrypt(filedir.get(), key_entry.get(), \
                '{}/{}'.format(master.DECRYPT_OUTPUT, output_filename_entry.get()), operation_mode.get()))
    execute_button.grid(column=0, padx=30, pady=50, sticky=tk.W)
    
def encrypt(filedir, key, output_dir, op_mode):
    if check_form_complete(filedir, key, output_dir, op_mode):
        print('=== Starting Encryption ===')
        hashed_key = hs.sha256(key)
        print_user_input(filedir, key, hashed_key, output_dir, op_mode)

        ciphertext = bytes('', 'utf-8')
        if op_mode == 'ecb':
            ciphertext = ElectronicCodeBook.encrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'cbc':
            ciphertext = CipherBlockChaining.encrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'cfb':
            pass
            ciphertext = CipherFeedback.encrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'ofb':
            pass
            ciphertext = OutputFeedback.encrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'cm':
            pass
            # ciphertext = CounterMode.encrypt(filedir, hashed_key, output_dir)
        
        output_folder = output_dir.split('/')[:-1]
        output_folder = '/'.join(output_folder)
        fl.create_folder(output_folder)
        fl.write_byte(ciphertext, output_dir)
        print('=== Finished with filesize: {} ==='.format(len(ciphertext)))

def decrypt(filedir, key, output_dir, op_mode):
    if check_form_complete(filedir, key, output_dir, op_mode):
        print('=== Starting Decrytion ===')
        hashed_key = hs.sha256(key)
        print_user_input(filedir, key, hashed_key, output_dir, op_mode)

        plaintext = bytes('', 'utf-8')
        if op_mode == 'ecb':
            plaintext = ElectronicCodeBook.decrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'cbc':
            plaintext = CipherBlockChaining.decrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'cfb':
            pass
            plaintext = CipherFeedback.decrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'ofb':
            pass
            plaintext =  OutputFeedback.decrypt(filedir, hashed_key, output_dir)
        elif op_mode == 'cm':
            pass
            # plaintext =  CounterMode.decrypt(filedir, hashed_key, output_dir)

        output_folder = output_dir.split('/')[:-1]
        output_folder = '/'.join(output_folder)
        fl.create_folder(output_folder)
        fl.write_byte(plaintext, output_dir)
        print('=== Finished with filesize: {} ==='.format(len(plaintext)))

def print_user_input(filedir, key, hashed_key, output_filename, op_mode):
    print('File Directory: {}'.format(filedir))
    print('Key: {}'.format(key))
    print('Hashed Key: {}'.format(hashed_key))
    print('Output Filename: {}'.format(output_filename))
    print('Operation Mode: {}'.format(op_mode))

def check_form_complete(filedir, key, output_filename, op_mode):
    is_valid = (filedir != '' and key != '' \
        and output_filename != '' and op_mode != '')
    if not is_valid:
        print('Ada field yang kosong; Periksa lagi')
    return is_valid