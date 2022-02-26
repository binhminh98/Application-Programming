"""
Module to define functions in the main game play
"""

import Functions.command as c
import Classes.file_class as fc
import Classes.user_class as uc
import Functions.main_menu_function as mmf
import Functions.map as m
import sys
import time

# 7. Use case: Play game (Main game loop)
def prompt_action_loop(current_user):
    """Function to prompt users for their action in main game world"""
    m.home.owner = current_user.username
    # Prompt for the next action
    action = prompt_action()
    action = check_valid_command(action,c.VALID_MAIN_GAME_COMMANDS)
    action = action.lower().strip()
    if action in c.ME_COMMANDS:
        display_user_information(current_user)
    elif action in c.MOVE_COMMANDS:
        current_user.move()
    elif action in c.INSPECT_COMMANDS:
        current_user.inspect_current_location()
    elif action in c.INSPECT_ITEM_COMMANDS:
        if current_user.check_interactive_location() == True:
            current_user.display_current_location_items()
            current_user.inspect_item('location')
        else:
            print('\nThere is nothing here...')
    elif action in c.INVENTORY_COMMANDS:
        current_user.display_inventory()
        current_user.inspect_item('inventory')
    elif action in c.PICKUP_ITEM_COMMANDS:
        item_name = current_user.choose_item()
        if item_name == None:
            pass
        else:
            current_user.pickup_item(item_name)
            current_user.unlock_location_of_item(item_name)
    elif action in c.SAVE_COMMANDS:
        save_progress(current_user)
        message = f"\nYou've succesfully saved your progress, {current_user.save_info['name'].title()}."
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
    elif action in c.CHECK_USERS_COMMANDS:
        if mmf.check_admin(current_user) == True:
            check_user_information()
        else:
            message = '\nYou are not the Admin!!!'
            for character in message:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
    elif action in c.DISPLAY_MAP_COMMANDS:
        current_user.display_current_map()
    elif action in c.AVAILABLE_ACTION_COMMANDS:
        display_action_list(c.main_game_command_lists)
    # Unlock a location each time user did the corresponding task
    elif action.lower().strip() in c.HELP_COMMANDS:
        action = mmf.interact_help_menu(prompt_action_loop,[current_user])
    check_quit_command(current_user,action)
    return action


def prompt_action():
    """Function to prompt users for their action in main game world"""
    prompt = '\nHmmm... what do you wanna do?'
    prompt += " (press 'help' to seek for help)"
    print(prompt)
    action = input('> ')
    return action


def display_user_information(current_user):
    """Function to display user's information"""
    message = f"\nYou are {current_user.save_info['name']}, {current_user.save_info['age']} years old."
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
        print()
    print(f"You are a {current_user.save_info['title']} at UEA.")
    current_user.show_progress()


# 20. Use case: Log out of the system
def quit_game(current_user):
    """Function to print a farewell message to user, auto-save, and quit the game"""
    name = current_user.save_info['name']
    message = (f"\nFarewell {name}! Hope to see you soon in another UEA Adventure...")
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    # Auto-save user's progress
    save_progress(current_user)
    sys.exit()


def check_quit_command(current_user, command):
    """Function to check if user input is a quit command -> quit game"""
    check_quit = False
    if command.lower().strip() in c.QUIT_COMMANDS:
        check_quit = True
        quit_game(current_user)
    return check_quit


def save_progress(current_user):
    """Function to save current user's progress -> return a new list of users"""
    # Retrieve existing users
    users = load_existing_users()
    user_exist = False
    for user in users:
        # If user already exist -> replace new progress of current user
        if current_user.username == user['username']:
            user_exist = True
            users.remove(user)
            users.append(current_user.save_info)
            break
    # If user does not exist -> save progress of current user
    if user_exist == False:
        users.append(current_user.save_info)
    # Convert users list to string to write into a text file
    users_string = fc.TXTFile.convert_list_to_string(users)
    fc.TXTFile.save_users_data(users_string)
    return users


# Other functions
def load_existing_users():
    """Function to load existing users's data"""
    # Initialize users data as an empty list, and a default admin user
    users = []
    admin = uc.Admin('admin','tda21hwu',current_location=m.bed_room,inventory={},name='Minh',age=24,gender='Male',height=175,weight=60,title='Admin')
    # if-else block:
    #   - If there is no file exists to load data -> if block to save admin into a list and then write to the file
    #   - If there exists a file to load data -> try to load data -> If there are no users in the database -> save admin    
    users_file = fc.TXTFile('Data/existing_users.txt')
    users_string = users_file.load_users_data()
    if users_string == '':
        users = [admin.save_info]
        # Convert users list to string to write into a text file
        users_string = fc.TXTFile.convert_list_to_string(users)
        users_file.save_data(users_string)
    else:
        users = fc.TXTFile.convert_string_to_list(users_string)
    return users


def display_action_list(action_list):
    """Function to valid display action list"""
    message = '\nActions you can do in UEA Adventure:'
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    for action in action_list:
        if action == c.CHECK_USERS_COMMANDS:
            print(f"- '{action[0]}' (for Admin only)")
        else:
            print(f"- '{action[0]}'")


def check_user_information():
    """Function to check users' information"""
    users = load_existing_users()
    message = '\nHere is the list of all current users:'
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    for user in users:
        print(f"- {user['username']}")


def check_valid_command(command, command_type):
    """Function to detect invalid commands -> return a valid command"""
    while command.lower().strip() not in command_type:
        if command.lower().strip() not in command_type:
            command = input('Invalid command! Please try again: ')
            mmf.check_quit_command(command)
        else:
            break
    return command