from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import DictProperty


class CharacterSkills(BoxLayout):
    """
    This class organizes skills categorized by attributes, displaying them in groups
    with checkboxes for user interaction.

    Attributes:

        attr_skills (DictProperty): Dictionary with attributes as keys
            and list of skills as values. Example:
            {
                "strength": ["Athletics"],
                "intelligence": ["Investigation", "History"]
            }

    Methods:
    --------
        on_attr_skills(instance, value)
            Updates the interface when the skill dictionary is modified.
        create_skill_group()
            Creates the labels and checkboxes widgets for each skill group.
        on_checkbox_active(checkbox, value)
            Event fired when a checkbox is clicked.
    """
    
    attr_skills = DictProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        self.bind(attr_skills=self.on_attr_skills)

    def on_attr_skills(self, instance, value):
        self.clear_widgets()
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
                padding = (0, 45, 0, 10),
                height=30
            )
            self.add_widget(attr_label)

            skills_grid = GridLayout(
                cols=3,
                spacing=5,
                size_hint_y=None,
                row_default_height=30,
                row_force_default=True,
                padding = (0, 10, 0, 0)
            )
            skills_grid.bind(minimum_height=skills_grid.setter('height'))

            for skill in skills:
                checkbox = CheckBox(size_hint=(None, None), size=(20, 20))
                checkbox.bind(active=self.on_checkbox_active)
                
                label_mod = Label(text="1", font_size="13dp", size_hint=(None, 1))
                label_skill = Label(text=skill, 
                                    font_size="13dp",
                                    text_size = self.size,
                                    halign = "left",
                                    valign = "middle",
                                    size_hint=(None, 1)
                )

                skills_grid.add_widget(checkbox)
                skills_grid.add_widget(label_mod)
                skills_grid.add_widget(label_skill)

            self.add_widget(skills_grid)

    def on_checkbox_active(self, checkbox, value):
        print("Checkbox clicado:", value)
