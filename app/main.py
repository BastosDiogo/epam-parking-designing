from classes import ParkingLot, Motorbike, Car

# TESTS
# Create a parking lot
lot = ParkingLot()
lot.add_parking_spot("Compact", 1)
lot.add_parking_spot("Regular", 2)
lot.add_parking_spot("Regular", 3)

# Create vehicles
motorbike = Motorbike()
car = Car()

print(f'Lot: {lot}')
# Test 1: Initial state
assert lot.get_available_spots() == {'Compact': 1, 'Regular': 2}

# Test 2: Park a motorbike
lot.park(motorbike)  # Should park in Compact spot
assert lot.get_available_spots() == {'Compact': 0, 'Regular': 2}

# Test 3: Park a car
lot.park(car)  # Should park in Regular spot
assert lot.get_available_spots() == {'Compact': 0, 'Regular': 1}

print("All tests passed!")



