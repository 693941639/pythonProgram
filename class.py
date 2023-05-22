from typing import Any


class Tea:
    name = None
    water = 0
    temperature = None

    def add_water(self, water):
        self.water = water


class LvTea(Tea):
    name = "Lv Tea"

    def add_water(self, water):
        super().add_water(water)
        print("Lv tea add water")

    @classmethod
    def show(cls):
        cls.name
        print("LvTea class name", cls.name)

    @staticmethod
    def say():
        print("Say what")
    
    @property
    def curr_temperature(self):
        if self.water > 0:
            return 50
        else:
            return 0
        
    @curr_temperature.setter
    def curr_temperature(self, val):
        self.temperature = val

    # @staticmethod
    def __call__(self):
        print("LvTea __call__")

lv_tea = LvTea()
# lv_tea.add_water(100)
# print(lv_tea.name, lv_tea.water, lv_tea.temperature)
# LvTea.show()
# LvTea.say()

# print(dir(LvTea))

# print(dir(LvTea()))

lv_tea()


