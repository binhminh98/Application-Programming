"""
Module to
1.  Generate inventory and items in the game world:
    1.1. Inventory
    1.2. Tests
    1.3. Badges
    1.4. LectureNote
    1.5. Transcript
    1.6. Degree
    1.7. Backpack
2. Add items to their location on the map:
    living room: {transcript}
    CMP School: {degree}
    bedroom: {backpack}
    hall of fame: {degree}
    AP Lecture 1: {lecturenote_ap_1}
    AP Lecture 2: {lecturenote_ap_2}
    AP Lecture 3: {lecturenote_ap_3}
    AP Lecture 4: {lecturenote_ap_4}
    AP Lecture 5: {lecturenote_ap_5}
    AP Test 1: {test_ap_1, badge_ap_1}
    AP Test 2: {test_ap_2, badge_ap_2}
    AP Test 3: {test_ap_3, badge_ap_3}
    AP Test 4: {test_ap_4, badge_ap_4}
    AP Test 5: {test_ap_5, badge_ap_5}    
"""

import Functions.map as m
import Classes.item_class as ic

# 1. GENERATE TESTS -> ADD TO THEIR LOCATION ON THE MAP #
test_ap_1 = ic.Test('test ap 1','This is the test paper for AP lecture 1','Test','ap_test_1',True,False,'ap room')
test_ap_2 = ic.Test('test ap 2','This is the test paper for AP lecture 2','Test','ap_test_2',True,False,'ap room')
test_ap_3 = ic.Test('test ap 3','This is the test paper for AP lecture 3','Test','ap_test_3',True,False,'ap room')
test_ap_4 = ic.Test('test ap 4','This is the test paper for AP lecture 4','Test','ap_test_4',True,False,'ap room')
test_ap_5 = ic.Test('test ap 5','This is the test paper for AP lecture 5','Test','ap_test_5',True,False,'ap room')
m.ap_test_1.items['test ap 1'] = test_ap_1
m.ap_test_2.items['test ap 2'] = test_ap_2
m.ap_test_3.items['test ap 3'] = test_ap_3
m.ap_test_4.items['test ap 4'] = test_ap_4
m.ap_test_5.items['test ap 5'] = test_ap_5

test_ap_dict = {
    'test ap 1': test_ap_1,
    'test ap 2': test_ap_2,
    'test ap 3': test_ap_3,
    'test ap 4': test_ap_4,
    'test ap 5': test_ap_5,
}

# 2. GENERATE CONSTANT BADGES -> ADD TO THEIR LOCATION ON THE MAP #
badges_ap_1 = ic.Badge('badge ap 1','A Badge with the title:','Badge','ap_test_1',False,False,'Software engineer expert')
badges_ap_2 = ic.Badge('badge ap 2','A Badge with the title:','Badge','ap_test_2',False,False,'Agile master')
badges_ap_3 = ic.Badge('badge ap 3','A Badge with the title:','Badge','ap_test_3',False,False,'King of hello world!')
badges_ap_4 = ic.Badge('badge ap 4','A Badge with the title:','Badge','ap_test_4',False,False,"Python's conqueror")
badges_ap_5 = ic.Badge('badge ap 5','A Badge with the title:','Badge','ap_test_5',False,False,'__PYTHON MASTER__')

m.ap_test_1.items['badge ap 1'] = badges_ap_1
m.ap_test_2.items['badge ap 2'] = badges_ap_2
m.ap_test_3.items['badge ap 3'] = badges_ap_3
m.ap_test_4.items['badge ap 4'] = badges_ap_4
m.ap_test_5.items['badge ap 5'] = badges_ap_5

badge_ap_dict = {
    'badge ap 1': badges_ap_1,
    'badge ap 2': badges_ap_2,
    'badge ap 3': badges_ap_3,
    'badge ap 4': badges_ap_4,
    'badge ap 5': badges_ap_5,    
}

# 3. GENERATE CONSTANT LECTURENOTE -> ADD TO THEIR LOCATION ON THE MAP #
lecturenote_ap_1 = ic.LectureNote('lecture note ap 1','This is the first Lecture note of AP Module','Lecture Note','ap_lecture_1',True,False)
lecturenote_ap_2 = ic.LectureNote('lecture note ap 2','This is the second Lecture note of AP Module','Lecture Note','ap_lecture_2',True,False)
lecturenote_ap_3 = ic.LectureNote('lecture note ap 3','This is the third Lecture note of AP Module','Lecture Note','ap_lecture_3',True,False)
lecturenote_ap_4 = ic.LectureNote('lecture note ap 4','This is the fourth Lecture note of AP Module','Lecture Note','ap_lecture_4',True,False)
lecturenote_ap_5 = ic.LectureNote('lecture note ap 5','This is the final Lecture note of AP Module','Lecture Note','ap_lecture_5',True,False)

m.ap_lecture_1.items['lecture note ap 1'] = lecturenote_ap_1
m.ap_lecture_2.items['lecture note ap 2'] = lecturenote_ap_2
m.ap_lecture_3.items['lecture note ap 3'] = lecturenote_ap_3
m.ap_lecture_4.items['lecture note ap 4'] = lecturenote_ap_4
m.ap_lecture_5.items['lecture note ap 5'] = lecturenote_ap_5

lecturenote_ap_dict = {
    'lecture note ap 1': lecturenote_ap_1,
    'lecture note ap 2': lecturenote_ap_2,
    'lecture note ap 3': lecturenote_ap_3,
    'lecture note ap 4': lecturenote_ap_4,
    'lecture note ap 5': lecturenote_ap_5,    
    }

# 4. GENERATE TRANSCRIPT -> ADD TO ITS LOCATION ON THE MAP #
transcript = ic.Transcript('transcript',"This is your transcript of the MSc. Data Science. Pick it up to go outside.\nYou can also type 'me' to see your progress!",'Transcript','living room',True,False,'MSc. Data Science')

transcript_dict = {
    'transcript': transcript,
}

m.living_room.items['transcript'] = transcript

# 5. DEGREE -> ADD TO ITS LOCATION ON THE MAP #
degree_ap = ic.Degree('','msc data science degree','This is the prestige degree of MSc. Data Science','Degree','hall of fame entrance',True,False,'MSc. Data Science')

degree_dict = {
    'msc data science degree': degree_ap,
}

m.hall_of_fame.items['msc data science degree'] = degree_ap

# 6. BACKPACK -> ADD TO ITS LOCATION ON THE MAP #
backpack = ic.Item('backpack','This is your backpack. Pick it up to open Living Room!','Backpack','bedroom',True,False)

backpack_dict = {
    'backpack': backpack,
}

m.bed_room.items['backpack'] = backpack

# UPDATE DICTIONARY OF ITEMS THAT CAN BE PICKED UP #
unpickable_item_dicts = {}
for dict in [test_ap_dict,lecturenote_ap_dict]:
    unpickable_item_dicts.update(dict)

# UPDATE THE DICTIONARY OF ALL ITEMS #
item_dicts = {}
for dict in [backpack_dict,degree_dict,transcript_dict,lecturenote_ap_dict,badge_ap_dict,test_ap_dict]:
    item_dicts.update(dict)