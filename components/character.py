from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import DictProperty, NumericProperty
from kivy.clock import Clock


class Skill(GridLayout):
    # Create each skill individually, and assign it its properties
    attr_mods = DictProperty()
    proef_mod = NumericProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.skill_attr = None
        self.is_checked = False


    def create_skill(self, attr=None, skill_name=None, modifier=None):
        self.skill_attr = attr
        
        self.ids.cbox.bind(active=self.on_checkbox_active)
        
        if skill_name:
            self.ids.skill_name.text = skill_name
        if modifier is not None:
            self.ids.modifier.text = str(modifier)
            

    def update_skill(self):
        if not self.skill_attr or not self.attr_mods:
            return
        
        total = self.attr_mods.get(self.skill_attr, 0)
        
        if self.is_checked:
            total += self.proef_mod
        
        if self.ids.modifier.text == str(total):
            return
        
        self.ids.modifier.text = str(total)


    def on_checkbox_active(self, checkbox, value):
        self.is_checked = value
        self.update_skill()
        
        
    def on_attr_mods(self, instance, value):
        self.update_skill()


    def on_proef_mod(self, instance, value):
        self.update_skill()
        
        
class CharacterSkills(BoxLayout):
    # Creates a list of skills on the sheet, which is updated dynamically
    attr_skills = DictProperty()
    attr_mods = DictProperty()
    proef_mod = NumericProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        Clock.schedule_once(self._finish_setup)


    def _finish_setup(self, dt):
        self.create_skill_group()


    def create_skill_group(self):
        skills_set = Label(
            text="Skills",
            font_size="15dp",
            size_hint_y=None,
            height=30
        )
        self.add_widget(skills_set)

        for attribute, skills in self.attr_skills.items():
            attr_label = Label(
                text=f"{attribute.upper()}",
                font_size="15dp",
                size_hint_y=None,
                padding=(0, 45, 0, 10),
                height=30
            )
            self.add_widget(attr_label)

            skills_grid = GridLayout(
                cols=1,
                spacing=5,
                size_hint_y=None,
                row_default_height=30,
                row_force_default=True,
                padding=(0, 10, 0, 0)
            )
            skills_grid.bind(minimum_height=skills_grid.setter('height'))

            for skill in skills:
                skill_widget = Skill()

                # Adia a criação real da skill para o próximo frame, assim como na classe A
                def setup_skill(dt, widget=skill_widget, attr=attribute, skill_name=skill):
                    widget.attr_mods = self.attr_mods
                    widget.proef_mod = self.proef_mod
                    widget.create_skill(attr=attr, skill_name=skill_name, modifier=self.attr_mods.get(attr, 0))

                Clock.schedule_once(setup_skill)

                # Bindings para manter sincronizado
                self.bind(attr_mods=lambda inst, val, w=skill_widget: setattr(w, 'attr_mods', val))
                self.bind(proef_mod=lambda inst, val, w=skill_widget: setattr(w, 'proef_mod', val))

                skills_grid.add_widget(skill_widget)

            self.add_widget(skills_grid)

            blank_space = Label(size_hint_y=None, height=10)
            self.add_widget(blank_space)
            
            
            