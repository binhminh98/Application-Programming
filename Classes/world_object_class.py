"""
Module to define class WorldObject and its subclasses: 
    1. Building: Home, HallOfFame.
    2. Room: LectureRoom
    3. Chapter: TestChapter
"""

class WorldObject():
    """Defining class WorldObject"""

    def __init__(self, name, description, map_path='', type='', locked=False, unlock_item=None, **items):
        """Initializing attributes of class Building"""
        self.name = name
        self.description = description
        self.map_path = map_path
        self.type = type
        self.locked = locked
        self.unlock_item = unlock_item
        self.items = items # Dictionary containing information about the world's objects
        # An dictionary of the building's directions
        self.directions = {
            'up': None,
            'down': None,
            'left': None,
            'right': None,
            }

# 1. BUILDING CLASS AND ITS SUBCLASSES: Home, HallOfFame #
class Building(WorldObject):
    """Defining subclass Building"""

    def __init__(self, name, description, map_path='', type='', locked=False, unlock_item=None,**items):
        """Initializing attributes of subclass Building"""
        super().__init__(name, description, map_path, type, locked, unlock_item, **items)
        self.rooms = {}


class Home(Building):
    """Defining subclass Home"""

    def __init__(self, name, description, owner, map_path='', type='', locked=False, unlock_item=None, **items):
        """Initializing attributes of subclass Home"""
        super().__init__(name, description, map_path, type, locked, unlock_item, **items)
        self.owner = owner


class HallOfFame(Building):
    """Defining subclass HallOfFame"""

    def __init__(self, name, description, leaderboard, map_path='', type='', locked=True, unlock_item=None, **items):
        """Initializing attributes of subclass HallOfFame -> locked until one user finised the game"""
        super().__init__(name, description, map_path, type, locked, unlock_item, **items)
        self.leaderboard = leaderboard

# 2. ROOM CLASS AND ITS SUBCLASS: LectureRoom #
class Room(WorldObject):
    """Defining class Room"""

    def __init__(self, name, description, map_path='', type='', locked=False, unlock_item=None, **items):
        """Initializing attributes of class Room"""
        super().__init__(name, description, map_path, type, locked, unlock_item, **items)


class LectureRoom(Room):
    """Defining subclass LectureRoom"""

    def __init__(self, name, description, map_path='', type='', password='', locked=False, unlock_item=None, total_tests=0, finished=False, **items):
        """Initializing attributes of subclass LectureRoom"""
        super().__init__(name, description, map_path, type, locked, unlock_item, **items)
        self.password = password
        self.total_tests = total_tests
        self.finished = finished

# 3. CHAPTER CLASS AND ITS SUBCLASS: TestChapter #
class Chapter(WorldObject):
    """Defining class Chapter"""

    def __init__(self, name, description, map_path='', type='', locked=False, unlock_item=None, **items):
        """Initializing attributes of class Chapter"""
        super().__init__(name, description, map_path, type, locked, unlock_item,**items)


class TestChapter(Chapter):
    """Defining subclass TestChapter"""

    def __init__(self, name, description, map_path='', type='', locked=False, unlock_item=None, solved=False, **items):
        super().__init__(name, description, map_path, type, locked, unlock_item, **items)
        """Initializing attributes of subclass TestChapter"""
        self.solved = solved