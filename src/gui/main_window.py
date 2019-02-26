import tkinter as tk

from src.gui.frames.forms import EncryptionForm, DecryptionForm
from src.gui.frames.main_menu import MainMenu

class MainWindows(tk.Tk):
    def __init__(self, title='window', width='800', height='600', resizable=True):
        tk.Tk.__init__(self)
        self.title('Tugas Besar 1')
        window_width = str(width)
        window_height= str(height)
        self.geometry('{}x{}'.format(window_width,window_height))

        self._frame = None
        self.open_main_menu()
    
    def open_new_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relx=0.5, y=48, anchor=tk.N)
    
    def open_main_menu(self):
        self.open_new_frame(MainMenu)
    
    def open_encryption_form(self):
        self.open_new_frame(EncryptionForm)

    def open_decryption_form(self):
        self.open_new_frame(DecryptionForm)
