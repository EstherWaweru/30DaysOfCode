# Objective
# Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video.

# Task
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

#     A Student class constructor, which has 

# parameters:

#     A string, 

# .
# A string,
# .
# An integer,
# .
# An integer array (or vector) of test scores,

#         .
#     A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

# [Grading.png]

# Input Format

# The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.

# The first line contains
# , , and , separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes

# .

# Constraints

# Output Format

# Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

# Sample Input

# Heraldo Memelli 8135627
# 2
# 100 80

# Sample Output

#  Name: Memelli, Heraldo
#  ID: 8135627
#  Grade: O

# Explanation

# This student had
# scores to average: and . The student's average grade is . An average grade of corresponds to the letter grade , so the calculate() method should return the character'O'.


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        # super(Person,self).__init__(firstName,lastName,idNumber)when the super class inherits from object
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores
        
    def calculate(self):
        score=self.scores
        total=0
        for sc in score:
            total+=sc
        grade=total/len(score) 
        if (grade>=90 and grade<=100):
            grades='O'
        elif(grade>=80 and grade<90):
            grades='E'
        elif(grade>=70 and grade<80):
            grades='A'
        elif(grade>=55 and grade<70):
            grades='P'
        elif (grade>=40 and grade<55):
            grades='D'
        else:
            grades='T'
            
        return grades
        
        

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()