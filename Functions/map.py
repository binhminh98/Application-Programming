"""
Modulde to generate game world's maps and 
functions that interact with the game world's maps:
    1. World map: Include Buildings
    2. Building map: Include Rooms
    3. Lecture Room map: Include Chapters
    4. Chapters
Every location-related Class has the last parameter (a dictionary) containing its smaller part
-> Initializing from smallest to largest: 1.Chapters => 2.Rooms => 3.Building => 4.World

Map summary:
//////////////////////////////////////////////////////////////////////////////////////////////////////
/                             leaderboard                                                            /
/                                  |                                                                 /
/  bedroom		        hall of fame entrance (locked)                                               /
/     |                            |                                                                 /
/  living room - home entrance - wolrd - school entrance            AP Test 1            AP Test 5   /
/                                               |                       |                    |       /
/                                 DB Room - CMP School - AP Room - AP Lecture 1 - ... - AP Lecture 5 /
/                                               |                                                    /
/                                            RT Room                                                 /
//////////////////////////////////////////////////////////////////////////////////////////////////////
"""

import Classes.world_object_class as woc

### INITIALIZING WORLD LOCATIONS ###

# 1. Initializing chapters # 
# 1.1 Application Programming module's chapters: 5 lectures and 5 tests #
# Only the room Application Programming has chapters (DB and RT for further development) #

# AP LECTURES #
ap_lecture_1 = woc.Chapter('AP Lecture 1','This is Lecture 1 of AP','ap_lecture_1.txt','Lecture',False)
ap_lecture_2 = woc.Chapter('AP Lecture 2','This is Lecture 2 of AP','ap_lecture_2.txt','Lecture',True,'badge ap 1')
ap_lecture_3 = woc.Chapter('AP Lecture 3','This is Lecture 3 of AP','ap_lecture_3.txt','Lecture',True,'badge ap 2')
ap_lecture_4 = woc.Chapter('AP Lecture 4','This is Lecture 4 of AP','ap_lecture_4.txt','Lecture',True,'badge ap 3')
ap_lecture_5 = woc.Chapter('AP Lecture 5','This is Lecture 5 of AP','ap_lecture_5.txt','Lecture',True,'badge ap 4')

# AP TESTS #
ap_test_1 = woc.TestChapter('AP Test 1','This is Test 1 of AP','ap_test_1.txt','Test',True,'lecture note ap 1')
ap_test_2 = woc.TestChapter('AP Test 2','This is Test 2 of AP','ap_test_2.txt','Test',True,'lecture note ap 2')
ap_test_3 = woc.TestChapter('AP Test 3','This is Test 3 of AP','ap_test_3.txt','Test',True,'lecture note ap 3')
ap_test_4 = woc.TestChapter('AP Test 4','This is Test 4 of AP','ap_test_4.txt','Test',True,'lecture note ap 4')
ap_test_5 = woc.TestChapter('AP Test 5','This is Test 5 of AP','ap_test_5.txt','Test',True,'lecture note ap 5')

# AP CHAPTERS DICTIONARY #
ap_lectures_dict = {
    'AP Lecture 1': ap_lecture_1,
    'AP Lecture 2': ap_lecture_2,
    'AP Lecture 3': ap_lecture_3,
    'AP Lecture 4': ap_lecture_4,
    'AP Lecture 5': ap_lecture_5,
}

ap_tests_dict = {
    'AP Test 1': ap_test_1,
    'AP Test 2': ap_test_2,
    'AP Test 3': ap_test_3,
    'AP Test 4': ap_test_4,
    'AP Test 5': ap_test_5,
}

# 2. Initializing rooms #
# 2.1 Initializing School's rooms #
cmp = woc.Room('cmp school',"You are standing at the Computing Science School's main hall",'cmp.txt','room',False)
ap = woc.LectureRoom('ap room','Room for Application Programming module','ap.txt','lecture room','',False,'',5)
db = woc.LectureRoom('db room','Room for Database Manipulation module','db.txt','lecture room','tda21hwu',True)
rt = woc.LectureRoom('rt room','Room for Research Techniques module','rt.txt','lecture room','tda21hwu',True)

school_rooms_dict = {
    'cmp school': cmp,
    'ap room': ap,
    'db room': db,
    'rt room': rt,
}

# 2.2 Initializing Home's rooms #
bed_room = woc.Room('bedroom','This is your bedroom','bed_room.txt','room',False)
living_room = woc.Room('living room','This is your living room','living_room.txt','room',True,'backpack')

home_rooms_dict = {
    'bedroom': bed_room,
    'living room': living_room,
}

# 2.3 Initializing Hall of fame's rooms #
leaderboard = woc.Room('leaderboard','All gifted students will be remembered forever!','leaderboard.txt','room',True,'msc data science degree')

hof_rooms_dict = {
    'leaderboard': leaderboard
}

# 3. Initializing buildings in game world #
school = woc.Building('school entrance','Welcome to UEA!','school.txt','building',False)
home = woc.Home('home entrance','You are standing at the front door of your home','','home.txt','building',True,'transcript')
hall_of_fame = woc.HallOfFame('hall of fame entrance','Welcome champion, to the Hall of Fame!!!',None,'hall_of_fame.txt','building',True,'badge ap 5')

school.rooms = school_rooms_dict
home.rooms = home_rooms_dict
hall_of_fame.rooms = hof_rooms_dict

building_dict = {
    'school entrance': school,
    'home entrance': home,
    'hall of fame entrance': hall_of_fame,
}

# 4. Initializing game world #

world = woc.WorldObject('world','You are currently in Norwich, United Kingdom!','world.txt','world',False)

world_dicts = {'world': world}
for dict in [building_dict,hof_rooms_dict,home_rooms_dict,school_rooms_dict,ap_lectures_dict,ap_tests_dict]:
    world_dicts.update(dict)

# GENERATE A LIST OF LOCATIONS THAT CONTAIN INTERACTIVE ITEMS #
location_contains_items = {}
location_contains_items.update(home_rooms_dict)
location_contains_items['hall of fame entrance'] = hall_of_fame
location_contains_items.update(ap_lectures_dict)
location_contains_items.update(ap_tests_dict)

### GENERATING MAP'S DIRECTIONS ###
# AP ROOM #
# AP LECTURES #
"""
Map summary:
//////////////////////////////////////////////////////////////////////////////////////
/                                                                                    /
/           AP Test 1       AP Test 2      AP Test 3      AP Test 4      AP Test_5   /
/               |               |              |              |              |       /
/ AP Room - AP Lecture 1 - AP Lecture 2 - AP Lecture 3 - AP Lecture 4 - AP Lecture_5 /
/                                                                                    /
//////////////////////////////////////////////////////////////////////////////////////
"""
# AP LECTURE 1 #
ap_lecture_1.directions['up'] = ap_test_1
ap_lecture_1.directions['down'] = None
ap_lecture_1.directions['left'] = ap
ap_lecture_1.directions['right'] = ap_lecture_2

# AP LECTURE 2 #
ap_lecture_2.directions['up'] = ap_test_2
ap_lecture_2.directions['down'] = None
ap_lecture_2.directions['left'] = ap_lecture_1
ap_lecture_2.directions['right'] = ap_lecture_3

# AP LECTURE 3 #
ap_lecture_3.directions['up'] = ap_test_3
ap_lecture_3.directions['down'] = None
ap_lecture_3.directions['left'] = ap_lecture_2
ap_lecture_3.directions['right'] = ap_lecture_4

# AP LECTURE 4 #
ap_lecture_4.directions['up'] = ap_test_4
ap_lecture_4.directions['down'] = None
ap_lecture_4.directions['left'] = ap_lecture_3
ap_lecture_4.directions['right'] = ap_lecture_5

# AP LECTURE 5 #
ap_lecture_5.directions['up'] = ap_test_5
ap_lecture_5.directions['down'] = None
ap_lecture_5.directions['left'] = ap_lecture_4
ap_lecture_5.directions['right'] = None

### AP TESTS ###
# AP TEST 1 #
ap_test_1.directions['up'] = None
ap_test_1.directions['down'] = ap_lecture_1
ap_test_1.directions['left'] = None
ap_test_1.directions['right'] = None

# AP TEST 2 #
ap_test_2.directions['up'] = None
ap_test_2.directions['down'] = ap_lecture_2
ap_test_2.directions['left'] = None
ap_test_2.directions['right'] = None

# AP TEST 3 #
ap_test_3.directions['up'] = None
ap_test_3.directions['down'] = ap_lecture_3
ap_test_3.directions['left'] = None
ap_test_3.directions['right'] = None

# AP TEST 4 #
ap_test_4.directions['up'] = None
ap_test_4.directions['down'] = ap_lecture_4
ap_test_4.directions['left'] = None
ap_test_4.directions['right'] = None

# AP TEST 5 #
ap_test_5.directions['up'] = None
ap_test_5.directions['down'] = ap_lecture_5
ap_test_5.directions['left'] = None
ap_test_5.directions['right'] = None

# SCHOOL BUILDING #
"""
Map summary:
////////////////////////////////////
/                                  /
/         school entrance          /
/               |                  /
/  DB Room - CMP School - AP Room  /
/               |                  /
/             RT Room              /
/                                  /
////////////////////////////////////
"""
# CMP MAIN HALL #
cmp.directions['up'] = school
cmp.directions['down'] = rt
cmp.directions['left'] = db
cmp.directions['right'] = ap

# APPLICATION PROGRAMMING ROOM #
ap.directions['up'] = None
ap.directions['down'] = None
ap.directions['left'] = cmp
ap.directions['right'] = ap_lecture_1

# DB Manipulation and Research Techniques rooms are locked for further development (password: tda21hwu) #
db.directions['up'] = None
db.directions['down'] = None
db.directions['left'] = None
db.directions['right'] = cmp

rt.directions['up'] = cmp
rt.directions['down'] = None
rt.directions['left'] = None
rt.directions['right'] = None

# HOME BUILDING #
"""
Map summary:
//////////////////////////////////
/                                /
/     bedroom                    /
/        |                       /
/   living room - home entrance  /
/                                /
//////////////////////////////////
"""
# BEDROOM #
bed_room.directions['up'] = None
bed_room.directions['down'] = living_room
bed_room.directions['left'] = None
bed_room.directions['right'] = None

# LIVING ROOM #
living_room.directions['up'] = bed_room
living_room.directions['down'] = None
living_room.directions['left'] = None
living_room.directions['right'] = home

# HALL OF FAME BUILDING #
"""
Map summary:
/////////////////////////
/                       /
/       leaderboard     /
/            |          /
/ hall of fame entrance /
/                       /
/////////////////////////
"""
# LEADERBOARD #
leaderboard.directions['up'] = None
leaderboard.directions['down'] = hall_of_fame
leaderboard.directions['left'] = None
leaderboard.directions['right'] = None

# GAME WORLD #
"""
Map summary:
////////////////////////////////////////////
/                                          /
/          hall of fame entrance           /
/                    |                     /
/  home entrance - world - school entrance /
/                                          /
////////////////////////////////////////////
"""
# SCHOOL BUILDING #
school.directions['up'] = None
school.directions['down'] = cmp
school.directions['left'] = world
school.directions['right'] = None

# HOME BUILDING #
home.directions['up'] = None
home.directions['down'] = None
home.directions['left'] = living_room
home.directions['right'] = world

# HALL OF FAME BUILDING -> can only enter after earning a degree #
hall_of_fame.directions['up'] = leaderboard
hall_of_fame.directions['down'] = world
hall_of_fame.directions['left'] = None
hall_of_fame.directions['right'] = None

# WOLRD #
world.directions['up'] = hall_of_fame
world.directions['down'] = None
world.directions['left'] = home
world.directions['right'] = school