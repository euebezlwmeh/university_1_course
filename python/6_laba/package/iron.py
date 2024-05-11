from package import values

import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

def iron_func():

    box1 = toga.Box()
    iron_calculate_A_box = toga.Box()
    iron_calculate_C_box = toga.Box()
    calculator1_box = toga.Box()

    iron_box = toga.Box()
    iron_calculate_A = toga.Box()
    iron_calculate_C = toga.Box()

    iron_days = toga.TextInput()
    iron_calculate_A = toga.TextInput(readonly=True)
    iron_calculate_C = toga.TextInput(readonly=True)

    iron_label = toga.Label("Кол-во часов исп. утюга", style=Pack(text_align=RIGHT))
    iron_label_A = toga.Label("Расход энергии для утюга", style=Pack(text_align=LEFT))
    iron_label_C = toga.Label("Стоим. исп. для утюга", style=Pack(text_align=LEFT))
    
    def iron(widget):
        try:
            iron_calculate_A.value = values.pIron * (float(iron_days.value))
            iron_calculate_C.value = float(iron_calculate_A.value) * values.tarif
        except ValueError:
            iron_calculate_A.value = "Введите кол-во часов"
            iron_calculate_C.value = "Введите кол-во часов"
            
    ironButton = toga.Button("Calculate", on_press=iron)

    iron_box.add(iron_label)
    iron_box.add(iron_days)
    iron_calculate_A_box.add(iron_label_A)
    iron_calculate_A_box.add(iron_calculate_A)
    iron_calculate_C_box.add(iron_label_C)
    iron_calculate_C_box.add(iron_calculate_C)
    calculator1_box.add(ironButton)

    box1.add(iron_box)
    box1.add(iron_calculate_A_box)
    box1.add(iron_calculate_C_box)
    box1.add(calculator1_box)
    
    box1.style.update(direction=COLUMN, padding=10)
    iron_box.style.update(direction=ROW, padding=5)
    iron_calculate_A_box.style.update(direction=ROW, padding=5)
    iron_calculate_C_box.style.update(direction=ROW, padding=5)
    calculator1_box.style.update(direction=ROW, padding=5)

    return box1
