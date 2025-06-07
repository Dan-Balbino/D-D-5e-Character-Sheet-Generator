from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

from components.character import CharacterSkills


Config.set('graphics', 'width', '700')   # Width
Config.set('graphics', 'height', '800')  # Height

Builder.load_file("ui/character_screen.kv")
Builder.load_file("ui/spells_screen.kv")
Builder.load_file("ui/details_screen.kv")



class Character_GeneratorApp(App):
    a = {"str": ("Athletics",), "dex": ("Acrobatics", "Sleight of hand"), "wis": ("Insight", "Medicine", "Perception")}
    

Character_GeneratorApp().run()
