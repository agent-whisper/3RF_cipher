import tkinter as tk
import tkinter.filedialog as tkfd

class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        DEFAULT_PADY = 5

        title = tk.Label(self, text='3Way Cipher', font='none 18 bold')
        title.grid(row=0, column=0, pady=20, sticky=tk.W+tk.E)

        encrypt_button = tk.Button(
            self,
            text='Encrypt',
            command=lambda: master.open_encryption_form()
        )
        encrypt_button.grid(row=1, column=0, pady=DEFAULT_PADY, sticky=tk.W+tk.E)

        decrypt_button = tk.Button(
            self,
            text='Decrypt',
            command=lambda: master.open_decryption_form()
        )
        decrypt_button.grid(row=2, column=0, pady=DEFAULT_PADY, sticky=tk.W+tk.E)

        exit_button = tk.Button(self, text='Keluar', command=master.destroy)
        exit_button.grid(row=3, column=0, pady=DEFAULT_PADY, sticky=tk.W+tk.E)