# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Project:          Image Encryption & Decryption           #
# Author:           Gavin McClure-Coleman                   #
# File:             gui.py                                  #
# Last Updated:     9/3/2025                                #
# Description:      Simple GUI to make image encryption     #
#                   and decryption easier to visualize      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import tkinter as tk
from tkinter import filedialog, OptionMenu, StringVar
from PIL import Image, ImageTk
import numpy as np
from Crypto.Cipher import AES

# TODO: IMPLEMENT MORE CRYPTOGRAPHY FUNCTIONS
# TODO: Make GUI look pretty? (better image scaling, color scheme, etc)

class ImageCryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encrypter & Decrypter")

        self.file_path = ""  # Image file that the user chooses

        # Window
        self.root.geometry('1920x1080')

        # Image Placeholders
        self.original_img = None
        self.encrypted_img = None

        # Buttons (bigger font and padding)
        btn_font = ("Arial", 16)
        btn_width = 20
        btn_height = 2

        self.load_btn = tk.Button(root, text="Load Image", command=self.load_image, font=btn_font, width=btn_width, height=btn_height)
        self.load_btn.pack(pady=20)

        cipher_options = ["XOR", "AES_ECB", "AES_CBC", "(None)"]
        self.selected_cipher = StringVar(value="(None)")
        self.dropdown_menu = OptionMenu(root, self.selected_cipher, *cipher_options)
        self.dropdown_menu.config(font=btn_font, width=btn_width, height=btn_height)
        self.dropdown_menu.pack(pady=20)

        self.encrypt_btn = tk.Button(root, text="Encrypt", command=self.encrypt, state=tk.DISABLED, font=btn_font, width=btn_width, height=btn_height)
        self.encrypt_btn.pack(pady=20)

        self.decrypt_btn = tk.Button(root, text="Decrypt", command=self.decrypt, state=tk.DISABLED, font=btn_font, width=btn_width, height=btn_height)
        self.decrypt_btn.pack(pady=20)

        self.save_img_btn = tk.Button(root, text="Save Image", command=self.save_img, state=tk.DISABLED, font=btn_font, width=btn_width, height=btn_height)
        self.save_img_btn.pack(pady=20)

        # Image Labels
        self.left_img_frame = tk.Frame(root)
        self.left_img_frame.pack(side="left", pady=10)

        self.right_img_frame = tk.Frame(root)
        self.right_img_frame.pack(side="right", pady=10)

        self.left_img_label = tk.Label(self.left_img_frame, text="Original Image")
        self.left_img_label.pack(side="left", padx=10)

        self.right_img_label = tk.Label(self.right_img_frame, text="Encrypted Image")
        self.right_img_label.pack(side="right", padx=10)
        
        # Change keys here for testing
        # AES key section
        self.ecb_key = (b'AAAABBBBCCCCDDDD') # must be 16 bytes (16 characters)
        self.cbc_key = (b'AAAABBBBCCCCDDDD')
        

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
        match cipher:
            case "XOR":
                self.xor()
                self.decrypt_btn.config(state=tk.NORMAL) 
                self.save_img_btn.config(state=tk.NORMAL)
            case "AES_ECB":
                self.AES_ECB_enc()
                self.decrypt_btn.config(state=tk.NORMAL)
                self.save_img_btn.config(state=tk.NORMAL)
            case "AES_CBC":
                self.AES_CBC_enc()
                self.decrypt_btn.config(state=tk.NORMAL)
                self.save_img_btn.config(state=tk.NORMAL)
            case _:
                print(f"Please select an option from the dropdown menu")

    def decrypt(self):
        cipher = self.selected_cipher.get()
        match cipher:
            case "XOR":
                self.xor_dec()
                self.decrypt_btn.config(state=tk.DISABLED) 
                self.save_img_btn.config(state=tk.DISABLED)
            case "AES_ECB":
                self.AES_ECB_dec()
                self.decrypt_btn.config(state=tk.DISABLED)
                self.save_img_btn.config(state=tk.DISABLED)
            case "AES_CBC":
                self.AES_CBC_dec()
                self.decrypt_btn.config(state=tk.DISABLED)
                self.save_img_btn.config(state=tk.DISABLED)
            case _:
                print(f"Please select the same encryption type you used last")

    def save_img(self):
        if self.encrypted_img:
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")])
            if filename:
                self.encrypted_img.save(filename)
        
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

    def AES_ECB_enc(self):
        if self.original_img:
            ecb_key = self.ecb_key
            cipher = AES.new(ecb_key, AES.MODE_ECB)

            arr = np.array(self.original_img)
            shape = arr.shape

            data = arr.tobytes()
            # pad manually with zeros so len(data) % 16 == 0, this is to get the image to be displayable in the GUI
            pad_len = (16 - (len(data) % 16)) % 16
            data += b"\x00" * pad_len

            enc_bytes = cipher.encrypt(data)

            # trim back to original length
            enc_arr = np.frombuffer(enc_bytes[:len(arr.tobytes())], dtype=np.uint8)
            enc_arr = enc_arr.reshape(shape)

            self.encrypted_img = Image.fromarray(enc_arr)
            self.display_enc_image(self.encrypted_img)


    def AES_ECB_dec(self):
        if self.encrypted_img:
            ecb_key = self.ecb_key
            cipher = AES.new(ecb_key, AES.MODE_ECB)

            arr = np.array(self.encrypted_img)
            shape = arr.shape

            data = arr.tobytes()
            pad_len = (16 - (len(data) % 16)) % 16
            data += b"\x00" * pad_len

            dec_bytes = cipher.decrypt(data)

            dec_arr = np.frombuffer(dec_bytes[:len(arr.tobytes())], dtype=np.uint8)
            dec_arr = dec_arr.reshape(shape)

            self.decrypted_img = Image.fromarray(dec_arr)
            self.display_enc_image(self.decrypted_img)


    def AES_CBC_enc(self):
        if self.original_img:
            cbc_key = self.cbc_key
            cipher = AES.new(cbc_key, AES.MODE_CBC)

            arr = np.array(self.original_img)
            shape = arr.shape

            data = arr.tobytes()
            # pad manually with zeros so len(data) % 16 == 0, this is to get the image to be displayable in the GUI
            pad_len = (16 - (len(data) % 16)) % 16
            data += b"\x00" * pad_len

            enc_bytes = cipher.encrypt(data)

            # trim back to original length
            enc_arr = np.frombuffer(enc_bytes[:len(arr.tobytes())], dtype=np.uint8)
            enc_arr = enc_arr.reshape(shape)

            self.encrypted_img = Image.fromarray(enc_arr)
            self.display_enc_image(self.encrypted_img)

    def AES_CBC_dec(self):
        if self.encrypted_img:
            cbc_key = self.cbc_key
            cipher = AES.new(cbc_key, AES.MODE_CBC)

            arr = np.array(self.encrypted_img)
            shape = arr.shape

            data = arr.tobytes()
            pad_len = (16 - (len(data) % 16)) % 16
            data += b"\x00" * pad_len

            dec_bytes = cipher.decrypt(data)

            dec_arr = np.frombuffer(dec_bytes[:len(arr.tobytes())], dtype=np.uint8)
            dec_arr = dec_arr.reshape(shape)

            self.decrypted_img = Image.fromarray(dec_arr)
            self.display_enc_image(self.decrypted_img)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCryptoApp(root)
    root.mainloop()
