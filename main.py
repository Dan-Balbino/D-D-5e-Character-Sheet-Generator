from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

from kivy.properties import DictProperty, NumericProperty

from components.character import CharacterSkills


Config.set('graphics', 'width', '700')   # Width
Config.set('graphics', 'height', '800')  # Height

Builder.load_file("ui/character_screen.kv")
Builder.load_file("ui/spells_screen.kv")
Builder.load_file("ui/details_screen.kv")


class Character_GeneratorApp(App):
    attr_mods = DictProperty({
        'str': 1, 
        'dex': 2, 
        'con': -1,
        'int': 1,
        'wis': 0,
        'char': 1
    })
    proef_mod = NumericProperty(3)

    def a(self):
        for chave in self.attr_mods:
            self.attr_mods[chave] += 1
        self.attr_mods = self.attr_mods.copy()  # dispara evento

    def b(self):
        self.proef_mod += 1

    
    ab = {"str": ("Athletics",), 
         "dex": ("Acrobatics", "Sleight of hand", "Stealth"), 
         "con": ("Endurance",),
         "int": ("Arcana", "History", "Investigation", "Nature", "Religion"),
         "wis": ("Animal handling", "Insight", "Medicine", "Perception", "Survival"),
         "char": ("Deception", "Intimidation", "Performance", "Persuasion")}





Character_GeneratorApp().run()
