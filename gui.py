# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Project:          Image Encryption & Decryption           #
# Author:           Gavin McClure-Coleman                   #
# File:             gui.py                                  #
# Last Updated:     9/3/2025                                #
# Description:      Simple GUI to make encryption           #
#                   and decryption easier to see            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import tkinter as tk
from tkinter import filedialog, OptionMenu, StringVar
from PIL import Image, ImageTk
import numpy as np
from cryptography import fernet

# TODO: IMPLEMENT CRYPTOGRAPHY FUNCTIONS
# TODO: IMPLEMENT ENCRYPTED IMAGE SAVE, SO I CAN DECRYPT IT

class ImageCryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encrypter & Decrypter")

        self.file_path = ""  # Image file that the user chooses

        # Window
        self.root.geometry('1024x768')

        # Image Placeholders
        self.original_img = None
        self.encrypted_img= None

        # Buttons
        self.load_btn = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=20)

        cipher_options = ["xor", "Test"]
        self.selected_cipher = StringVar(value="xor")
        self.dropdown_menu = OptionMenu(root, self.selected_cipher, *cipher_options).pack(pady=20)

        self.encrypt_btn = tk.Button(root, text="Encrypt", command=self.encrypt, state=tk.DISABLED)
        self.encrypt_btn.pack(pady=20)

        self.decrypt_btn = tk.Button(root, text="Decrypt", command=self.decrypt, state=tk.DISABLED)
        self.decrypt_btn.pack(pady=20)


        # Image Labels
        self.left_img_frame = tk.Frame(root)
        self.left_img_frame.pack(side="left", pady=10)

        self.right_img_frame = tk.Frame(root)
        self.right_img_frame.pack(side="right", pady=10)

        self.left_img_label = tk.Label(self.left_img_frame, text="Original Image")
        self.left_img_label.pack(side="left", padx=10)

        self.right_img_label = tk.Label(self.right_img_frame, text="Encrypted Image")
        self.right_img_label.pack(side="right", padx=10)


    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg"), ("All files", "*.*")])
        if filepath:
            self.original_img = Image.open(filepath).convert("RGB")
            self.display_image(self.original_img)
            self.encrypt_btn.config(state=tk.NORMAL)

    def display_image(self, img):
        resized_img = img.copy()
        resized_img.thumbnail((400, 400))
        tk_img = ImageTk.PhotoImage(resized_img)
        self.left_img_label.config(image=tk_img)
        self.left_img_label.image = tk_img 

    def display_enc_image(self, img):
        resized_img = img.copy()
        resized_img.thumbnail((400, 400))
        tk_img = ImageTk.PhotoImage(resized_img)
        self.right_img_label.config(image=tk_img)
        self.right_img_label.image = tk_img
        
    def encrypt(self):
        cipher = self.selected_cipher.get()
        if cipher == "xor":
            self.xor()
            self.decrypt_btn.config(state=tk.NORMAL) 
        else:
            print(f"Please select an option from the dropdown menu")

    def decrypt(self):
        cipher = self.selected_cipher.get()
        if cipher == "xor":
            self.xor_dec()
            self.decrypt_btn.config(state=tk.DISABLED) 
        else:
            print(f"Please select the same encryption type you used last")
        
    def xor(self):
        # This is just a test function to test applying operations to images
        if self.original_img:
            arr = np.array(self.original_img)
            xor_arr = arr ^ 127
            self.encrypted_img = Image.fromarray(xor_arr)
            self.display_enc_image(self.encrypted_img)

    def xor_dec(self):
        # This is just a test function to test applying operations to images
        if self.encrypted_img:
            arr = np.array(self.encrypted_img)
            xor_arr = arr ^ 127
            self.decrypted_img = Image.fromarray(xor_arr)
            self.display_enc_image(self.decrypted_img)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCryptoApp(root)
    root.mainloop()
