"""
Module to define functions in the main menu
"""

import Content.AP.ap_content as ac
import Classes.file_class as fc
import Classes.user_class as uc
import Functions.command as c
import Functions.map as m
import Functions.main_game_function as mgf
import Functions.inventory as inv
import sys
import time

# 1. Use case: Start game #
def display_title_screen():
    """
    Function to display the title screen.
    All graphics files are read from text files in the Graphics folder
    """
    # Generate file
    title_screen = fc.TXTFile('Graphics/title_screen.txt','r')
    # Print content of the file line by line
    title_screen.print_content()
    print()


def interact_title_screen():
    """Function to interact with the title screen"""
    # Display the title screen
    display_title_screen()
    # Prompt user to choose an option
    command = input('Please choose an option to continue: ')
    command = mgf.check_valid_command(command,c.VALID_MENU_COMMANDS)
    print()
    # Convert user's command to lowercase and
    # check with the lists of potential commands
    current_user = uc.User()
    if command.lower().strip() in c.NEW_GAME_COMMANDS:
        current_user = register_new_user()
        current_user = create_character(current_user)
        greet_new_users(current_user)
    elif command.lower().strip() in c.LOGIN_COMMANDS:
        current_user = log_in()
    elif command.lower().strip() in c.HELP_COMMANDS:
        current_user = interact_help_menu(interact_title_screen)
    check_quit_command(command)
    return current_user


# 2. Use case: See Help menu
def interact_help_menu(function=None,parameters=[]):
    """
    Function to interact with the help menu -> return a command
    When user types 'back' -> return to the previous activity
    """
    # Display help menu
    display_help_menu()
    # Prompt user for 'back' command
    command = input("Type 'back' when you finish reading: ")
    check_quit_command(command)
    command = mgf.check_valid_command(command,c.BACK_COMMANDS)
    if function == None:
        pass
    else:
        if parameters == []:
            return_value = function()
        elif len(parameters) == 1:
            parameter = parameters[0]
            return_value = function(parameter)
        elif len(parameters) == 2:
            parameter_1 = parameters[0]
            parameter_2 = parameters[1]
            return_value = function(parameter_1,parameter_2)
    return return_value


def display_help_menu():
    """
    Function to display the help menu.
    All graphics files are read from text files in the Graphics folder
    """
    # Generate file
    help_menu = fc.TXTFile('Graphics/help.txt','r')
    # Print from file line by line
    help_menu.print_content()
    print()


# 3. Use case: Quit game
def check_quit_command(command):
    """Function to check if unidentified user's input is a quit command -> quit game"""
    check_quit = False
    if command.lower().strip() in c.QUIT_COMMANDS:
        check_quit = True
        quit_game()
    return check_quit


def quit_game():
    """Function to print a farewell message to unidentified user and quit the game"""
    message = (f"Farewell, gamer! Hope to see you soon in another UEA Adventure...")
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    sys.exit()


# 4. Use case: Login - register with username/password
def register_new_user():
    """Function to register new user into the database -> return the current user"""
    # Initialize current user as a NewUser
    current_user = uc.NewUser()
    create_username(current_user)
    create_password(current_user)
    return current_user


def create_username(current_user):
    """Function to create username"""
    current_user.username = input('Please enter your username (Maximum 12 words or numbers): ')
    check_quit_command(current_user.username)
    if current_user.username.lower().strip() in c.HELP_COMMANDS:
        current_user.username = interact_help_menu(create_username,current_user)
    current_user.username = check_string_length('username',current_user.username,12)
    current_user.username = check_existing_username(current_user,current_user.username)
    # Store username in the demographic dictionary
    current_user.save_info['username'] = current_user.username
    print()
    return current_user.username


def check_existing_username(current_user,input_username):
    """Function to check if username exists or not"""
    # 1. Flag: user_existance to check if input_username exists in users list
    # 2. For loop: check each user's dictionary for their username
    #   - If input_username does not exists in the dictionary:
    #       + Flag = False, self.username = input_username, break
    #   - Else:
    #       + Continue to the next user's dictionary
    # 3. While loop:
    #   - If after the for loop username_existance == True 
    #       + Re-enter username and start over with a False flag
    username_existence = False
    while username_existence == False:
        for user in current_user.users:
            if input_username == user['username']:
                current_user.username = input_username
                username_existence = True
                break
            else:
                continue
        if username_existence == True:
            input_username = input('Username has already exist! Please re-enter your username: ')
            check_quit_command(input_username)
            username_existence = False
        else:
            break
    return current_user.username


def create_password(current_user):
    """Function to create password"""
    current_user.password = input('Set your password (Maximum 8 words or numbers): ')
    check_quit_command(current_user.password)
    if current_user.password.lower().strip() in c.HELP_COMMANDS:
        current_user.password = interact_help_menu(create_username,current_user)
    current_user.password = check_string_length('password',current_user.password,8)
    confirm_password(current_user)
    # Store password in the demographic dictionary
    current_user.save_info['password'] = current_user.password
    print()
    return current_user.password


def confirm_password(current_user):
    """Function to confirm password"""
    confirmed_password = input('Please re-enter to confirm your password: ')
    check_quit_command(confirmed_password)
    # A while loop to check input password against re-enter password 
    while current_user.password != confirmed_password:
        if current_user.password == confirmed_password:
            break
        else:
            confirmed_password = input('Password incorrect, please re-enter to confirm your password: ')
            check_quit_command(confirmed_password)


def log_in():
    """
    Function for old user to log into the system 
    -> return the current user information from the database
    """
    # 1. Verify login of an user
    # 2. Greet user according to their role
    current_user = verify_login()
    if check_admin(current_user) == True:
        # Defining Admin user
        admin = uc.Admin('admin','tda21hwu',current_location=m.bed_room,inventory={},name='Minh',age=24,gender='Male',height=175,weight=60,title='Admin')
        current_user = admin
        current_user = load_user_progress(current_user)
        if current_user.current_location.name == 'leaderboard':
            print(f"\nHello {current_user.save_info['name']}, you have already won the game!")
            current_user_details = f"- {current_user.username} - Level: {current_user.level} - Degree classification: {current_user.inventory['msc data science degree'].classification}"
            for character in current_user_details:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            sys.exit()
        greeting_admin(current_user)
    else:
        current_user = load_user_progress(current_user)
        if current_user.current_location.name == 'leaderboard':
            print(f"\nHello {current_user.save_info['name']}, you have already won the game!")
            current_user_details = f"- {current_user.username} - Level: {current_user.level} - Degree classification: {current_user.inventory['msc data science degree'].classification}"
            for character in current_user_details:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            print()
            sys.exit()
        greeting_old_users(current_user)
    return current_user


def load_user_progress(current_user):
    """Function to load current user's progress"""
    # Retrieve list of existing users
    users = mgf.load_existing_users()
    user = load_user_information(current_user,users)
    load_user_inventory(current_user,user)
    load_user_location(current_user,user)
    auto_unlock_location(current_user)
    return current_user


def load_user_information(current_user,users):
    """Function to load current user's information"""
    for user in users:
        # Retrieve user's information (user: a dictionary) from the database
        if current_user.username == user['username']:
            # Load current user's attributes from the user dictionary
            current_user.save_info = user
            for key in user.keys():
                setattr(current_user, key, user[key])
            break
    return user


def load_user_inventory(current_user,user):
    """Function to load current user's inventory"""
    # Retrieve inventory information from the data file to save_info dict
    current_user.save_info['inventory'] = user['inventory']
    # Add each owned item in the save file to current user's inventory
    current_user.inventory = {}
    for owned_item in user['inventory']:
        # Search the owned item in the items dictionary
        for item in inv.item_dicts.values():
            if owned_item['name'] == item.name:
                # Load item's attributes from the owned_item dictionary
                for key in owned_item.keys():
                    setattr(item, key, owned_item[key]) 
                current_user.inventory[item.name] = item
                break


def load_user_location(current_user,user):
    """Function to load current user's current location"""
    for location in m.world_dicts.values():
        if user['current_location'] == location.name:
            current_user.save_info['current_location'] = location.name
            current_user.current_location = location


def auto_unlock_location(current_user):
    """Function to automatic unlock saved locations after an old user log in"""
    # A for loop to go through each items in current user's inventory
    # -> unlock each item's corresponding location
    for item in current_user.inventory.keys():
        # A for loop to search for the corresponding location of the current 'item'
        # -> unlock the location
        for location in m.world_dicts.values():
            if item == location.unlock_item:
                location.locked = False
                break


# 5. Use case: Verify log-in/resgistration
def verify_login():
    """Function to verify login"""
    current_user = uc.OldUser()
    message = 'Please input your login details:'
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    input_username = str(input('\n- Username: '))
    if input_username in c.BACK_COMMANDS:
        interact_title_screen()
    check_quit_command(input_username)
    current_user.username = verify_username(current_user, input_username)
    input_password = str(input('- Password: '))
    if input_password in c.BACK_COMMANDS:
        interact_title_screen()
    check_quit_command(input_password)
    current_user.password = verify_password(current_user, input_password)
    return current_user


def verify_username(current_user, input_username):
    """Function to check if username exists or not"""
    # 1. Flag: user_existance to check if input_username exists in users list
    # 2. For loop: check each user's dictionary for their username
    #   - If input_username is found in the dictionary:
    #       + Flag = True, self.username = input_username, break
    #   - Else:
    #       + Continue to the next user's dictionary
    # 3. While loop:
    #   - If after the for loop username_existance == False 
    #       + Re-enter username and start over
    users = mgf.load_existing_users()
    username_existance = False
    while username_existance == False:
        for user in users:
            if input_username == user['username']:
                current_user.username = input_username
                username_existance = True
                break
            else:
                continue
        if username_existance == False:
            input_username = input('Your username does not exist. Please re-enter your username: ')
            if input_username in c.BACK_COMMANDS:
                interact_title_screen()
            check_quit_command(input_username)
    return current_user.username


def verify_password(current_user, input_password):
    """Function to check if password is correct or not"""
    # 1. Flag: correct_password to check if input_password is correct for self.username
    # 2. For loop: check each user's dictionary for their username and password
    #   - If input_password is correct for self.username:
    #       + Flag = True
    #       + self.password = input_password
    #       + self.save_info = user dictionary, break
    #   - Else:
    #       + Continue to the next user's dictionary
    # 3. While loop:
    #   - If after the for loop username_existance == False 
    #       + Re-enter username and start over
    users = mgf.load_existing_users()
    correct_password = False
    while correct_password == False:
        for user in users:
            if current_user.username == user['username'] and input_password == user['password']:
                current_user.password = input_password
                current_user.save_info = user
                correct_password = True
                break
            else:
                continue
        if correct_password == False:
            input_password = input('Your password is incorrect. Please re-enter your password: ')
            check_quit_command(input_password)
    return current_user.password


def greeting_old_users(current_user):
    """Function to greet old users and show their current location"""
    message = (f"\nGreetings, {current_user.save_info['name']}. Welcome back to the game!")
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    message = f"\nYour current location: {current_user.current_location.name.title()}\n"
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    current_user.display_current_map()
    current_user.display_inventory()


def greeting_admin(current_user):
    """Function to greet admin and show their privileges"""
    current_user.privileges.display_privileges()
    message = f"\nYour current location: {current_user.current_location.name.title()}"
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    current_user.display_current_map()
    current_user.display_inventory()


def check_string_length(string_type, content, maximum_string_length):
    """
    Function to check username and password length -> returns a string
    Parameters: 
        - string_type: 'username' or 'password' (can be extended to check any strings)
        - content: content of the string being checked
        - maximum_string_length: maximum length of a string
    """
    while len(content) > maximum_string_length:
        if len(content) <= maximum_string_length:
            break
        else:
            content = input(f'{string_type.title()} too long. Please re-enter your {string_type}: ')
            check_quit_command(content)
            # Store information with the new input
    return content


def check_admin(current_user):
    """Function to check if the login user is Admin -> return a Flag"""
    is_admin = False
    if current_user.username == 'admin':
        is_admin = True
    return is_admin


# 6: Use case: Character creation
def create_character(current_user):
    """
    Function for character creation, store several attributes in the demographic dictionary
    """
    message = "Now, let's start with some basic questions about yourself."
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    input_name(current_user)
    input_age(current_user)
    input_gender(current_user)
    input_height(current_user)
    input_weight(current_user)
    input_title(current_user)
    return current_user


def input_name(current_user):
    """Function to prompt user for their full name"""
    first_name = input('First, let me know your first name: ')
    check_quit_command(first_name)
    last_name = input('\nSecond, let me know your last name: ')
    check_quit_command(last_name)
    full_name = f'{first_name.title()} {last_name.title()}'
    current_user.save_info['name'] = full_name
    return full_name


def input_age(current_user):
    """Function to prompt user for their age"""
    while True:
        age = input('\nThird, how old are you? (from 0-100): ')
        check_quit_command(age)
        try:
            while int(age) not in [i for i in range(0,101)]:
                age = input('Invalid age, please input your age (from 0-100): ')
            break
        except ValueError:
            print('Invalid age, try again...')
    current_user.save_info['age'] = age
    return age


def input_gender(current_user):
    """Function to prompt user for their gender"""
    while True:   
        gender = input('\nFourth, what is your gender? (Male , Female, Unknown): ')
        check_quit_command(gender)
        try:
            while gender.lower() not in ['male','female','unknown']:
                gender = input('Invalid gender, please input your gender (Male , Female, Unknown): ')
            break
        except ValueError:
            print('Invalid gender, try again...')
    current_user.save_info['gender'] = gender
    return gender


def input_height(current_user):
    """Function to prompt user for their height"""
    while True:
        height = input('\nFifth, input your height (from 70-230cm): ')
        check_quit_command(height)
        try:
            while int(height) not in [i for i in range(70,231)]:
                height = input('Invalid height, please input your height (from 70-230cm): ')
            break
        except ValueError:
            print('Invalid height, try again...')
    current_user.save_info['height'] = height
    return height


def input_weight(current_user):
    """Function to prompt user for their weight"""    
    while True:
        weight = input('\nSixth, input your weight (from 30-200kg): ')
        check_quit_command(weight)
        try:
            while int(weight) not in [i for i in range(30,201)]:
                weight = input('Invalid weight, please input your weight (from 30-200kg): ')
            break
        except ValueError:
            print('Invalid weight, try again...')
    current_user.save_info['weight'] = weight
    return weight


def input_title(current_user):
    """Function to prompt user for their title"""
    while True:
        title = input('\nLast but not least, please choose your title (Student, Teacher): ')
        check_quit_command(title)
        try:
            while title.lower() not in ['student', 'teacher']:
                title = input('Invalid title, please input your title (Student, Teacher): ')
            break
        except ValueError:
            print('Invalid title, try again...')
    current_user.save_info['title'] = title
    return title


def greet_new_users(current_user):
    """Function to greet new users after they create an account"""
    message = f"\nGreetings, {current_user.save_info['name']}. Welcome to UEA Adventure!"
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    show_instruction(current_user) # Always show instruction for new users
    message = f"\nYour current location: {current_user.current_location.name.title()}\n"
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    current_user.display_current_map()
    current_user.display_inventory()


def show_instruction(current_user):
    """Function to show instruction of the game"""
    if current_user.save_info['title'] == 'student':
        message = "\nRight now, it is the beginning of a new semester and\n"
        message += "you are enrolling in MSc Data Science at UEA.\n"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        message = "You undertake 3 modules in this semester: Application Programming (AP),\n"
        message += "Database Manipulation (DB), and Research Techniques (RT). However,\n"
        message += "DB and RT are private classes so you could not attend unless you have a password.\n"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        message = "Try to finish all the tests in AP module to earn your Masters degree\n"
        message += "After that, your name will forever be remembered in the Hall Of Fame!!!\n\n"
        message += "I wish that you will earn a Distinction Degree.\n\n"
        message += "And have lots of fun playing UEA Adventure ^^\n\n"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
    if current_user.save_info['title'] == 'teacher':
        message = "\nRight now, it is the beginning of a new semester and\n"
        message += "you have to attend MSc Data Science at UEA to revise your knowledge.\n"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        message = "You undertake 3 modules in this semester: Application Programming (AP),\n"
        message += "Database Manipulation (DB), and Research Techniques (RT).\n"
        message += "However, DB and RT are private classes so you could not attend unless\n"
        message += "you have a password.\n"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        message = "Try to finish all the tests in AP module so you can continue teaching\n"
        message += "After that, your name will forever be remembered in the Hall Of Fame!!!\n\n"
        message += "And also, I wish that you will have lots of fun playing UEA Adventure ^^.\n"
        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        print()