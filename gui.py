# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Project:          Image Encryption & Decryption           #
# Author:           Gavin McClure-Coleman                   #
# File:             gui.py                                  #
# Last Updated:     9/3/2025                                #
# Description:      Simple GUI to make encryption           #
#                   and decryption easier to see            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import tkinter as tk


#TODO: ALL CODE BELOW IS PLACEHOLDER TESTING FOR TKINTER

def button_clicked():
    print("Button clicked!")

def build_gui():
    root = tk.Tk()

    root.geometry('1920x1080')

    # Creating a button with specified options
    button = tk.Button(root, 
                    text="Test", 
                    command=button_clicked,
                    activebackground="blue", 
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=40,
                    wraplength=100)

    button.pack(padx=20, pady=20)

    root.mainloop()