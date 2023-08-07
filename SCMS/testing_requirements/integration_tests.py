import unittest
from backend_layer.data_models import CrewMembers, DispositionSchedule, TrainingRecords, ShipJobAmounts, Ships, ShipPortSchedule, Ports, Brand, JobCodes, CrewTrainingRecords
from backend_layer.crud_operations import create_crew_member, update_crew_member, delete_crew_member, get_crew_member
from backend_layer.business_logic import load_ship_schedules, assign_crew_members

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.crew_member = CrewMembers(crew_id=1, crew_name='John Doe')
        self.disposition_schedule = DispositionSchedule(id=1, crew_id=1, ship_code='SC001')
        self.training_record = TrainingRecords(training_id=1, training_name='Safety Training')

    def test_crud_operations(self):
        # Test Create operation
        create_crew_member(self.crew_member)
        result = get_crew_member(1)
        self.assertEqual(result.crew_name, 'John Doe')

        # Test Update operation
        self.crew_member.crew_name = 'Jane Doe'
        update_crew_member(self.crew_member)
        result = get_crew_member(1)
        self.assertEqual(result.crew_name, 'Jane Doe')

        # Test Delete operation
        delete_crew_member(self.crew_member)
        result = get_crew_member(1)
        self.assertIsNone(result)

    def test_business_logic(self):
        # Test Load Ship Schedules
        schedules = load_ship_schedules('Riviera', 'June')
        self.assertIsNotNone(schedules)

        # Test Assign Crew Members
        assign_crew_members(self.crew_member, self.disposition_schedule)
        result = get_crew_member(1)
        self.assertEqual(result.disposition_schedule.ship_code, 'SC001')

    def tearDown(self):
        delete_crew_member(self.crew_member)

if __name__ == '__main__':
    unittest.main()