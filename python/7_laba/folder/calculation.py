from folder import gui, electrodevices

class Calculation:
    tariff = 4
    def __init__(self, power: float, hours: float):
        self.power = power
        self.hours = hours

    def electricity(self):
        return self.power * self.hours
    
    def coast(self):
        return self.tariff * self.power * self.hours
    
    def __str__(self):
        return f"Расход электричества: {self.electricity()}, стоимость: {self.coast()}"

Calc = Calculation(electrodevices.iron.power, 5)
Electricity = Calc.electricity()
Coast = Calc.coast()

print(Calc)