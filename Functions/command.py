"""
Module to define user's commands and functions to interact with them
    1. Main menu commands: new game, login, help, quit
    2. Main game commands: me, move, inspect, search item, inventory, help, quit, pick up item, save, map, action
    3. Test commands: yes, no
    4. Admin's commands: check user's information
"""

import Functions.map as m
import Functions.inventory as inv

# MAIN MENU COMMANDS: new game, log in, help, quit, back #
NEW_GAME_COMMANDS = ['new game','n','ng','new','newgame','gamenew','start','go','play','register']
LOGIN_COMMANDS = ['login','log in','log']
HELP_COMMANDS = ['help','h','save me']
QUIT_COMMANDS = ['quit','q','stop','break','shut down','log out','log off','out','shut']
BACK_COMMANDS = ['back','b']

menu_command_lists = [
    NEW_GAME_COMMANDS,
    LOGIN_COMMANDS,
    HELP_COMMANDS,
    QUIT_COMMANDS,
    BACK_COMMANDS,
    ]

# Concatenate small command lists into a big command list
VALID_MENU_COMMANDS = []
for command in menu_command_lists:
    VALID_MENU_COMMANDS += command

# MAIN GAME LOOP COMMANDS: me, move, inspect, search item, inventory, pick up item, help, quit, save, map, action, world objects #
# ME -> DISPLAY USER'S INFORMATION #
ME_COMMANDS = ['me','myself','i','self']

# MOVE #
MOVE_COMMANDS = ['move','go','walk','travel','run','fly','forward']
MOVE_UP_COMMANDS = ['up','u']
MOVE_DOWN_COMMANDS = ['down','d','do','dow'] 
MOVE_LEFT_COMMANDS = ['left','l','le','lef']
MOVE_RIGHT_COMMANDS = ['right','r','ri','rig','righ']

move_command_lists = [
    MOVE_UP_COMMANDS,
    MOVE_DOWN_COMMANDS,
    MOVE_LEFT_COMMANDS,
    MOVE_RIGHT_COMMANDS,
    ]

# Concatenate small command lists into a big command list
VALID_MOVE_COMMANDS = []
for command in move_command_lists:
    VALID_MOVE_COMMANDS += command

# INSPECT #
INSPECT_COMMANDS = ['inspect','look','examine','search','check']

# SEARCH ITEM #
INSPECT_ITEM_COMMANDS = ['search item','inspect item','look at item','examine item','check item','inspectitem']

# DISPLAY INVENTORY #
INVENTORY_COMMANDS = ['inventory','inv','invent']

# PICK UP ITEM #
PICKUP_ITEM_COMMANDS = ['pick up','pick','pickup','take']

# SAVE GAME #
SAVE_COMMANDS = ['save','save game','remember','remember me']

# ADMIN COMMANDS: check users #
CHECK_USERS_COMMANDS = ['check user','checkuser']

# MAP COMMANDS #
DISPLAY_MAP_COMMANDS = ['map','direction','show map','world']

# ACTION COMMAND #
AVAILABLE_ACTION_COMMANDS = ['action','command','help action']

# WORLD OBJECTS #
world_objects = []

for key in m.world_dicts.keys():
    world_objects.append(key.lower().strip())

for key in inv.item_dicts.keys():
    world_objects.append(key.lower().strip())

# MAIN GAME COMMAND LIST #
main_game_command_lists = [
    ME_COMMANDS,
    MOVE_COMMANDS,
    INSPECT_COMMANDS,
    INSPECT_ITEM_COMMANDS,
    INVENTORY_COMMANDS,
    PICKUP_ITEM_COMMANDS,
    SAVE_COMMANDS,
    DISPLAY_MAP_COMMANDS,
    AVAILABLE_ACTION_COMMANDS,
    CHECK_USERS_COMMANDS,
    HELP_COMMANDS,
    QUIT_COMMANDS,
    ]

# Concatenate small command lists into a big command list
VALID_MAIN_GAME_COMMANDS = []
for command in main_game_command_lists:
    VALID_MAIN_GAME_COMMANDS += command

# DO TEST COMMANDS: yes,no #
# YES
YES_COMMANDS = ['yes','y','ye','yep','sure','ok']
NO_COMMANDS = ['no','n','none','thanks','nope']

test_command_lists = [YES_COMMANDS, NO_COMMANDS]

# Concatenate small command lists into a big command list
VALID_TEST_COMMANDS = []
for command in test_command_lists:
    VALID_TEST_COMMANDS += command