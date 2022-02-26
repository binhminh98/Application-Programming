"""
Module to generate Application Programming's learning materials
    1. Lecture notes
    2. Lecture tests
"""

import Functions.inventory as inv

# LECTURE NOTES #

inv.lecturenote_ap_1.content = {
    'note 0': "\nThis is the first lecture note of the Application Programming Module. \nPlease read it carefully because it may appears in your exam!!!",
    'note 1': "\n1. Software Engineer is a 'systematic approach to the analysis, design, \nassessment, implementation, test, maintenance \
and reengineering of software, that is, \nthe application of engineering to software'",
    'note 2': '\n2. Stakeholder is a person or company that is involved in a particular organization, project, system, etc.',
    'note 3': '\n3. There are two types of requirements: Functional and Non-functional',
    'note 4': "\n4. MoSCoW is short for: 'Must' - 'Should' - 'Could' - 'Would'",
    'note 5': '\n5. An Empathy Map is a user experience design asset',
    }

inv.lecturenote_ap_2.content = {
    'note 0': "\nThis is the second lecture note of the Application Programming Module. \nPlease read it carefully because it may appears in your exam!!!",
    'note 1': "\n1. There are 2 kinds of UML: Behavioral and Structural",
    'note 2': "\n2. UML diagrams: Use Case, Textual Use Case, Sequence, Class",
    'note 3': "\n3. A Use Case Diagram is for creating visual overview of the whole system",
    'note 4': "\n4. A Sequence Diagram is used to capture order of messages, flowing from one object to another",
    'note 5': "\n5. A Class Diagram is a static diagram that represents a view of a system",
    }

inv.lecturenote_ap_3.content = {
    'note 0': "\nThis is the third lecture note of the Application Programming Module. \nPlease read it carefully because it may appears in your exam!!!",    
    'note 1': "\n1. A statement is an instruction to the python interpreter that gives it a task to perform",
    'note 2': "\n2. Variable names can contain only letters, numbers and underscores",
    'note 3': "\n3. Variables are often described as boxes you can store values in",
    'note 4': "\n4. There are two numerical types in Python: Integers and Floats",
    'note 5': "\n5. A list is a collection of items in a particular order",
    }

inv.lecturenote_ap_4.content = {
    'note 0': "\nThis is the fourth lecture note of the Application Programming Module. \nPlease read it carefully because it may appears in your exam!!!",    
    'note 1': "\n1. All lists start from index 0, not index 1.",
    'note 2': "\n2. You can put anything in a list",
    'note 3': "\n3. If statements allow you to examine the current state of a program and respond appropriately",
    'note 4': "\n4. Input takes a string argument that is the output to the console",
    'note 5': "\n5. A for loop is a type of construct that will perform the same block of code a fixed number of times",
    }

inv.lecturenote_ap_5.content = {
    'note 0': "\nThis is the last lecture note of the Application Programming Module. \nPlease read it carefully because it may appears in your exam!!!",
    'note 1': "\n1. While loops will repeat the block of code for as long as the boolean expression evaluates to True",
    'note 2': "\n2. We can combine the creation of a list and the loop in one simple statement using List Comprehension",
    'note 3': "\n3. Tuple's value cannot be change",
    'note 4': "\n4. Each entry in a Dictionary is called a Key - Value Pair.",
    'note 5': "\n5. Dictionary's are dynamic. We can initialise them however we want, and we can updated the data\n inside them at any point",
    }

# TESTS #

inv.test_ap_1.content = {
    "1. _____________ is a 'systematic approach to the analysis, design, assessment, implementation, test,\n maintenance and reengineering of software, that is, the application of engineering to software.\n\nType the correct number: [1]software engineer [2]civil engineer [3]data engineer [4]business analytics'": '1',
    "2. _____________ is a person or company that is involved in a particular organization, project, system, etc.\n\nType the correct number: [1]project manager [2]risk lover [3]empathy map [4]stakeholder'": '4',
    "3. There are two types of requirements: _____________ and _____________\n\nType the correct number: [1]simple and complex [2]functional and non-functional [3]class and sequence [4]risk and return'": '2',
    "4. _____________ is short for: 'Must' - 'Should' - 'Could' - 'Would'\n\nType the correct number: [1]FBI [2]CIA [3]MoSCoW [4]FIFA'": '3',
    "5. An _____________ is a user experience design asset\n\nType the correct number: [1]use case diagram [2]empathy map [3]class diagram [4]sequence diagram'": '2',
}

inv.test_ap_2.content = {
    "1. There are 2 kinds of UML diagrams: _____________ and _____________\n\nType the correct number: [1]direct and indirect [2]top-down and bottom-up [3]simple and complex [4]behavioral and structural'": '4',
    "2. _____________: Use Case, Textual Use Case, Sequence, Class\n\nType the correct number: [1]Learning curves [2]UML diagrams [3]Softwares [4]Hardwares'": '2',
    "3. A _____________ diagram is for creating visual overview of the whole system\n\nType the correct number: [1]use case [2]sequence [3]class [4]textual use case": '1',
    "4. A _____________ diagram is used to capture order of messages, flowing from one object to another\n\nType the correct number: [1]use case [2]sequence [3]class [4]textual use case": '2',
    "5. A _____________ diagram is a static diagram that represents a view of a system\n\nType the correct number: [1]use case [2]sequence [3]class [4]textual use case": '3',
}

inv.test_ap_3.content = {
    "1. _____________ is an instruction to the python interpreter that gives it a task to perform\n\nType the correct number: [1]order [2]statement [3]move [4]do it": '2',
    "2. _____________ can contain only letters, numbers and underscores\n\nType the correct number: [1]your name [2]letters [3]variable name [4]emails": '3',
    "3. _____________ are often described as boxes you can store values in\n\nType the correct number: [1]hoops [2]loops [3]boxes [4]variables": '4',
    "4. There are two numerical types in Python: _____________ and _____________\n\nType the correct number: [1]integers and floats [2]function and method [3]positive and negative [4]real and imaginary": '1',
    "5. A _____________ is a collection of items in a particular order\n\nType the correct number: [1]book [2]string [3]list [4]float": '3',
}

inv.test_ap_4.content = {
    "1. All lists start from index ___, not index 1.\n\nType the correct number: [1]4 [2]0 [3]3 [4]10": '2',
    "2. You can put _________ in a list\n\nType the correct number: [1]book [2]anything [3]notes [4]tests": '2',
    "3. _____________ allow you to examine the current state of a program and respond appropriately\n\nType the correct number: [1]output [2]for loop [3]if statement [4]while loop": '3',
    "4. _____________ takes a string argument that is the output to the console\n\nType the correct number: [1]terminal [2]statement [3]quiz [4]input": '4',
    "5. A _____________ is a type of construct that will perform the same block of code a fixed number of times\n\nType the correct number: [1]for loop [2]string [3]integer [4]float": '1',
}

inv.test_ap_5.content = {
    "1. _____________ will repeat the block of code for as long as the boolean expression evaluates to True\n\nType the correct number: [1]while loop [2]for loop [3]if-elif-else [4]try-except": '1',
    "2. We can combine the creation of a list and the loop in one simple statement using _____________\n\nType the correct number: [1]list [2]dictionary [3]list comprehension [4]tuple": '3',
    "3. _____________'s value cannot be change\n\nType the correct number: [1]list [2]dictionary [3]variable [4]tuple": '4',
    "4. Each entry in a Dictionary is called a _____________ Pair.\n\nType the correct number: [1]simple-complex [2]key-value [3]method-function [4]list-tuple": '2',
    "5. _____________'s are dynamic. We can initialise them however we want, and we can update the\n data inside them at any point\n\nType the correct number: [1]tuple [2]float [3]dictionary [4]integer": '3',
}