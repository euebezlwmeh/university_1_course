from package import values

import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

def tv_func():

    box2 = toga.Box()
    tv_calculate_A_box = toga.Box()
    tv_calculate_C_box = toga.Box()
    calculator2_box = toga.Box()
    tv_box = toga.Box()
    
    tv_calculate_A = toga.Box()
    tv_calculate_C = toga.Box()

    tv_days = toga.TextInput()
    tv_calculate_A = toga.TextInput(readonly=True)
    tv_calculate_C = toga.TextInput(readonly=True)

    tv_label = toga.Label("Кол-во часов исп. ТВ", style=Pack(text_align=RIGHT))
    tv_label_A = toga.Label("Расход энергии для ТВ", style=Pack(text_align=LEFT))
    tv_label_C = toga.Label("Стоим. исп. для ТВ", style=Pack(text_align=LEFT))
    
    def tv(widget):
        try:
            tv_calculate_A.value = values.pTv * (float(tv_days.value))
            tv_calculate_C.value = float(tv_calculate_A.value) * values.tarif
        except ValueError:
            tv_calculate_A.value = "Введите кол-во часов"
            tv_calculate_C.value = "Введите кол-во часов"
            
    tvButton = toga.Button("Calculate", on_press=tv)

    tv_box.add(tv_label)
    tv_box.add(tv_days)
    tv_calculate_A_box.add(tv_label_A)
    tv_calculate_A_box.add(tv_calculate_A)
    tv_calculate_C_box.add(tv_label_C)
    tv_calculate_C_box.add(tv_calculate_C)
    calculator2_box.add(tvButton)

    box2.add(tv_box)
    box2.add(tv_calculate_A_box)
    box2.add(tv_calculate_C_box)
    box2.add(calculator2_box)
    
    box2.style.update(direction=COLUMN, padding=10)
    tv_box.style.update(direction=ROW, padding=5)
    tv_calculate_A_box.style.update(direction=ROW, padding=5)
    tv_calculate_C_box.style.update(direction=ROW, padding=5)
    calculator2_box.style.update(direction=ROW, padding=5)

    return box2
