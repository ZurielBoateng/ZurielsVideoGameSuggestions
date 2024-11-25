import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random


class ZurielsVideoGameSuggestions:
    def __init__(self, root):
        self.root = root
        self.root.title("Zuriel's Video Game Suggestions")
        self.root.geometry("500x500")
        self.root.configure(bg="#ECE4f2")

        # Title label
        self.title_label = ttk.Label(root, text="Want to play something fun?", font=("Helvetica", 24, "bold"),
                                     foreground="#3AC5C7", background="#ECE4f2")
        self.title_label.pack(pady=20)

        # Button to get random activity
        self.get_activity_button = ttk.Button(root, text="Suggest a Video Game", command=self.suggest_random_videogame)
        self.get_activity_button.pack(pady=10)

        # Label to display the activity
        self.activity_label = ttk.Label(root, text="", font=("Helvetica", 14), wraplength=450, justify="center",
                                        foreground="black", background="#ECE4f2")
        self.activity_label.pack(pady=20)
