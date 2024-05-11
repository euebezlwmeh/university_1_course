from package import values

import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

def vashingmachine_func():

    box3 = toga.Box()
    vashingmachine_calculate_A_box = toga.Box()
    vashingmachine_calculate_C_box = toga.Box()
    calculator3_box = toga.Box()

    vashingmachine_box = toga.Box()
    vashingmachine_calculate_A = toga.Box()
    vashingmachine_calculate_C = toga.Box()

    vashingmachine_days = toga.TextInput()
    vashingmachine_calculate_A = toga.TextInput(readonly=True)
    vashingmachine_calculate_C = toga.TextInput(readonly=True)

    vashingmachine_label = toga.Label("Кол-во часов исп. стиральной машины", style=Pack(text_align=RIGHT))
    vashingmachine_label_A = toga.Label("Расход энергии для стиральной машины", style=Pack(text_align=LEFT))
    vashingmachine_label_C = toga.Label("Стоим. использ. для стиральной машины", style=Pack(text_align=LEFT))
    
    def vashingmachine(widget):
        try:
            vashingmachine_calculate_A.value = values.pVashingMachine * (float(vashingmachine_days.value))
            vashingmachine_calculate_C.value = float(vashingmachine_calculate_A.value) * values.tarif
        except ValueError:
            vashingmachine_calculate_A.value = "Введите кол-во часов"
            vashingmachine_calculate_C.value = "Введите кол-во часов"

    vashingmachineButton = toga.Button("Calculate", on_press=vashingmachine)

    vashingmachine_box.add(vashingmachine_label)
    vashingmachine_box.add(vashingmachine_days)
    vashingmachine_calculate_A_box.add(vashingmachine_label_A)
    vashingmachine_calculate_A_box.add(vashingmachine_calculate_A)
    vashingmachine_calculate_C_box.add(vashingmachine_label_C)
    vashingmachine_calculate_C_box.add(vashingmachine_calculate_C)
    calculator3_box.add(vashingmachineButton)

    box3.add(vashingmachine_box)
    box3.add(vashingmachine_calculate_A_box)
    box3.add(vashingmachine_calculate_C_box)
    box3.add(calculator3_box)
    
    box3.style.update(direction=COLUMN, padding=10)
    vashingmachine_box.style.update(direction=ROW, padding=5)
    vashingmachine_calculate_A_box.style.update(direction=ROW, padding=5)
    vashingmachine_calculate_C_box.style.update(direction=ROW, padding=5)
    calculator3_box.style.update(direction=ROW, padding=5)

    return box3
