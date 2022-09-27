# OOP Calculator Part 2 - Work in Progress (WIP)

## Introduction

The purpose of this assignment is to introduce you to the implementation of encapsulation, inheritance, polymorphism,
and abstraction. You will learn how to implement static, class, and instance methods as well as be introduced to your
first OOP design pattern that is called the "factory pattern."

### Assignment Requirements

1. Create a calculation abstract class
2. Add  a create factory method that returns a class instance on the calculation class
3. Add a get result method on the calculation class that returns the result property
4. Add a set result method on the calculation class that sets the result property
5. Add a constructor to the calculator class to set val1 and val2 properties
6. Create addition, subtraction, division and multiplication concrete classes that extend the calculator class
7. Add a class constructor to each operation class above that calls the parent constructor with "super" keyword and then set the result using the associated operation function i.e. set result using the addition function 
8. Write a test using the isInstance function to verify each instance type i.e. one test for each operation
9. Refactor your code so that each class is in its own file in the app folder
10. Write parameterized tests with at least 4 distinct sets of values 
11. Make sure all functions are tested.

Instructor Video - Part 1 [Watch Here](https://youtu.be/hXqD_jbfCwQ)
Instructor Video - Part 2 - To Be Announced


### Module Readings:

To Be Determined

### Prerequisite Knowledge

Note: Previously completed the unit testing module.

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


