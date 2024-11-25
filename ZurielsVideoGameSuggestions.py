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

        # Button to get random videogame
        self.get_activity_button = ttk.Button(root, text="Suggest a Video Game", command=self.suggest_random_videogame)
        self.get_activity_button.pack(pady=10)

        # Label to display the videogame
        self.activity_label = ttk.Label(root, text="", font=("Helvetica", 14), wraplength=450, justify="center",
                                        foreground="black", background="#ECE4f2")
        self.activity_label.pack(pady=20)

    def suggest_random_videogame(self):
        # A local list of video games
        videogames = [
            "Grand theft auto 5",
            "Grand Theft Auto: San Andreas",
            "Grand Theft Auto: Vice City",
            "Grand Theft Auto IV",
            "Path of Exile",
            "Path of Exile II",
            "Call of Duty: Black Ops III Zombies",
            "Call of Duty: World at War",
            "Call of Duty: Black Ops",
            "Call of Duty: Modern Warfare 2 (2009)",
            "Call of Duty: Modern Warfare 3 (2011)",
            " Call of Duty: Black Ops II",
            "Forza Horizon 5",
            "Warframe",
            "Age of Empires II: Definitive Edition",
            "For Honor",
            "Assassin's Creed",
            "Assassin's Creed II",
            "Assassin's Creed: Brotherhood",
            "Assassin's Creed: Revelations ",
            "Assassin's Creed III",
            "Far Cry 5",
            "Yakuza 0",
            "NBA 2K Playgrounds 2",
            "Desperados III",
            "Shadow Gambit: The Cursed Crew",
            "Shadow Tactics: Aiko’s Choice",
            "Shadow Tactics: Blades of the Shogun",
            "Dishonored",
            "Dragon's Dogma: Dark Arisen",
            "Mafia: Definitive Edition",
            "Minecraft",
            "League of Legends - Please dont unironically play this",
            "Tetris",
            "Super Smash Bros. Melee",
            "Super Smash Bros. Ultimate",
        ]
