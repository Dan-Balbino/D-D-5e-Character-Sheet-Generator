from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import DictProperty


class CharacterSkills(BoxLayout):
    attr_skills = DictProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.bind(attr_skills=self.on_attr_skills)


    def on_attr_skills(self, instance, value):
        self.clear_widgets()
        self.create_skill_group()


    def create_skill_group(self):
        for attribute, skills in self.attr_skills.items():
            grid_layout = GridLayout(cols=3)

            for skill in skills:
                checkbox = CheckBox()
                checkbox.bind(active=self.on_checkbox_active)

                attribute_mod = Label(text="1")

                skill_name = Label(text=skill)

                grid_layout.add_widget(checkbox)
                grid_layout.add_widget(attribute_mod)
                grid_layout.add_widget(skill_name)

            self.add_widget(grid_layout)


    def on_checkbox_active(self, checkbox, value):
        print("Checkbox clicado:", value)






# class MyApp(App):
#     def build(self):
#         return CharacterSkills(a)

# if __name__ == '__main__':
#     MyApp().run()
