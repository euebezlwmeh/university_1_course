#Расход электроэнергии (кВт.ч) = мощность (кВт) × время использования (ч) (A)
#Стоимость использования прибора за период = расход электроэнергии х тариф (C)

from package import iron, tv, vashingmachine
import toga
from toga.style.pack import COLUMN

def build(app):
    box = toga.Box()
    box.add(iron.iron_func())
    box.add(tv.tv_func())
    box.add(vashingmachine.vashingmachine_func())
    box.style.update(direction=COLUMN, padding=10)
    return box

def main():
    return toga.App("6_laba", "6_laba", startup=build)

if __name__ == "__main__":
    main().main_loop()
