# OOP Calculator Part 2 - Work in Progress (WIP)

## Introduction

The purpose of this assignment is to introduce you to the implementation of encapsulation, inheritance, polymorphism,
and abstraction. You will learn how to implement static, class, and instance methods as well as be introduced to your
first OOP design pattern that is called the "factory pattern."  You must write the implementation code to pass
the [teacher calculation](tests/test_calculation_teacher.py)
and [teacher calculator tests](tests/test_calculator_teacher.py). THIS WILL NOT WORK AT ALL WITHOUT YOU WRITING CODE.
YOU ARE GOING TO NEED TO KNOW HOW TO WRITE THE CODE AND LEARN BY FIXING ERROR MESSAGES. IF YOU NEED HELP POST A
SCREENSHOT TO SLACK OR THE DISCUSSION BOARD FOR THE UNIT.

# Grading Rubric
* 50 Points for calculator teacher tests passing
* 50 Points for calculation teacher tests passing

Note:  You will receive a 0 if you do not follow the Object Oriented Designs ideas in the unit.

### Assignment Instructions

1. Create a calculation abstract class
2. Add a create factory method that returns a class instance on the calculation class
3. Add a get result method on the calculation class that returns the result property
4. Add a set result method on the calculation class that sets the result property
5. Add get/set methods for val1 and val2 respectively
6. Add a constructor to the calculation class to set val1 and val2 properties
7. Create addition, subtraction, division and multiplication concrete classes that extend the calculator class
8. Add a constructor to each operation class .i.e. Addition, Multiplication, Division, and Subtraction that sets the
   result based on calling the correct operation

Instructor Video - Part 1 [Watch Here](https://youtu.be/hXqD_jbfCwQ)
Instructor Video - Part 2 - To Be Announced

### Module Readings:

1. Is
   Instance https://pynative.com/python-isinstance-explained-with-examples/#h-how-to-use-isinstance-function-in-python
2. Class Method Factor - https://dev.to/danyson/how-classmethod-in-python-helps-in-implementing-factory-methods-23gl

## Vocabulary

1. Class - Schematic for an object or a organizational tool like a folder to organize methods and properties into
   logical groups like a directory. Classes are the blueprints / design of your program
2. Instance - Copy of a class with its own data
3. Class Member - The methods and properties of a class. Think of the class as a club and the properties and methods are
   the members
4. Property - Data i.e. variable that describes the class
5. Method - Actions of the class
6. Abstract Class - Generic representation of a class type i.e. pet
7. Concrete Class - Specific representation of a class type i.e Dog, Cat, etc...
8. Factory Method - Generic method that returns an instance of a class
9. Constructor Method - The first method automatically called when a class is instantiated into an object / instance
10. Namespace - Equivalent to the files and folders that are used to logically organize a programs code
11. Static Method / Property - Used to namespace properties and methods that don't need to operate on the class or an
    instance of a class
12. Class Method - Used to operate on class data that is not a copy / instance uses the cls keyword
13. Instance Method - used to operate on the properties and methods of a class instance i.e. copy uses the self keyword
14. Override - When a child's class member replaces a parents member
15. Inheritance - Class Extension to connect e.g. connecting the calculation class to the Addition class to inherit the
    members of the calculation class
16. Abstraction - layering from simple to complex e.g. how the calculator add method creates an addition instance and
    returns the result of the calculation
17. Polymorphism - Many shapes - think of how we are using the get result method from the abstract calculation class to
    set the result for an addition
18. Encapsulation - Think of how we are creating multiple instances of Addition in the calculation test and each
    instance is independent from the other

### Prerequisite Knowledge

Note: Previously completed on static methods

## Steps to Complete the Assignment

1. Open Pycharm Pro / Pycharm Community and clone the assignment repository. Open up a terminal in Pycharm, run "pip
   install -r requirements.txt" and then run "pytest".  **If pycharm shows you an error about pip / requirements when
   you clone the repo just skip/cancel/dismiss the error and run the command in the terminal like I said above**
2. You will need to complete the requirements for the assignment and remove/replace the tests that are meant to fail
   that I placed in each file.
3. When your pytest passes just commit and push it back to the origin and the assignment will be graded automatically by
   GitHub running the test that you run locally.
4. Check that your tests pass on GitHub after you push the assignment and then submit a link to your repository to the
   assignment in Canvas. In GitHub on the repository, click the actions tab on GitHub to see your tests run. You will
   need to click on the autograding workflow to inspect that screen to see the detail test results.


