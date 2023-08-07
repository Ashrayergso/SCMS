import unittest
from backend_layer import data_models, crud_operations, business_logic

class TestSCMS(unittest.TestCase):

    def setUp(self):
        self.crew_member = data_models.CrewMember()
        self.ship_schedule = data_models.ShipSchedule()
        self.crud = crud_operations.CRUDOperations()
        self.logic = business_logic.BusinessLogic()

    def test_crew_member_creation(self):
        self.crew_member.crew_id = 1
        self.crew_member.crew_name = "John Doe"
        self.assertEqual(self.crew_member.crew_id, 1)
        self.assertEqual(self.crew_member.crew_name, "John Doe")

    def test_ship_schedule_creation(self):
        self.ship_schedule.id = 1
        self.ship_schedule.ship_code = "SC001"
        self.assertEqual(self.ship_schedule.id, 1)
        self.assertEqual(self.ship_schedule.ship_code, "SC001")

    def test_crud_operations(self):
        # Test Create operation
        created_crew_member = self.crud.create(self.crew_member)
        self.assertEqual(created_crew_member.crew_id, 1)

        # Test Read operation
        read_crew_member = self.crud.read(1)
        self.assertEqual(read_crew_member.crew_id, 1)

        # Test Update operation
        self.crew_member.crew_name = "Jane Doe"
        updated_crew_member = self.crud.update(self.crew_member)
        self.assertEqual(updated_crew_member.crew_name, "Jane Doe")

        # Test Delete operation
        self.crud.delete(self.crew_member)
        deleted_crew_member = self.crud.read(1)
        self.assertIsNone(deleted_crew_member)

    def test_business_logic(self):
        # Test Load Ship Schedules
        schedules = self.logic.load_ship_schedules("Riviera", "June")
        self.assertIsNotNone(schedules)

        # Test Assign Crew Members
        assigned = self.logic.assign_crew_members(self.crew_member, self.ship_schedule)
        self.assertTrue(assigned)

if __name__ == '__main__':
    unittest.main()

