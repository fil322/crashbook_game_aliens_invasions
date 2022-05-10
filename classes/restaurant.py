class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print('Restaurant is open')

# restaurant = Restaurant('Duna', 'Seafood')

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors.split()

    def show_flavors(self):
        print(* self.flavors)

icecreamstand = IceCreamStand('ICE', 'icecream', 'chocolote vanila strawberry mango')
icecreamstand.show_flavors()

