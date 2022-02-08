#  1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


#  2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f'Bus contains {self.capacity} seats.')


my_bus = Bus(60, 100, 30)

#  3
print(type(my_bus))

#  4
print(isinstance(my_bus, Vehicle))


#  5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


#  6
class SchoolBus(School, Bus):
    def __init__(self, bus_school_color, get_school_id, number_of_students,
                 seating_capacity, max_speed, mileage):
        Bus.__init__(self, seating_capacity, max_speed, mileage)
        School.__init__(self, get_school_id, number_of_students)
        self.bus_school_color = bus_school_color

    def print_bus_school_color(self):
        print(f'School bus is {self.bus_school_color}')


s_bus = SchoolBus('white', 100, 30, 30, 60, 5)
s_bus.print_bus_school_color()


#  7
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (f'Bear make sound like {self.sound}!')


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (f'Wolf make sound like {self.sound}!')


beear = Bear('Rrrrrr')
woolf = Wolf('Uuuuuuuu')
animals = (beear, woolf)

for animal_sound in animals:
    print(animal_sound.make_sound())


#  8
# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#     def check_population(self):
#         if self.population > 1500:
#             return self.population
#         else:
#             return (f'Your city {self.name} is too small')
#
#
# Lutsk = City('Lutsk', 50000)
# Pryvitne = City('Pryvitne', 1000)
# all_cities = (Lutsk, Pryvitne)
#
# for i in all_cities:
#     print(i.check_population())