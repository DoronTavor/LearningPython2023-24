class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle("Tesla", "Model X")
my_car.get_make_model()
my_car.moves()
your_car = Vehicle("Kia", "Picanto")
your_car.get_make_model()
your_car.moves()


# print(my_car.make)
# print(my_car.model)

# Inheritance
class AirPlane(Vehicle):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along..")



class Truck(Vehicle):
    def moves(self):
        print("Rumbles along..")


class GolfCart(Vehicle):
    pass  # Inherit

airbusA380 = AirPlane("Airbus","A380","388")
airbusA380.get_make_model()
airbusA380.moves()

mack =Truck('Mack', 'Pinnacle')
golf_wagon = GolfCart ('Yamaha', 'GC100')
mack.get_make_model()
mack.moves()
golf_wagon.get_make_model()
golf_wagon.moves()

print("\n")

for v in (airbusA380, golf_wagon,my_car,your_car,mack):
    v.get_make_model()
    v.moves()