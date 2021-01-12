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