class Marik():
    def __init__(self, super_name='', super_power='', super_time_save_world=''):
        self.super_name = super_name
        self.super_power = super_power
        self.super_time_save_world = super_time_save_world

    def printe(self):
        return print(self.super_name, self.super_power, self.super_time_save_world)

m = Marik()
m.printe()
