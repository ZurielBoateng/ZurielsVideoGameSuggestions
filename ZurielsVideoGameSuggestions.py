import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


class ZurielsVideoGameSuggestions:
    def __init__(self, root):
        self.root = root
        self.root.title("Zuriel's Video Game Suggestions")
        self.root.geometry("500x600")
        self.root.configure(bg="#ECE4f2")

        # Title label
        self.title_label = ttk.Label(root, text="Want to play something fun?", font=("Helvetica", 25, "bold"),
                                     foreground="#3AC5C7", background="#ECE4f2")
        self.title_label.pack(pady=20)

        # Button to get random video game
        self.get_activity_button = ttk.Button(root, text="Suggest a Video Game", command=self.suggest_random_videogame)
        self.get_activity_button.pack(pady=10)

        # Label to display the video game
        self.activity_label = ttk.Label(root, text="", font=("Helvetica", 14), wraplength=450, justify="center",
                                        foreground="black", background="#ECE4f2")
        self.activity_label.pack(pady=20)

        # Label to display the iamge
        self.image_label = tk.Label(root, bg="#ECE4f2")
        self.image_label.pack(pady=20)

    def suggest_random_videogame(self):
        # A local list of video games
        videogames = {
            "Grand theft auto 5": "images/Gta5.jpg",
            "Grand Theft Auto: San Andreas": "images/Gtasa.jpg",
            "Grand Theft Auto: Vice City": "images/Gtavc.jpg",
            "Grand Theft Auto IV": "images/Gtaiv.jpg",
            "Path of Exile": "images/poe.jpg",
            "Path of Exile II": "images/poe2.jpg",
            "Call of Duty: Black Ops III Zombies": "images/codbo3z.jpg",
            "Call of Duty: World at War": "images/codwaw.jpg",
            "Call of Duty: Black Ops": "images/codbo.jpg",
            "Call of Duty: Modern Warfare 2 (2009)": "images/codmw2.jpg",
            "Call of Duty: Modern Warfare 3 (2011)": "images/codmw3.jpg",
            "Call of Duty: Black Ops II": "images/codbo2.jpg",
            "Forza Horizon 5": "images/fh5.jpg",
            "Warframe": "images/warframe.jpg",
            "Age of Empires II: Definitive Edition": "images/aoe2de.jpg",
            "For Honor": "images/fh.jpg",
            "Assassin's Creed": "images/ac.jpg",
            "Assassin's Creed II": "images/ac2.jpg",
            "Assassin's Creed: Brotherhood": "images/acbh.jpg",
            "Assassin's Creed: Revelations ": "images/acr.jpg",
            "Assassin's Creed III": "images/ac3.jpg",
            "Far Cry 3": "images/fc3.jpg",
            "Far Cry 5": "images/fc5.jpg",
            "Yakuza 0": "images/y0.jpg",
            "NBA 2K Playgrounds 2": "images/nba2kpg2.jpg",
            "Desperados III": "images/d3.jpg",
            "Shadow Gambit: The Cursed Crew": "images/sgtcc.jpg",
            "Shadow Tactics: Aiko’s Choice": "images/stac.jpg",
            "Shadow Tactics: Blades of the Shogun": "images/stbots.jpg",
            "Dishonored": "images/dishonored.jpg",
            "Dragon's Dogma: Dark Arisen": "images/ddda.jpg",
            "Mafia: Definitive Edition": "images/mde.jpg",
            "Minecraft": "images/minecraft.jpg",
            "League of Legends - Please dont unironically play this": "images/lol.jpg",
            "Tetris": "images/tetris.jpg",
            "Super Smash Bros. Melee": "images/ssbm.jpg",
            "Super Smash Bros. Ultimate": "images/ssbu.jpg",
        }

        # Choose a random video game
        videogame = random.choice(list(videogames.keys()))

        # Display the video game
        self.activity_label.config(text=f"You should try: {videogame}")

        # Load image
        from PIL import Image
        image_path = videogames[videogame]
        image = Image.open(image_path)
        image = image.resize((300, 370), Image.Resampling.LANCZOS)  # Resize to fit the GUI
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to avoid poor collection

# Create the main application window
root = tk.Tk()
app = ZurielsVideoGameSuggestions(root)
root.mainloop()
