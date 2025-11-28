from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Base class for all vehicles"""
    def __init__(self, compact:bool, regular:bool):
        self.compact = compact
        self.regular = regular


class ParkingSpot:
    """Class representing a parking spot"""
    def __init__(self, spot_id, spot_type):
        self.id = spot_id
        self.type = spot_type
        self.is_occupied = False
        self.vehicle = None

class ParkingLot:
    """Class for managing the parking lot"""
    def __init__(self):
        self.spots = []
    
    def add_parking_spot(self, spot_type, spot_id):
        """Add a parking spot to the lot"""
        pass
    
    def park(self, vehicle):
        """Park a vehicle in the lot"""
        pass
    
    def get_available_spots(self):
        """Get count of available spots by type"""
        pass


class Motorbike():
    def __init__(self, compact:int, regular:int):
        self.compact = compact
        self.regular = regular


class Car():
    def __init__(self, compact:int):
        self.compact = compact


# TESTS
# Create a parking lot
lot = ParkingLot()
lot.add_parking_spot("Compact", 1)
lot.add_parking_spot("Regular", 2)
lot.add_parking_spot("Regular", 3)

# Create vehicles
motorbike = Motorbike(compact=1, spot=2)
car = Car()

# Test 1: Initial state
assert lot.get_available_spots() == {'Compact': 1, 'Regular': 2}

# Test 2: Park a motorbike
lot.park(motorbike)  # Should park in Compact spot
assert lot.get_available_spots() == {'Compact': 0, 'Regular': 2}

# Test 3: Park a car
lot.park(car)  # Should park in Regular spot
assert lot.get_available_spots() == {'Compact': 0, 'Regular': 1}

print("All tests passed!")



