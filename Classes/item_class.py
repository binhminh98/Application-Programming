"""
Module to define class Item and its subclasses: Transcript, Lecture Note, Badge, Test.
"""

class Item():
    """Defining class Item"""

    def __init__(self, name='', description='', type='', location='', availability=True, owned=False):
        """Initializing attributes of class Item"""
        self.name = name
        self.description = description
        self.type = type
        self.location = location
        self.availability = availability
        self.owned = owned


class Transcript(Item):
    """Defining subclass Transcript"""

    def __init__(self, name='', description='', type='', location='', availability=True, owned=False, degree='', gpa=''):
        """Initializing attributes of class Transcript"""
        super().__init__(name, description, type, location, availability, owned)
        self.degree = degree
        self.gpa = gpa


class Degree(Transcript):
    """Defining subclass of Transcript: Degree"""

    def __init__(self, classification='', name='', description='', type='', location='', availability=True, owned=False, degree='', gpa=''):
        """Initializing attributes of class Transcript"""
        super().__init__(name, description, type, location, availability, owned, degree, gpa)
        self.classification = classification


class LectureNote(Item):
    """Defining subclass Lecture Note"""

    def __init__(self, name='', description='', type='', location='', availability=True, owned=False, **content):
        """Initializing attributes of class Lecture Note"""
        super().__init__(name, description, type, location, availability, owned)
        self.content = content


class Badge(Item):
    """Defining subclass Badge"""

    def __init__(self, name='', description='', type='', location='', availability=True, owned=False, title=''):
        """Initializing attributes of class Badge"""
        super().__init__(name, description, type, location, availability, owned)
        self.title = title


class Test(Item):
    """Defining subclass Test"""

    def __init__(self, name='', description='', type='', location='', availability=True, owned=False, module='', mark='', **content):
        """Initializing attributes of class Badge"""
        super().__init__(name, description, type, location, availability, owned)
        self.module = module
        self.mark = mark
        self.content = content