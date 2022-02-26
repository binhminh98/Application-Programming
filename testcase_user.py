"""
Module for testcases of user_class.py
"""

import unittest
import Functions.map as m
import Classes.user_class as uc
import Functions.inventory as inv
import Functions.main_menu_function as mmf

class TestUser(unittest.TestCase):
    """Testcase for 'user_class.py'"""

    def setUp(self):
        """Method to create an user instance to use in all test methods"""
        self.user = uc.User('admin','tda21hwu')


class TestInit(TestUser):
    """Test user initialize"""
    
    def test_initialize_username(self):
        """Test if initial username = 'admin'"""
        self.assertEqual(self.user.username,'admin')

    def test_initialize_password(self):
        """Test if initial password = 'tda21hwu'"""
        self.assertEqual(self.user.password,'tda21hwu')

    def test_initialize_current_location(self):
        """Test if initial current location = bedroom"""
        self.assertEqual(self.user.current_location,m.bed_room)

    def test_initialize_inventory(self):
        """Test if initial inventory = {}"""
        self.assertEqual(self.user.inventory,{})

    def test_initialize_test_count(self):
        """Test if initial test_count = {}"""
        self.assertEqual(self.user.test_count,{})

    def test_initialize_level(self):
        """Test if initial level = 0"""
        self.assertEqual(self.user.level,0)

    def test_initialize_gpa(self):
        """Test if initial gpa = 0"""
        self.assertEqual(self.user.gpa,0)

    def test_initialize_save_info_current_location(self):
        """Test if initial save information['current_location'] = 'bedroom'"""
        self.assertEqual(self.user.save_info['current_location'],'bedroom')

    def test_initialize_save_info_inventory(self):
        """Test if initial save information['inventory'] = []"""
        self.assertEqual(self.user.save_info['inventory'],[])


class TestSeeMap(TestUser):
    """Test method to display the current map"""

    def test_display_current_map(self):
        """Test if return a map path = current location's map path"""
        map = self.user.display_current_map()
        self.assertEqual(map.path, f"Graphics/{self.user.current_location.map_path}")


class TestSeeInventory(TestUser):
    """Test methods to display the inventory"""

    def test_count_items_in_inventory(self):
        """Test if return count of items in inventory"""
        item_count = self.user.count_inventory_items()
        self.assertEqual(item_count, 0)

    def test_display_empty_inventory(self):
        """Test if return the string '\nYour inventory is currently empty...'"""
        self.user.inventory = {}
        message = self.user.display_inventory()
        self.assertEqual(message, '\nYour inventory is currently empty...')
    
    def test_display_inventory_has_one_item(self):
        """Test if return the string '\nYou currently have 1 item in your inventory:'"""
        self.user.inventory = {}
        self.user.inventory['backpack'] = inv.backpack
        message = self.user.display_inventory()
        self.assertEqual(message, '\nYou currently have 1 item in your inventory:')
    
    def test_display_inventory_has_more_than_one_item(self):
        """Test if return the string '\nYou currently have 2 items in your inventory:'"""
        self.user.inventory = {}
        self.user.inventory['backpack'] = inv.backpack
        self.user.inventory['transcript'] = inv.transcript
        message = self.user.display_inventory()
        self.assertEqual(message, '\nYou currently have 2 items in your inventory:')


class TestInspectLocation(TestUser):
    """Test methods to inspect the current location"""
    
    def test_inspect_current_location(self):
        """Test if return string '\nThis is your bedroom.\nYou see some items in Bedroom'"""
        message = self.user.inspect_current_location()
        self.assertEqual(message, '\nThis is your bedroom.\nYou see some items in Bedroom...')

    def test_first_time_user_inspect_location(self):
        """Test methods to check if self.user.first_time = False"""
        self.user.first_time = self.user.first_time_inspect()
        self.assertEqual(self.user.first_time, False)


class TestCreateCharacter(TestUser):
    """Test methods to create new character"""

    def test_function_to_input_username(self):
        """Test if return full_name = 'first_name.title()' + 'last_name.title()'"""
        full_name = mmf.input_name(self.user)
        self.assertEqual(full_name, 'Minh Lai')

    def test_function_to_input_valid_age(self):
        """Test if return age from range 0-100"""
        age = mmf.input_age(self.user)
        self.assertIn(age, [str(i) for i in range(0,101)])

    def test_function_to_input_valid_gender(self):
        """Test if return gender in ['male','female','unknown]"""
        gender = mmf.input_gender(self.user)
        self.assertIn(gender, ['male','female','unknown'])

    def test_function_to_input_valid_height(self):
        """Test if return height from range 70-230"""
        height = mmf.input_height(self.user)
        self.assertIn(height, [str(i) for i in range(70,231)])

    def test_function_to_input_valid_weight(self):
        """Test if return weight from range 30-200"""
        weight = mmf.input_weight(self.user)
        self.assertIn(weight, [str(i) for i in range(30,201)])

    def test_function_to_input_valid_title(self):
        """Test if return title in ['student','lecturer']"""
        title = mmf.input_title(self.user)
        self.assertIn(title, ['student','lecturer'])


class TestMove(TestUser):
    """Test methods to move user around"""

    def test_move_to_valid_destinations(self):
        """Test if return current_location = new location"""
        self.user.current_location = m.bed_room
        self.user.move_user('down')
        self.assertEqual(self.user.current_location, m.living_room)

    def test_move_to_invalid_destinations(self):
        """Test if return string direction in ['up','down','left','right']"""
        self.user.current_location = m.bed_room
        direction = self.user.check_direction_exist('left')
        self.assertIn(direction, ['up','down','left','right'])
    
    def test_move_to_locked_destinations(self):
        """Test if return direction = None"""
        self.user.current_location = m.world
        direction = self.user.check_locked_location('up')
        self.assertEqual(direction, None)

    def test_move_to_destinations_with_password(self):
        """Test if return direction in [None,'up','down','left','right']"""
        self.user.current_location = m.cmp
        direction = self.user.check_locked_location('down')
        self.assertIn(direction, [None,'up','down','left','right'])

if __name__ == '__main__':
    unittest.main()