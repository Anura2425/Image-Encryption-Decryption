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

# TODO: 

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
        self.load_btn.pack(pady=5)

        cipher_options = ["xor", "Test"]
        self.selected_cipher = StringVar(value="xor")
        self.dropdown_menu = OptionMenu(root, self.selected_cipher, *cipher_options).pack(pady=5)

        self.encrypt_btn = tk.Button(root, text="Encrypt", command=self.select_cipher, state=tk.DISABLED)
        self.encrypt_btn.pack(pady=5)


        # Image Labels
        self.img_frame = tk.Frame(root)
        self.img_frame.pack(pady=10)

        self.left_img_label = tk.Label(self.img_frame, text="Original Image")
        self.left_img_label.pack(side="left", padx=10)

        self.right_img_label = tk.Label(self.img_frame, text="Encrypted Image")
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
        
    def select_cipher(self):
        cipher = self.selected_cipher.get()
        if cipher == "xor":
            self.xor()
        else:
            print(f"No cipher implemented yet for: {cipher}")


    def xor(self):
        # This is just a test function to test applying operations to images
        if self.original_img:
            arr = np.array(self.original_img)
            xor_arr = arr ^ 127
            self.encrypted_img = Image.fromarray(xor_arr)
            self.display_image(self.encrypted_img)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCryptoApp(root)
    root.mainloop()
