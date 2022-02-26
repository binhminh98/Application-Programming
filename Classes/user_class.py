"""
Module to define class User and its subclasses: NewUser, OldUser, Admin, Lecturer. 
And a Privilege class that shows privileges of the class Admin
"""

import Classes.file_class as fc
import Functions.command as c
import Functions.main_game_function as mgf
import Functions.main_menu_function as mmf
import Functions.map as m
import sys
import Functions.inventory as inv
import time

class User():
    """Defining superclass User"""

    def __init__(self, username='', password='', current_location=m.bed_room, inventory={}, test_count={}, **save_info):
        """Initializing attributes of User class"""
        self.username = username
        self.password = password
        self.current_location = current_location
        self.inventory = inventory
        self.test_count = test_count
        self.save_info = save_info
        self.level = 0
        self.first_time = True
        self.gpa = 0
        self.save_info['current_location'] = self.current_location.name
        self.save_info['inventory'] = []

# 8. Use case: see map
    def display_current_map(self,mode='r'):
        """
        Method to display a map to user. Parameters:
            1. name: input self.map_path of a building
            2. mode: read mode by default
        """
        current_location = self.current_location.map_path
        map = fc.TXTFile(f'Graphics/{current_location}',mode)
        map.print_content()
        return map

# 9. Use case: see inventory
    def display_inventory(self):
        """Method to print current inventory to user"""
        items_count = self.count_inventory_items()
        if items_count == 0:
            message = '\nYour inventory is currently empty...'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        elif items_count == 1:
            message =  f'\nYou currently have {items_count} item in your inventory:'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()

        else:
            message = f'\nYou currently have {items_count} items in your inventory:'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        for item in self.inventory.values():
            print(f"- {item.name.title()}")
        return message

    def count_inventory_items(self):
        """Method to count total items in the inventory"""
        items_count = len(self.inventory.keys())
        return items_count

# 10. Use case: inspect location
    def inspect_current_location(self):
        """Method to display current location's description"""
        # If the location contains items -> inform users
        location_description = self.current_location.description
        location_name = self.current_location.name
        if self.current_location.name in m.location_contains_items.keys():
            message = f'\n{location_description}.\nYou see some items in {location_name.title()}...'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        else:
            message = f"\n{location_description}.\nSeems like there's nothing to do here..."
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        self.first_time_inspect()
        return message
        
    def first_time_inspect(self):
        """Method to display a message to prompt for 'search item' command if it is the first time"""
        if self.first_time == True:
            message = "\nYou could also use command: 'search item' to search for items in this location"
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            self.first_time = False
            self.save_info['first_time'] = self.first_time
        return self.first_time

# 11. Use case: inspect items
    def inspect_item(self, container):
        """Method to inspect an item -> print its description"""
        # Inspect item in both Inventory and World Object
        if container == 'inventory':
            item = self.prompt_item_name_inventory()
        elif container == 'location':
            item = self.prompt_item_name_location()
        # If invalid item -> pass
        if item == None:
            pass
        else:
            # Try to retrieve item's type 
            # If it does not exist -> print its description
            # try:
                if item.type == 'Badge':
                    message = f"\n{item.description} {item.title}"
                    for character in message:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.005)
                    print()
                elif item.type == 'Test':
                    test_done = self.check_test_done(item.name)
                    self.prompt_do_test(item.name,test_done)
                elif item.type == 'Lecture Note':
                    self.prompt_read_note(item.name)
                else:
                    message = f"\n{item.description}"
                    for character in message:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.005)
                    print()

    def prompt_item_name_location(self):
        """Method to prompt user to choose an item -> return item name"""
        item = None
        items_count = self.count_current_location_items()
        # If a location has 0 item -> print message
        if items_count == 0:
            pass
        else:
            prompt = input(f"\nType 'item's name' to look the item: ")
            # Saninitise user's input
            item_name = prompt.lower().strip()
            item_name = mgf.check_valid_command(item_name,c.world_objects)
            mgf.check_quit_command(self,item_name)
            # Generate a list of items in user's current location
            current_location_items_list = [item for item in self.current_location.items.keys()]
            # If user input correct item -> assign to variable 'item'
            # If user input incorrect item -> print a message
            if item_name in current_location_items_list:
                item = self.current_location.items[item_name]
                if item.type in ['Lecture Note','Test'] and item.owned == True:
                    message = f"\nYou've already done this {item.type.lower()}. If you want to revise the lecture's materials, open your Inventory."
                    for character in message:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.005)
                    print()
                    item = None
            else:
                message = f"\nThere is no '{item_name.title()}' in your current location: {self.current_location.name.title()}"
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
        return item
    
    def prompt_item_name_inventory(self):
        """Method to prompt user to choose an item -> return item name"""
        item = None
        items_count = self.count_inventory_items()
        # If the inventory has 0 item -> pass
        if items_count == 0:
            pass
        else:
            prompt = input(f"\nType 'item's name' to look at the item: ")
            # Saninitise user's input
            item_name = prompt.lower().strip() 
            item_name = mgf.check_valid_command(item_name,c.world_objects)
            # Generate a list comprehension of items in user's inventory
            inventory_items_list = [item for item in self.inventory.keys()]
            # If user input correct item -> assign to variable 'item'
            # If user input incorrect item -> print a message
            if item_name in inventory_items_list:
                item = self.inventory[item_name]
            else:
                message = f"\nThere is no '{item_name}' in your Inventory"
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
        return item

    def display_current_location_items(self):
        """Method to display items in current location"""
        item_list = self.current_location.items.values()
        items_count = self.count_current_location_items()
        if items_count == 0:
            message = f"\nThere is nothing in {self.current_location.name.title()}..."
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        elif items_count == 1:
            message = f"\nYou see an item in {self.current_location.name.title()}:"
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        else:
            message = f"\nYou see several items in {self.current_location.name.title()}:"
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        # Print items in current location
        for item in item_list:
            if item.availability == True:
                if self.check_owned_item(item.name) == False:
                    print(f"- {item.name.title()}")
                else:
                    print(f"- {item.name.title()} (owned)")

    def check_interactive_location(self):
        """
        Method to check if the current location contains 
        interactive items or not -> return a Flag
        """
        interactive_location = False
        if self.current_location.name in m.location_contains_items.keys():
            interactive_location = True
        return interactive_location

    def count_current_location_items(self):
        """Method to count total items available in a location"""
        items_count = 0
        for item in self.current_location.items.values():
            if item.availability == True:
                items_count += 1
        return items_count

    def check_owned_item(self, key):
        """Method that return a flag of whether an item is owned or not"""
        # If key does not exist -> print a message
        owned_item = None
        try:
            owned_item = inv.item_dicts[key].owned
        except KeyError:
            pass
        return owned_item

# 12. Use case: pick up item to inventory
    def choose_item(self):
        """Method to choose item to pick up"""
        item_name = None
        item_counts = self.count_current_location_items()
        if item_counts == 0:
            print('\nThere is nothing here to pick up...')
        else:
            message = '\nWhich item do you wanna pick up? '
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            for item in self.current_location.items.values():
                if item.availability == True and item.owned == True:
                    print(f'- {item.name.title()} (owned)')
                elif item.availability == True:
                    print(f'- {item.name.title()}')
            item_name = input('> ')
            if item.owned == True:
                print("\nYou've already owned this item...")
                item_name = None
            else:
                if item_name in inv.unpickable_item_dicts.keys():
                    print("\nThis item cannot be picked up. You need to read it... (type 'inspect item')")
                    item_name = None
        return item_name

    def pickup_item(self, key):
        """Method to pickup and add an item into inventory dictivonary"""
        # Check if user has owned the item or not
        item_owned = self.check_owned_item(key)
        if item_owned == False:
            # Search item's key in the game's item dictionary -> auto remove duplicates
            self.inventory[key] = inv.item_dicts[key]
            # Print a message to user
            item = self.inventory[key]
            if item.type == 'Badge':
                message = f"\nYou've earned yourself a brand new badge: {item.name.title()}"
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
            elif item.type == 'Degree':
                self.earn_degree(inv.degree_ap)
            else:
                message = f"\nYou've picked up {item.name.title()} to your Inventory"
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
            # Save inventory to user's save_info dictionary
            self.save_info['inventory'].append(item.__dict__)
            self.own_item(key)
        elif item_owned == None:
            current_location = self.current_location.name.title()
            print(f"\nSorry, there is nothing as a '{key}' in {current_location}")
        else:
            print("\nYou've already owned this item...")
        return self.inventory

    def unlock_location_of_item(self,item):
        """Method to unlock a location"""
        # For loop to search for the item's corresponding location
        for location in m.world_dicts.values():
            if item == location.unlock_item:
                if location.locked == True:
                    print(f"\nThe {location.name.title()} has been unlocked!!")
                    location.locked = False
        return item

    @staticmethod
    def own_item(key):
        """Method to change item's 'owned flag' to True"""
        inv.item_dicts[key].owned = True
        flag = inv.item_dicts[key].owned
        return flag

# 13. Use case: see overall progress
    def show_progress(self):
        """Method to show user's overall progress"""
        owned_transcript = inv.item_dicts['transcript'].owned
        if owned_transcript == True:
            degree = self.inventory['transcript'].degree
            message = f'\nYour level: {self.level}'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            try:
                self.gpa = self.calculate_gpa(inv.test_ap_dict)
                message = f'\nYour current GPA of {degree} degree: {self.gpa}/100.'
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
            except ZeroDivisionError:
                message = "\nYou haven't took any tests in your Masters degree..."
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
        else:
            message = "\nYou haven't got a transcript. Go to your Living Room to get your transcript."
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()

# 14. Use case: move around
    def move(self):
        """Method to move around the map"""
        # Prompt user to move to a direction
        direction = input('\nWhere would you like to go?: ')
        # Check user'sinput
        mgf.check_quit_command(self,direction)
        if direction.lower().strip() in c.HELP_COMMANDS:
            self.current_location = mmf.interact_help_menu(self.move,[self])
        direction = self.convert_move_commands(direction)
        direction = self.check_direction_exist(direction)
        direction = self.check_locked_location(direction)
        # If locked location => direction = none => pass
        if direction == None:
            pass
        else:
            # Move user to their destination (not locked)
            self.current_location = self.move_user(direction)
        return self.current_location

    def check_direction_exist(self, direction):
        """Method to detect invalid direction -> return a valid direction"""
        # Flag of whether the direction exists or not
        while self.current_location.directions[direction] == None:
            if self.current_location.directions[direction] == None:
                direction = input(f'You cannot go {direction}. Please try again: ')
                direction = self.convert_move_commands(direction)
                mgf.check_quit_command(self,direction)
            else:
                break
        return direction

    def check_locked_location(self, direction):
        """Method to check a location is locked or not -> return a valid direction"""
        # A flag to check locked condition
        # -> if the location is locked, a while loop to prompt users for another move command
        locked = True
        # Retrieve location name
        destination = self.current_location.directions[direction]
        while locked == True:
            # Loop through the list of location in the world
            # If matches -> assign a 'locked' flag
            for location in m.world_dicts.values():
                if location == destination:
                    locked = location.locked
                    break
            if locked == True:
                if location.name == 'hall of fame entrance':
                    print(f"\nThe {location.name.title()} is temporarily locked. Please comeback later...")
                    direction = None
                elif location.name.lower() in ['db room','rt room']:
                    print(f"\nYou will need a password to enter {location.name.title()}.")
                    direction = self.verify_room_password(location.password, direction)
                else:
                    print(f"\nThe {location.name.title()} is locked. Please find something to unlock it...")
                    direction = None
                break
        return direction
    
    @staticmethod
    def verify_room_password(password, direction):
        """Method to verify rooms's password to let user in"""
        input_password = input('\nPlease enter password to enter this room: ')
        if input_password == password:
            pass
        else:
            print('\nWrong password! Try again later...')
            direction = None
        return direction

    def move_user(self, direction):
        """Method to move player to the destination"""
        destination = self.current_location.directions[direction]
        self.current_location = destination
        # Save current_location to user's save_info dictionary
        self.save_info['current_location'] = self.current_location.name
        message = f"\nYou've moved to {self.current_location.name.title()}"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        self.display_current_map()
        self.check_enter_leaderboard(destination)
        return self.current_location

    def check_enter_leaderboard(self, destination):
        """Method to check if user enters the leaderboard or not -> end the game"""
        if destination.name == 'leaderboard':
            self.display_learderboard()
            message = "\nCONGRATULATIONS! YOU HAVE WON THE GAME!"
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            mgf.save_progress(self)
            sys.exit()

    def display_learderboard(self):
        """Method to display current leaderboard of the game"""
        users = mgf.load_existing_users()
        message = '\nTHE MOST GIFTED STUDENTS WILL ALWAYS BE REMEMBERED:'
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        current_user_details = f"- {self.username} - Level: {self.level} - Degree classification: {self.inventory['msc data science degree'].classification}"
        for character in current_user_details:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for user in users:
            for item in user['inventory']:
                if item['type'] == 'Degree':
                        user_details = f"- {user['username']} - Level: {user['level']} - Degree classification: {item['classification']}"
                        print(user_details)
                        break

    @staticmethod
    def convert_move_commands(command):
        """Function convert move command to a valid input"""
        command = mgf.check_valid_command(command,c.VALID_MOVE_COMMANDS)
        if command.lower().strip() in c.MOVE_UP_COMMANDS:
            command = 'up'
        elif command.lower().strip() in c.MOVE_DOWN_COMMANDS:
            command = 'down'
        elif command.lower().strip() in c.MOVE_LEFT_COMMANDS:
            command = 'left'
        elif command.lower().strip() in c.MOVE_RIGHT_COMMANDS:
            command = 'right'
        return command

# 15. Use case: do tests
    def prompt_read_note(self,note):
        """Method to prompt user to read lecture"""
        message = '\nDo you wanna read this lecture note right now?'
        print(message)
        lecture_check = input('> ')
        # Sanitized input
        lecture_check = mgf.check_valid_command(lecture_check,c.VALID_TEST_COMMANDS)
        if message.lower().strip() in c.HELP_COMMANDS:
            mmf.interact_help_menu(self.prompt_read_note,[self,note])        
        mgf.check_quit_command(self,lecture_check)
        if lecture_check in c.NO_COMMANDS:
            print('You can return to this lecture anytime...')
        elif lecture_check in c.YES_COMMANDS:
            self.read_note(note)

    def read_note(self,note):
        """Method to read lecture notes"""
        # Retrieve lecture note contents
        lecture_note_contents = self.current_location.items[note].content.values()
        # For loop to print all content in the lecture note
        for content in lecture_note_contents:
            message = f'{content}'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            continue_check = input('\nDo you want to continue to the next sentence? (y/n) ')
            # Sanitize input
            mgf.check_valid_command(continue_check,c.VALID_TEST_COMMANDS)
            if continue_check.lower().strip() in c.HELP_COMMANDS:
                mmf.interact_help_menu(self.read_note,[self,note])
            mgf.check_quit_command(self,continue_check)
            # While loop if user type 'yes' -> move on to the next sentence
            while continue_check in c.NO_COMMANDS:
                if continue_check in c.NO_COMMANDS:
                    continue_check = input("Not yet? Take your time ... (type 'y/n' to continue): ")
                    mgf.check_valid_command(continue_check,c.VALID_TEST_COMMANDS)
                elif continue_check in c.YES_COMMANDS:
                    break
        # Pick up the item to inventory if not owned to unlock the next location
        if self.current_location.items[note].owned == False:
            self.pickup_item(note)
            self.unlock_location_of_item(note)

    def prompt_do_test(self,test,test_done):
        """Method to prompt user to do test"""
        if test_done == False:
            message = '\nDo you wanna do this test right now?\n'
            message += 'There are a total of 5 questions, 20 points each.\n'
            message += '(You need to earn more than 50 points to pass this test)'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            test_check = input('> ')
            # Sanitized input
            test_check = mgf.check_valid_command(test_check,c.VALID_TEST_COMMANDS)
            mgf.check_quit_command(self,test_check)
            if test_check in c.NO_COMMANDS:
                print('You can return to this test anytime...')
            elif test_check in c.YES_COMMANDS:
                self.do_test(test)

    def check_test_done(self,test):
        """Method to check if user has already done the test or not"""
        test_done = None
        try:
            test_done = self.inventory[test].owned
        except KeyError:
            test_done = False
        else:
            if test_done == True:
                test_name = self.inventory[test].name
                test_mark = self.inventory[test].mark
                print(f"\nYou've already finished {test_name}... Test mark: {test_mark}/100!!!")
        return test_done

    def do_test(self,test):
        """Method to do a test and print current GPA of user"""
        test_content = self.current_location.items[test].content
        test_mark = 0
        for question in test_content.keys():
            message = f'\n{question}'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            response = input('What is your answer for this question? ')
            mgf.check_quit_command(self,response)
            suitable_answer = False
            while suitable_answer == False:
                if response in ['1','2','3','4']:
                    if response == test_content[question]:
                        message = f"\nCongratulation, {self.save_info['name'].title()}! Your answer is correct!"
                        for character in message:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.005)
                        print()
                        test_mark += 20
                    else:
                        message = f"\nUnfortunately, the answer is: '{test_content[question]}' :( Good luck in the next quetion!"
                        for character in message:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.005)
                        print()
                    suitable_answer = True
                else:
                    response = input('Please input a number (1,2,3,4): ')
        self.classify_test_result(test,test_mark)

    def increment_test_count(self,test):
        """
        Method to increment the test count of a module by 1 after they finish a test.
            - Try: have done some test in the module =? increment test count by 1
            - Except: have not done any test in that module => set to 0
        """
        for module in m.school_rooms_dict.values():
            if self.inventory[test].module == module.name:
                try:
                    self.test_count[module.name] += 1
                    self.finish_module(module)
                except KeyError:
                    self.test_count[module.name] = 0
                    self.test_count[module.name] += 1
                break
        return self.test_count

# 16. Use case: earn marks
    def classify_test_result(self, test, test_mark):
        """
        Method to classify test result
            - test_mark < 50: fail
            - 50 <= test_mark < 70: pass -> +1 level
            - test_mark >= 70: distinction -> +2 level
        """
        # Print test mark
        message = f'\nYour mark for this test: {test_mark}/100 :D'
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        # Pick up item to unlock new location
        if test_mark < 50:
            message = f"\nYou've failed the test. Goodluck next time :("
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            pass
        elif test_mark >= 50 and test_mark < 70:
            message = "\nYou've passed the test with a decent mark!"
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            self.level_up(1)
            message = f'You have level up +1 level to: level {self.level}.'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            self.pickup_item(test)
            self.current_location.items[test].mark = test_mark
            self.earn_badge()
            self.update_gpa()
            # Increment the test count of that module by 1
            self.increment_test_count(test)
        elif test_mark >= 70:
            message = "Congratulations!!! You've passed the test with a distinction mark!!!"
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            self.level_up(2)
            message = f'You have level up +2 level to: level {self.level}.'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            self.pickup_item(test)
            self.current_location.items[test].mark = test_mark
            self.earn_badge()
            self.update_gpa()
            # Increment the test count of that module by 1
            self.increment_test_count(test)

    def update_gpa(self):
        """Method to update current user's GPA"""
        self.gpa = self.calculate_gpa(inv.test_ap_dict)
        # Save current GPA to transcript
        self.inventory['transcript'].gpa = self.gpa
        message = f'\nYour current GPA: {self.gpa}'
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        return self.gpa

    @staticmethod
    def calculate_gpa(module_test_dict):
        """Method to calculate current user's GPA"""
        tests_count = 0
        total_mark = 0
        # Count the tests that have mark
        for test in module_test_dict.values():
            if test.mark == '':
                continue
            else:
                tests_count += 1
        # Sum total mark for the module
        for test in module_test_dict.values():
            if test.mark == '':
                continue
            else:
                total_mark += test.mark
        # Rounding GPA to 2 decimal points
        gpa = round(total_mark/tests_count, 2)
        return gpa

# 17. Use case: level up
    def level_up(self,number):
        """Method to level up user"""
        self.level += number
        self.save_info['level'] = self.level
        return self.level

# 18. Use case: earn badges
    def earn_badge(self):
        """Method to reward the corresponding badge after user finishes a test"""
        badge_name = None
        for item in self.current_location.items.values():
            if item.type == 'Badge':
                item.availability = True
                badge_name = item.name
                self.pickup_item(badge_name)
                message = f"{item.description} {item.title}"
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.005)
                print()
                self.unlock_location_of_item(badge_name)
        return badge_name

# 19. Use case: earn degree
    def finish_module(self,module):
        """Method to finish a module -> return a flag"""
        if self.test_count[module.name] == module.total_tests:
            module.finished = True
        return module.finished

    def earn_degree(self,degree):
        """Method for student to earn a degree after completed all tests"""        
        degree.gpa = self.gpa
        message = f"\nCongratulations {self.save_info['name'].title()}! You have successfully earned yourself a degree in {degree.degree}"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        if 50 <= degree.gpa < 60:
            degree.classification = 'pass'
            message = f'Your degree classification: {degree.classification.title()}. Goodjob!'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        elif 60 <= degree.gpa < 70:
            degree.classification = 'merit'
            message = f'Your degree classification: {degree.classification.title()}. Hooray!!'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
        elif degree.gpa >= 70:
            degree.classification = 'distinction'
            message = f'Your degree classification: {degree.classification.title()}. Well done indeed!!!'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()


class NewUser(User):
    """Defining subclass NewUser"""

    def __init__(self, username='', password='', current_location=m.bed_room, inventory={}, **save_info):
        """Initializing attributes of NewUser class"""
        super().__init__(username, password, current_location, inventory, **save_info)
        self.users = mgf.load_existing_users()


class OldUser(User):
    """Defining subclass OldUser"""

    def __init__(self, username='', password='', current_location=m.bed_room, inventory={}, **save_info):
        """Initializing attributes of NewUser class"""
        super().__init__(username, password, current_location, inventory, **save_info)


class Admin(OldUser):
    """Defining subclass Admin"""

    def __init__(self, username='', password='', current_location=m.bed_room, inventory={}, **save_info):
        """Initializing attributes of class Admin"""
        super().__init__(username, password, current_location, inventory, **save_info)
        self.save_info['username'] = self.username
        self.save_info['password'] = self.password
        self.privileges = Privilege()


class Privilege():
    """Defining Privileges class"""

    def __init__(self, privileges=[]):
        """Initializing attributes of class Privilege"""
        privileges = ["Check user's information"]
        self.privileges = privileges

    def display_privileges(self):
        """Method to show Admin's privileges"""
        message = "\nAdmin's privileges: "
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for privilege in self.privileges:
            print(f'- {privilege}')