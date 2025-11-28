import unittest
from uuid import uuid4
from classes import ParkingLot, Motorbike, Car

class TestParking(unittest.TestCase):

    def test_add_parking_spot(self):
        lot = ParkingLot()

        lot.add_parking_spot("Compact", str(uuid4()))
        lot.add_parking_spot("Regular", str(uuid4()))
        lot.add_parking_spot("Regular", str(uuid4()))

        expected = {'Compact': 1, 'Regular': 2}
        evaluation = lot.get_available_spots()
        assert_ = evaluation == expected

        self.assertTrue(assert_, f'FAILED.\nExpected: {expected}\nEvaluation: {evaluation}')

    def test_creating_motorbike_instance(self):
        motorbike = Motorbike()

        expected = True
        evaluation = isinstance(motorbike, Motorbike)
        assert_ = evaluation == expected

        self.assertTrue(assert_, f'FAILED.\nExpected: {expected}\nEvaluation: {evaluation}')

    def test_creating_car_instance(self):
        car = Car()

        expected = True
        evaluation = isinstance(car, Car)
        assert_ = evaluation == expected

        self.assertTrue(assert_, f'FAILED.\nExpected: {expected}\nEvaluation: {evaluation}')


if __name__ == '__main__':
    unittest.main()
