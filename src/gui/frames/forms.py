import tkinter as tk
import tkinter.filedialog as tkfd

class EncryptionForm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=800)
        DEFAULT_PADY = 5
        self.filedir = tk.StringVar()
        self.filedir.set('')

        title = tk.Label(self, text='Encrytion', font='none 18 bold')
        title.grid(column=0, columnspan=2, pady=20, sticky=tk.W+tk.E)

        create_input_frame(self, 1, columnspan=2)

        return_button = tk.Button(self, text='Kembali', command=lambda: master.open_main_menu())
        return_button.grid(column=0, pady=50, sticky=tk.W)

class DecryptionForm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        DEFAULT_PADY = 5
        self.filedir = tk.StringVar()
        self.filedir.set('')
        
        title = tk.Label(self, text='Decryption', font='none 18 bold')
        title.grid(column=0, columnspan=2, pady=20, sticky=tk.W+tk.E)

        create_input_frame(self, 1, columnspan=2)

        return_button = tk.Button(self, text='Kembali', command=lambda: master.open_main_menu())
        return_button.grid(column=0, pady=50, sticky=tk.W)

def create_input_frame(master, row, column=0, columnspan=1):
    input_frame = tk.Frame(master)
    input_frame.grid(row=row, column=column, columnspan=columnspan, sticky=tk.W+tk.E)

    tk.Label(master=master, text='Direktori Berkas:').grid(columnspan=2, sticky=tk.W)
    filedir_label = tk.Label(master=master, textvariable=master.filedir)
    filedir_label.grid(columnspan=2, sticky=tk.W)
    pick_file = tk.Button(
        master=master,
        text='Pilih Berkas',
        command=lambda: master.filedir.set(tkfd.askopenfilename()),
    )
    pick_file.grid(column=0, sticky=tk.W)