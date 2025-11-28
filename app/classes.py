import copy
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Base class for all vehicles"""
    def __init__(self, compact:bool, regular:bool):
        self.compact = compact
        self.regular = regular

    @abstractmethod
    def number_of_tires(self):
        pass

    def vehicle_type(self):
        """Return type of vehicle."""
        return {'compact': self.compact, 'regular': self.regular}

class ParkingSpot:
    """Class representing a parking spot"""
    def __init__(self, spot_id, spot_type):
        self.id = spot_id
        self.type = spot_type
        self.is_occupied = False
        self.vehicle = None

    def __repr__(self):
        return (
            f'ParkingSpot(id: {self.id}, type: {self.type}, is_occupied: {self.is_occupied}, '
            + f'vehicle: {self.vehicle})'
        )

class ParkingLot:
    """Class for managing the parking lot"""
    def __init__(self):
        self.spots = {'Regular': 0, 'Compact': 0}
        self.parking_spots = []

    @property
    def all_parking_spots(self):
        return self.parking_spots

    @property
    def parking_spot(self):
        """List of types of spots."""
        return tuple(self.spots.keys())

    def __repr__(self):
        return f'ParkingLot(spots: {self.spots}, parking_spots: {self.spots})'

    def __str__(self):
        response = copy.copy(self.spots)
        response['parking_spots'] = self.parking_spots
        return f'{response}'

    def add_parking_spot(self, spot_type:str, spot_id:int):
        """Add a parking spot to the lot"""
        spot_type = spot_type.capitalize()
        if spot_type not in self.parking_spot:
            print('spot_type is not a valid type.')
            return False

        elif spot_id in tuple(map(lambda x: x.id, self.all_parking_spots)):
            print(f'ID {spot_id} already added.')
            return False

        self.spots[spot_type] += 1
        self.parking_spots.append(ParkingSpot(spot_id, spot_type))
        print(f'spot_type was added suscess!')
        return True
    
    def park(self, vehicle):
        """Park a vehicle in the lot"""
        if vehicle.compact is False and vehicle.regular is True:
            self.spots['Regular'] -= 1
            print('Vehicle has been parking on Regular spot.')

        else:
            self.spots['Compact'] -= 1
            print('Vehicle has been parking on Compact spot.')
    
    def get_available_spots(self):
        """Get count of available spots by type"""
        return self.spots



class Motorbike(Vehicle):
    def __init__(self):
        super().__init__(True, True)

    def number_of_tires(self):
        return {'tire': 2}

class Car(Vehicle):
    def __init__(self):
        super().__init__(False, True)

    def number_of_tires(self):
        return {'tire': 4}