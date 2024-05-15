from folder import electrodevices, calculation, docx_save
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Box:
    def __init__(self, label: str, interactionWindow: float):
        self.label = label
        self.interactionWindow = interactionWindow

class myApp(App):

    def btnPress(self):
        
        docx_save.docx_save(electrodevices.iron.name, calculation.Calc.hours, calculation.Electricity, calculation.Coast)

    def build(self):
        box = BoxLayout()

        hoursInput = TextInput()
        hoursBox = Box("Введите количество часов", hoursInput)
        # return super().build()
    
if __name__ == "__main__":
    myApp().run()