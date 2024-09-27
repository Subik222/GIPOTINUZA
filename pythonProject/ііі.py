class Marik:
    def __init__(self, super_name='', super_power='', super_time_save_world=0):
        self.super_name = super_name
        self.super_power = super_power
        self.super_time_save_world = super_time_save_world

    def printe(self):
        """Виведення інформації про ТЦК"""
        return print(f"Воєнком: {self.super_name}, Суперсила: {self.super_power}, Кількість мобілізованих: {self.super_time_save_world}")
