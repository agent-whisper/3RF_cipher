import tkinter as tk
import tkinter.filedialog as tkfd

class EncryptionForm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        DEFAULT_PADY = 5

        title = tk.Label(self, text='Encrytion', font='none 18 bold')
        title.grid(row=0, column=0, pady=20, sticky=tk.W+tk.E)

        return_button = tk.Button(self, text='Kembali', command=lambda: master.open_main_menu())
        return_button.grid(row=3, column=0, pady=DEFAULT_PADY, sticky=tk.W+tk.E)

class DecryptionForm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        DEFAULT_PADY = 5

        title = tk.Label(self, text='Decryption', font='none 18 bold')
        title.grid(row=0, column=0, pady=20, sticky=tk.W+tk.E)

        return_button = tk.Button(self, text='Kembali', command=lambda: master.open_main_menu())
        return_button.grid(row=3, column=0, pady=DEFAULT_PADY, sticky=tk.W+tk.E)