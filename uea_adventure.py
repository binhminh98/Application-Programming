"""
Main module of the game loop
-----------UEA Adventure-------------
"""

import Functions.main_menu_function as mmf
import Functions.main_game_function as mgf

### MAIN GAME LOOP ###

# LOAD EXISTING USERS #
users = mgf.load_existing_users()

### 1: MAIN MENU ###
current_user = mmf.interact_title_screen()

### 2: MAIN GAME PLAY ###
# Main game loop #

while True:
    mgf.prompt_action_loop(current_user)