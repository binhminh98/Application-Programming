"""
Module to define class TXTFile and its methods
    - TXT files are used to store data -> load, save progress
    - TXT files are used to store graphics -> print content
"""

class TXTFile():
    """Defining class TXTFile"""

    def __init__(self, path, mode=''):
        """Initializing attributes of class TXTFile"""
        self.path = path
        self.mode = mode

    def print_content(self):
        """Method to print content the file line by line"""
        with open(self.path,self.mode) as file_object:
            for line in file_object:
                print(line.strip())

    def save_data(self, content):
        """
        Method to save data to a text file (on write mode)
        All data files are in the Data folder
        """
        # Attribute to determine which contents of the game
        # we want to store in files
        with open(self.path,'w') as data_object:
            data_object.write(content)

    def load_users_data(self):
        """
        Method to load data from a text file (on read mode)
        All data files are in the Data folder
        """
        data = ''
        try:
            with open(self.path,'r') as data_object:
                data = data_object.read()
        except FileNotFoundError:
            pass
        return data

    @staticmethod
    def save_users_data(users):
        """
        Method to save a list of current users to a text file named: 'existing_users.txt'
        """
        users_file = TXTFile('Data/existing_users.txt')
        users_file.save_data(users)

    @staticmethod
    def convert_string_to_list(strings):
        """Function to convert a string into a list using eval() method"""
        lists = eval(strings)
        return lists

    @staticmethod
    def convert_list_to_string(lists):
        """Function to convert a list into a string"""
        strings = str(lists)
        return strings