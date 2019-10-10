# TODO: Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km


class Taxi(Prius):

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0
