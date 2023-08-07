import unittest
from backend_layer.data_models import CrewMember, Ship, DispositionSchedule
from backend_layer.crud_operations import create_crew_member, create_ship, assign_crew_to_ship
from backend_layer.business_logic import load_ship_schedules, assign_crew_members

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.crew_member = CrewMember(crew_id=1, crew_name='John Doe')
        self.ship = Ship(ship_id=1, ship_name='Riviera')
        self.disposition_schedule = DispositionSchedule(id=1, crew_id=1, ship_code=1)

    def test_create_and_assign_crew_member(self):
        create_crew_member(self.crew_member)
        create_ship(self.ship)
        assign_crew_to_ship(self.crew_member, self.ship)
        self.assertEqual(self.crew_member.ship, self.ship)

    def test_load_ship_schedules(self):
        create_ship(self.ship)
        load_ship_schedules(self.ship)
        self.assertIsNotNone(self.ship.schedules)

    def test_assign_crew_members(self):
        create_crew_member(self.crew_member)
        create_ship(self.ship)
        assign_crew_members(self.ship, [self.crew_member])
        self.assertIn(self.crew_member, self.ship.crew_members)

if __name__ == '__main__':
    unittest.main()